function isAnagram(firstString, secondString) {
  const sortedFirstStr = firstString.toLowerCase().split("").sort().join("").replaceAll(" ", "");  
  const sortedSecondStr = secondString.toLowerCase().split("").sort().join("").replaceAll(" ", "");  
  if (sortedFirstStr == sortedSecondStr) {
    return true;
  } else{
    return false;
  }
}


console.log(isAnagram("Astronomer", "Moon starer")); 
console.log(isAnagram("School master", "The classroom"));
console.log(isAnagram("true", "false"));