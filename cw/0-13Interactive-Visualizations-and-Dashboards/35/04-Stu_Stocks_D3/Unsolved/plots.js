var apiKey = "oVzzy_k9z871BBz1Bm23";

/* global Plotly */
var url =
  `https://www.quandl.com/api/v3/datasets/WIKI/AMZN.json?start_date=2016-10-01&end_date=2017-10-01&api_key=${apiKey}`;

/**
 * Helper function to select stock data
 * Returns an array of values
 * @param {array} rows
 * @param {integer} index
 * index 0 - Date
 * index 1 - Open
 * index 2 - High
 * index 3 - Low
 * index 4 - Close
 * index 5 - Volume
 */
function unpack(rows, index) {
  return rows.map(function(row) {
    return row[index];
  });
}

function buildPlot() {
  d3.json(url).then(function(data) {

    // Grab values from the data json object to build the plots
    var name = data.dataset.name;
    var stock = data.dataset.dataset_code;
    var startDate = data.dataset.start_date;
    var endDate = data.dataset.end_data;
    var dates = unpack(data.dataset.data,0);
    var closingPrices = unpack(data.dataset.data,4);


    var trace1 = {
      x:dates,
      y:closingPrices,
      type:"scatter"
    }

    var data  = [trace1];

    var layout = {
      title: `Closing Price of ${stock}`,
      xaxis: {title:"Date"},
      yaxis: {title:"Closing Price"}
    }
    Plotly.newPlot("plot", data, layout);

  });
}

buildPlot();
