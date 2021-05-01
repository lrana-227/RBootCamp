// The Stages of JavaScript
var theStagesOfJS = ["confidence", "sadness", "confusion", "realization", "debugging", "satisfaction"];

var  mapSample = theStagesOfJS.map(function(item){   //forEach is the same thing except map gives you the index number

  console.log(item)
});

// Challenge Activity
var princesses = [
  { name: "Rapunzel", age: 18 },
  { name: "Mulan", age: 16 },
  { name: "Anna", age: 18 },
  { name: "Moana", age: 16 }
];

// Log the name of each princess, follow by a colon, followed by their age
// Hint: use forEach
princesses.forEach(function(element,abc){
  console.log(`Position is ${abc+1} and Name is ${element.name} and Age is  ${element.age}`)
});

// Create an array of just the names from the princesses array
// Hint: use map
var pr_names= [];

abc = princesses.map(function(element){
  //pr_names.push(element.name);
  return element.name;
});

console.log(abc);
