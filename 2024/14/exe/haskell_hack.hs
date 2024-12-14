module Main where
import Control.Monad
import Text.Regex.TDFA
import qualified Data.Text as T

main :: IO ()
main = do
    s <- readFile "input.txt"
    let inputLines = T.lines $ T.pack s
    let myIndices = map doRegexWith inputLines
    let quadrants = []
    let zeroesList = filter (== 0) myIndices
    let zeroesListLength = length zeroesList
    let onesList = filter (== 1) myIndices
    let onesListLength = length onesList
    let twosList = filter (== 2) myIndices
    let twosListLength = length twosList
    let threesList = filter (== 3) myIndices
    let threesListLength = length threesList
    print (((zeroesListLength*onesListLength)*twosListLength)*threesListLength)


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
