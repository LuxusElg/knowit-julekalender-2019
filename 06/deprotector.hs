module Main
    where

import Data.Bits

import Prelude as P
import Graphics.Image as I
import Graphics.Image.IO
import Graphics.Image.Interface

xorList :: [Int] -> [Int] -> [Int]
xorList = P.zipWith xor

getPair :: [[Int]] -> [[Int]]
getPair pixels =
    let pair = take 2 pixels in
        case (length pair) of
            0 -> []
            1 -> []
            2 -> let newPixel = xorList (head pair) (last pair) in
                    newPixel : getPair (last pair : (drop 1 (tail pixels)))

pixelToList :: Pixel RGB Double -> [Int]
pixelToList pixel = P.map (wToi) (toListPx (toWord8Px pixel))

wToi :: Word8 -> Int
wToi p = fromIntegral p
iTod :: Int -> Double
iTod p = fromIntegral p / 255.0

listToWord :: [Int] -> [Double]
listToWord = P.map iTod

wordToPixel :: [Double] -> Pixel RGB Double
wordToPixel (r:g:b:xs) = PixelRGB r g b :: Pixel RGB Double

listsToPixels :: [[Int]] -> [Pixel RGB Double]
listsToPixels lists = P.map wordToPixel (P.map listToWord lists)

combineLists :: [Pixel RGB Double] -> Int -> [[Pixel RGB Double]]
combineLists [] lLength = []
combineLists list lLength = 
    take lLength list : combineLists (drop lLength list) lLength

main :: IO ()
main = do
    image <- readImageRGB VU "mush.png"
    let lists = toLists image
    let converted = P.map (pixelToList) (concat lists)
    let xored = (head converted) : (getPair converted)
    let combined = combineLists (listsToPixels xored) (length (head lists))
    I.writeImage "out.png" (fromLists combined :: Image VU RGB Double)
