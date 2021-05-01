// The new student and grade to add to the table
var newGrade = ["Wash", 79];

// Use D3 to select the table
var tableSelection =d3.select(".grades_table");


// Use d3 to create a bootstrap striped table
// http://getbootstrap.com/docs/3.3/css/#tables-striped

tableSelection.attr("class","table table-striped")


// Use D3 to select the table body
var mytable = tableSelection.select("tbody");
// Append one table row `tr` to the table body
var mytow = mytable.append("tr");
// Append one cell for the student name
mytow.append("td").text(newGrade[0]);
// Append one cell for the student grade
mytow.append("td").text(newGrade[1]);