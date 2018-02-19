import System.IO
import System.Environment

main = do
  xs <- getArgs
  mapM (\x ->putStrLn $ reverseComple x) xs
  
    
comple :: Char -> Char
comple c
  | c == 'A' = 'T'
  | c == 'T' = 'A'
  | c == 'G' = 'C'
  | c == 'C' = 'G'
  | otherwise = 'X'
  
reverseComple :: String -> String
reverseComple [] =[]
reverseComple str =foldl(\acc x -> comple(x):acc) [] str
