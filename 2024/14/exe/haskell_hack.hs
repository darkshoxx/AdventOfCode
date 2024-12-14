module Main where
import Control.Monad
import Text.Regex.TDFA
import qualified Data.Text as T

main :: IO ()
main = do
    s <- readFile "input.txt"
    let inputLines = T.lines $ T.pack s
    let myIndices = map doRegexWith inputLines
    let quadrants = [0,1,2,3]
    let myFilter p = (== p)
    let myListConstructor r = filter (myFilter r) myIndices
    let myfunc q = length (myListConstructor q)
    let toTakeProduct = map myfunc quadrants
    let number = product toTakeProduct
    -- let number = product(map (\q -> length (filter (== q) myIndices)) quadrants)
    print number


doRegexWith :: T.Text -> Int
doRegexWith input = 
    let inputStr = T.unpack input
        myRegex = "\\-?[0-9]+"
        outputs = getAllTextMatches $ (inputStr =~ myRegex) :: [String]
        [xPos, yPos] = calculateXPos outputs
        
        myIndex = indexToIncrement [xPos, yPos]
    in myIndex
    -- forM_ outputs printMyLine
    -- printMyLine "NEXT"


indexToIncrement :: [Int] -> Int
indexToIncrement positions
    | positions!!0 < 50 && positions!!1 < 51 = 0
    | positions!!0 < 50 && positions!!1 > 51 = 1
    | positions!!0 > 50 && positions!!1 < 51 = 2
    | positions!!0 > 50 && positions!!1 > 51 = 3
    | otherwise = 10


calculateXPos :: [String] -> [Int]
calculateXPos positionsList =
    let xPosString = positionsList!!0
        yPosString = positionsList!!1
        xVelString = positionsList!!2
        yVelString = positionsList!!3
        xPos = read xPosString
        yPos = read yPosString 
        xVel = read xVelString
        yVel = read yVelString
        xPosNew = mod (xPos + 100*xVel) 101
        yPosNew = mod (yPos + 100*yVel) 103
    in [xPosNew, yPosNew]

printMyLine :: String -> IO ()
printMyLine str = putStrLn str
