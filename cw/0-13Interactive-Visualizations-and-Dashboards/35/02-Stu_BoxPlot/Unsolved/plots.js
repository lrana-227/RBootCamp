var trace1 = {
  y : temps.newyork,
  type: "box",
  boxpoints:"all"
  };
  
  var trace2 = {
    y : temps.houston,
    type: "box"
  };
  
  var data = [trace1, trace2];
  
  var layout = {
    title : "New York VS Houston Temp Box Plot"
  };
  
  // Plot the chart to a div tag with id "plot"

  Plotly.newPlot("plot",data,layout);
  