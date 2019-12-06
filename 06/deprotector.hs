module Main
    where

import Data.Bits

import Codec.Picture
import Codec.Picture.Types
--import Graphics.Image

xorList :: [Int] -> [Int] -> [Int]
xorList = zipWith xor

getPair :: [[Int]] -> [[Int]]
getPair pixels =
    let pair = take 2 pixels in
        if length pair > 1
            then
                let newPixel = xorList (head pair) (pair !! 1) in
                    newPixel : getPair (newPixel : (drop 1 (tail pixels)))
            else
                []

dynToImg :: DynamicImage -> Image PixelRGB8
dynToImg (ImageRGB8 img) = img

imgToList :: Image PixelRGB8 -> [[Int]]
imgToList ([PixelRGB8] img) = map (pixelToList) img

pixelToList :: PixelRGB8 -> [Int]
pixelToList (PixelRGB8 r g b) = pToi r : pToi g : pToi b :[]

pToi :: Pixel8 -> Int
pToi p = fromIntegral p

-- [130, 105, 49] og B = [22, 168, 25] blir då A XOR B [148, 193, 40]
main :: IO ()
main = do
    Right inImage <- readImage "mush.png"
    let image = dynToImg inImage
    let list = imgToList image
    print list


--list = [[240, 33, 11], [205, 111, 102], [120, 96, 7], [45, 3, 202], [76, 237, 47]]