String myDefaultPathWin = "C:/Code/GithubRepos/AdventOfCode/2024/3/";  //shoddy hack for convenience
import processing.sound.*;
import java.io.File;
import javax.swing.JFileChooser;
import javax.swing.JOptionPane;
import processing.net.*;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.util.List;
  color black = color(0);
  color white = color(255);
void exitWithMessage(String message) {
  JOptionPane.showMessageDialog(null, message, "Error", JOptionPane.ERROR_MESSAGE);
  println(message);
  System.exit(0);
}

String[] safeLoadStrings(String path, String errorMessage) {
  try {
    return loadStrings(path);
  }
  catch(java.lang.NullPointerException e) {
    println(errorMessage);
    return null;
  }
}

ArrayList<String> allMatches = new ArrayList<String>();
void setup() {
  background(100);
  size(800, 800);
  String inputfile = "C:/Code/GithubRepos/AdventOfCode/2024/3/input.txt";
    File fileObject = new File(inputfile);
  if (!fileObject.exists()) {
    JFileChooser chooser = new JFileChooser(myDefaultPathWin);
    chooser.setDialogTitle("Please select input.txt");
    if ( chooser.showOpenDialog(null) != JFileChooser.APPROVE_OPTION) {
      exitWithMessage("No path selected, terminating!");
    }

    inputfile = chooser.getSelectedFile().getAbsolutePath();
    println(inputfile);
    fileObject = new File(inputfile);
    if (!fileObject.exists()) {
      exitWithMessage("Path does not contain config file! Terminating!");
    }
  }
    String[] input_data = loadStrings(inputfile);
  
  String complete_input = String.join("",input_data);
  String input_test_data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))";
  
  println(input_data);
  String regex_pattern= "mul\\(\\d\\d?\\d?,\\d\\d?\\d?\\)";
  Pattern pattern = Pattern.compile(regex_pattern);
  Matcher matcher = pattern.matcher(complete_input);
  while(matcher.find()){
    allMatches.add(matcher.group());
  }
  println(allMatches);
}
void draw(){

  int accumulator = 0;
  int first_n;
  int second_n;
  int lines = 0;
  String[] parts;
  String second_string;
  String parts_object;
  String regex_pattern2= ",";
  for( int m_ind=0; m_ind< allMatches.size(); m_ind++){

    parts_object = allMatches.get(m_ind);
    parts = parts_object.split(regex_pattern2);
    println(parts[0].substring(4));
    second_string = parts[1];
    second_string = second_string.substring(0, second_string.length() -1);
    first_n = int(parts[0].substring(4));
    second_n = int(second_string);
    accumulator += first_n*second_n;

    

    fill(black);
    rect(0,0,800,800);
    fill(white);

    text(parts_object, 200, lines*2 );

    lines += 1;
    lines = lines % 100;
  }

  //fill(white);

  print(accumulator);
}
