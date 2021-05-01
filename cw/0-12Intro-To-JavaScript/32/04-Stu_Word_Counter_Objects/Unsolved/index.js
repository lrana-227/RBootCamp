function wordCount(myString) {
    // Convert string to an array of words
    var stringArray  = myString.split(" ");
   
  
    // An object to hold word frequency
    var wordFrequency = {};
      
    // Iterate through the array
    for (var i = 0; i < stringArray.length; i++) {
      var currWord = stringArray[i]
      if (currWord in wordFrequency){
        wordFrequency[currWord] +=1
      }
      else{
        wordFrequency[currWord] = 1;
      }
    }

    console.log(wordFrequency);
    return wordFrequency;
  }
  
  fre_op = wordCount("I yam what I yam and always will be what I yam");
  console.log(fre_op);