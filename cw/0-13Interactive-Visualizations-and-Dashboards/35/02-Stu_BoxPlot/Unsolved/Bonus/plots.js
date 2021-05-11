// Create the Traces
var trace1 = {
  y: data.survival.map(val => Math.sqrt(val)),
  x: data.organ,
  type : "box"

  };
  
  // Create the data array for the plot
var data_a = [trace1];
  
  // Define the plot layout
  var layout = {
    title : "Cancer Data"
  };
  
  // Plot the chart to a div tag with id "plot"

  Plotly.newPlot("plot",data_a,layout);