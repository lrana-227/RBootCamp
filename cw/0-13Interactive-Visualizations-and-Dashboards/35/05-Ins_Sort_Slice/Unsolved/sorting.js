// Sort the array in descending order
var numArray = [1, 4,2, 3];
numArray.sort(function compareFunction(firstNum,secNum){
    return secNum - firstNum;
})
console.log(numArray)

// Sort the array in ascending order
var numArray2 = [3, 2, 1];
numArray2.sort()
console.log(numArray2)

// Sort the array in ascending order, using an arrow function
var numArray3 = [3, 2, 1];
numArray3.sort((firstNum,secNum) => secNum - firstNum);
console.log(numArray3)

// Reverse the array
var numArray4 = [1, 2, 3];
numArray4.sort((firstNum,secNum) => firstNum - secNum);
console.log(numArray4)
