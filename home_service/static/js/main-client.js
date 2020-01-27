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


function updateCard() {
  $.ajax({
    url: 'home_api/room_temp',
    type: 'GET',
    async: true,
    data: {names: 'bedroom', n: 1},
    success: (returnJSON) => {
      document.getElementById('temperatureStatus').innerHTML = returnJSON.bedroom[0].y + 'C';
    }
  })

  $.ajax({
    url: 'home_api/room_humidity',
    type: 'GET',
    async: true,
    data: {names: 'laundry_closet', n: 1},
    success: (returnJSON) => {
      document.getElementById('humidityStatus').innerHTML = returnJSON.laundry_closet[0].y + '%';
    }
  })

}

function getPlotDataFromURL(url, data, plotname, yLabel, colourSeed) {
  $.ajax({
    url: url,
    type: 'GET',
    async: true,
    data: null,
    success: (returnJSON) => {

      traces = {}
      returnJSON["result"].forEach(function (v, i) {
        if (v.name in traces) {
            traces[v.name].push({x: moment(v.time), y: v.value})
        } else {
            traces[v.name] = [];
        }
      });

      if ("bedroom" in traces) {
          if (plotname.search("Humidity") >= 0) {
              document.getElementById('humidityStatus').innerHTML = traces.bedroom[0].y + '%';
          } else if (plotname.search("Temperature") >=0) {
              document.getElementById('temperatureStatus').innerHTML = traces.bedroom[0].y + 'C';
          }

      }

      
      datasets = []
      Object.keys(traces).forEach(function (v, i) {
        datasets.push({
          label: v,
          data: traces[v],
          borderColor: chartColors[Object.keys(chartColors)[i+colourSeed]],
          showLine: true,
          pointRadius: 0,
          lineTension: 0.3
        });
      });
      // Update plots
      areaPlotMulti(plotname, datasets, yLabel)
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
  getPlotDataFromURL(
    "home_api/server_temp",
    null,
    'graphServerTemp',
    'Temperature (°C)',
    0
  )
  getPlotDataFromURL(
    "home_api/room_temp",
    null,
    'graphTemperature',
    'Temperature (°C)',
    0,
  )
  getPlotDataFromURL(
    "home_api/room_humidity",
    null,
    'graphHumidity',
    'Humidity (%)',
    2
  )

  //updateCard()
  get_language();
})
