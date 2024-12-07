// See https://aka.ms/new-console-template for more information
using System.ComponentModel.DataAnnotations;

Console.WriteLine("Hello, World!");
IEnumerable<string> inputData = File.ReadLines("C:\\Code\\GithubRepos\\AdventOfCode\\2024\\7\\input.txt");
long candiateAccumulator = 0;
foreach (string line in inputData){
    string[] leftAndRight = line.Split(":");
    long testNumber = long.Parse(leftAndRight[0]);
    string[] componentsString = leftAndRight[1].Split(" ");
    long[] components = componentsString.Skip(1).Select(long.Parse).ToArray();
    int numOfOperands = components.Length ;
    int numOfOperators = numOfOperands - 1;
    for (int binNumber=0; binNumber < 1 << numOfOperators; binNumber++){
        long miniAccumulator = components[0];
        for( int runningIndex = 0; runningIndex < numOfOperators; runningIndex++ ){
            int currentFlag = binNumber >>> runningIndex&1;
            if (currentFlag == 0){
                miniAccumulator = miniAccumulator + components[runningIndex+1];
            } else {
                miniAccumulator = miniAccumulator * components[runningIndex+1];
            }


        }
        if (miniAccumulator == testNumber) {
            candiateAccumulator += testNumber;
            break;
        }
    }
}
Console.WriteLine(candiateAccumulator);