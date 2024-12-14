import Control.Monad
import Data.Char
import Text.Regex.TDFA

main = do
    s <- readFile "input.txt"
    doSomething s

doSomething :: String -> IO ()
doSomething str = putStrLn str
myRegex = "\\-?[0-9]+"
testInput = "p=31,100 v=-36,-71"
outputs = getAllTextMatches $ (testInput =~ myRegex) :: [String]
