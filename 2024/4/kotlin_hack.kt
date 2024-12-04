package com.example.linkedinproj

import android.os.Bundle
import android.util.Log
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.linkedinproj.ui.theme.LinkedinProjTheme
import java.io.File

class MainActivityAOC : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            LinkedinProjTheme {
                Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
                    Greeting_AOC(
                        name = "Android",
                        modifier = Modifier.padding(innerPadding)
                    )
                }
            }
        }
    }
}

fun readFileAsLinesUsingReadLines(fileName: String): List<String>
        = File(fileName).readLines()

fun tryPath(i: Int, j: Int, data:List<String>, numOfLines: Int, lengthOfLines: Int): String{
    var line = ""
    line = if (i < 0 || i >= numOfLines || j < 0 || j >= lengthOfLines){
        "0"

    }
    else {
        data[i].substring(j, j+1)
    }
    Log.d("AOC", line)
    return line
}

fun TestForXMAS(row: Int, col: Int, data:List<String>, numOfLines: Int, lengthOfLines: Int): Int{
    val directions = intArrayOf(-1,0,1);
    val comparisonList = mutableListOf("M", "A", "S");
    var myAccumulator = 0;
    for (i in directions){
        for (j in directions){
            var testList = mutableListOf<String>()
            testList.add(tryPath(row+i, col+j, data, numOfLines, lengthOfLines))
            testList.add(tryPath(row+2*i, col+2*j, data, numOfLines, lengthOfLines))
            testList.add(tryPath(row+3*i, col+3*j, data, numOfLines, lengthOfLines))
            if (testList == comparisonList){
                myAccumulator += 1;
            }
        }

    }
    return myAccumulator
}

@Composable
fun Greeting_AOC(name: String, modifier: Modifier = Modifier) {
    val fileLocation = "C:\\Code\\GithubRepos\\AdventOfCode\\2024\\4\\input.txt";
    val input = readFileAsLinesUsingReadLines(fileLocation);
    var accumulator = 0;
    val numOfLines = input.size;
    val lengthOfLines = input[0].length;
    var testText: String
    testText = tryPath(7,2, input, numOfLines, lengthOfLines)
    testText = tryPath(5,2, input, numOfLines, lengthOfLines)

    for (i in 0 until numOfLines){
        for (j in 0 until lengthOfLines){
            if (input[i].substring(j, j+1) == "X"){
            accumulator += TestForXMAS(i, j, input, numOfLines, lengthOfLines)
        }
        }
    }

    Column {
        Text(
            text = accumulator.toString(),
            modifier = modifier,
            textAlign = TextAlign.Center,
            style = TextStyle(fontSize = 10.sp)
        )
        LazyColumn(
            modifier = modifier
        ) {
            items(input) { line ->
                Text(
                    text = line,
                    textAlign = TextAlign.Center,
                    style = TextStyle(fontSize = 10.sp),
                    maxLines = 1, // Prevent line breaks
                    overflow = TextOverflow.Ellipsis // Truncate with ellipsis
                )
            }
        }
    }
//    for (line in input) {
//        Text(
//            text = line,
//            modifier = modifier,
//            textAlign = TextAlign.Center,
//            style = TextStyle(fontSize = 10.sp)
//        )
//    }
}

@Preview(showBackground = true)
@Composable
fun GreetingPreview_AOC() {
    LinkedinProjTheme {
        Greeting_AOC("Android")
    }
}