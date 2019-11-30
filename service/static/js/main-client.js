// // Plots

chartColors = {
  red: 'rgb(255, 99, 132)',
  green: 'rgb(75, 192, 192)',
  blue: 'rgb(54, 162, 235)',
  orange: 'rgb(255, 159, 64)',
  yellow: 'rgb(255, 205, 86)',
  purple: 'rgb(153, 102, 255)',
  grey: 'rgb(201, 203, 207)'
};

const serverNames = ['TigerPi', 'TigerPi4', 'TigerPiZeroW']
const tempNames = []

// function get_sensor_temp() {
//   let url = "/home_api/sensor_temp";
//   $.ajax({
//     url: url,
//     type: 'GET',
//     async: true,
//     data: {n: 300},
//     success: (sensorData) => {
//       datasets = []

//       // Update cards
//       var len = sensorData.timestamp.length-1;
//       var str = sensorData.temperature[len] + " C"
//       document.getElementById('temperatureStatus').innerHTML = str;
//       var str = sensorData.activity[len];
//       document.getElementById('activityStatus').innerHTML = str;

//       sensorData.timestamp.forEach(function(part, index, arr) {
//         arr[index] = moment.unix(part);
//       })

//       // Update plots
//       areaPlot('graphTemperature', sensorData.timestamp, sensorData.temperature, 'Temperature (°C)')
//       areaPlot('graphActivity', sensorData.timestamp, sensorData.activity, 'Activity (count)')
//     }
//   })
// }

function updateCard() {
  $.ajax({
    url: 'home_api/sensor_temp',
    type: 'GET',
    async: true,
    data: {name: 'bedroom', n: 1},
    success: (returnJSON) => {
      document.getElementById('temperatureStatus').innerHTML = returnJSON.bedroom[0].y;
    }
  })

}

function getNameTempFromURL(url, data, plotname) {
  $.ajax({
    url: url,
    type: 'GET',
    async: true,
    data: null,
    success: (returnJSON) => {
      datasets = []
      Object.keys(returnJSON).forEach(function (v, i) {
        returnJSON[v].forEach(function (part, index, arr) {
          arr[index].x = moment.unix(arr[index].x);
        });
        datasets.push({
          label: v,
          data: returnJSON[v],
          borderColor: chartColors[Object.keys(chartColors)[i]],
          showLine: true,
          pointRadius: 0,
          lineTension: 0.3
        });
      });
      // Update plots
      areaPlotMulti(plotname, datasets, 'Temperature (°C)')
    }
  })
}

function get_language() {
  let url = "https://api.github.com/repos/haolinnie/home-service-v2/languages"
  $.ajax({
    url: url,
    type: 'GET',
    async: true,
    success: (language_data) => {
      pieChart('myPieChart', {
          labels: Object.keys(language_data),
          data: Object.values(language_data),
          backgroundColor: ['#1cc88a', '#4e73df', '#36b9cc', '#f6c23e'],
          hoverBackgroundColor: ['#17a673', '#2e59d9', '#2c9faf', '#DBAD23'],
      });
    }
  })
}

$(function() {
  "use strict";
  updateCard()
  getNameTempFromURL(
    "home_api/pi_temp",
    null,
    'graphPiTemp'
  )
  getNameTempFromURL(
    "home_api/sensor_temp",
    {n: 300},
    'graphTemperature'
  )

  get_language();
})
