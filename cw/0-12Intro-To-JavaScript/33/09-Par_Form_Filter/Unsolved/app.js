// Assign the data from `data.js` to a descriptive variable
var people = data;

// Select the button
var button = d3.select("#button");

// Select the form
var form = d3.select("#form");

// Create event handlers 
button.on("click", runEnter);
form.on("submit",runEnter);

function Filter(bloodType){
  var dict = [];
  for (var i =0; i< people.length; i++)
  {
    if (bloodType == people.bloodType){
      dict.push(people[i])
    }
  }
}

// Complete the event handler function for the form
function runEnter() {

  // Prevent the page from refreshing
  d3.event.preventDefault();
  // Select the input element and get the raw HTML node
  var input_ele = d3.select(".form-control");
  // Get the value property of the input element
  var input_val = input_ele.property("value");
  console.log(input_val);
 
  // Use the form input to filter the data by blood type

  if (input_val == "A+"){
    Filter("A+");
  }
  else if (input_val == "A-"){
    Filter("A-");
  }
  else if (input_val == "B-"){
    Filter("B-");
  }
  else if (input_val == "B+"){
    Filter("B+");
  }
  else if (input_val == "AB-"){
    Filter("AB-");
  }
  else if (input_val == "AB+"){
    Filter("AB+");
  }
  else if (input_val == "0-"){
    Filter("O-");
  }
  else {
    Filter("O+");
  }


  // BONUS: Calculate summary statistics for the age field of the filtered data

  // First, create an array with just the age values

  // Next, use math.js to calculate the mean, median, mode, var, and std of the ages

  // Finally, add the summary stats to the `ul` tag
};
