d3.csv("./hours-of-tv-watched.csv").then(function(tvData)
{
    //console.log(tvData);
//map makes output an array 
    var names = tvData.map(data => data.name);
    console.log(names);

    var hrs = tvData.map(data => parseInt(data.hours));
    console.log(hrs);
});
