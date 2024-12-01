const fileInput = document.getElementById('fileInput');
      
const file = fileInput.files[0];
if (file){ 
  const reader = new FileReader();

  reader.onload = (event) => {
    const fileContent = event.target.result;
    doAThing(fileContent)
  };

  reader.readAsText(file);  

};
function p(text){console.log(text)}
function doAThing(filestring){

lineArray = filestring.split("\r\n")
lineArray.pop()
let leftArray = [];
let rightArray= [];
for(let index = 0; index<1000; index++){
    element = lineArray[index];
    let smolArray = element.split("   ");
    leftArray.push(smolArray[0]);
    rightArray.push(smolArray[1]);
}
leftArray.sort()
rightArray.sort()
let accumulator = 0;
for(let index = 0; index<1000; index++){
    accumulator += Math.abs(leftArray[index]- rightArray[index])
}
p(accumulator)

}
