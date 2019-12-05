module Main
    where

fronttoback string =
    let half = div (length string) 2 in
        drop half string ++ take half string

pairswap [] = []
pairswap string =
    let pair = take 2 string in
        (tail pair ++ [head pair]) ++ pairswap (drop (length pair) string)

tripleswap [] = []
tripleswap string =
    let front = take 3 string
        back = drop (length string - 3) string
        middle = take (length string - 6) (drop 3 string)
        in back ++ tripleswap middle ++ front

        -- test string= oepHlpslainttnotePmseormoTtlst
main = putStrLn (fronttoback (pairswap (tripleswap "tMlsioaplnKlflgiruKanliaebeLlkslikkpnerikTasatamkDpsdakeraBeIdaegptnuaKtmteorpuTaTtbtsesOHXxonibmksekaaoaKtrssegnveinRedlkkkroeekVtkekymmlooLnanoKtlstoepHrpeutdynfSneloietbol")))
