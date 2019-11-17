// // Plots

function get_data() {
  let url = "/home_api/get_curr_data";
  $.ajax({
    url: url,
    type: 'GET',
    async: true,
    data: null,
    success: (sensorData) => {
      // Update cards
      var len = sensorData.timestamp.length-1;
      var str = sensorData.temperature[len] + " C"
      document.getElementById('temperatureStatus').innerHTML = str;
      var str = sensorData.activity[len];
      document.getElementById('activityStatus').innerHTML = str;

      timestamp = []
      sensorData.timestamp.forEach(t => {
        timestamp.push(moment.unix(t))
        // .format('MM/DD/YY HH:mm'))
      })

      // Update plots
      areaPlot('graphTemperature', timestamp, sensorData.temperature, 'Temperature (°C)')
      areaPlot('graphActivity', timestamp, sensorData.activity, 'Activity (count)')
    }
  })
}

function get_pi_temp() {
  let url = "/home_api/pi_temp";
  $.ajax({
    url: url,
    type: 'GET',
    async: true,
    data: null,
    success: (piTemp) => {

      timestamp = []
      piTemp['TigerPi']['timestamp'].forEach(t => {
        timestamp.push(moment.unix(t))
      })
      timestamp4 = []
      piTemp['TigerPi4']['timestamp'].forEach(t => {
        timestamp4.push(moment.unix(t))
      })
      timestampW = []
      piTemp['TigerPiZeroW']['timestamp'].forEach(t => {
        timestampW.push(moment.unix(t))
      })


      datasets = []
      datasets.push({
        label: 'TigerPi',
        data: piTemp['TigerPi']['temperature'],
        backgroundColor: "rgba(78, 115, 223, 0.25)",
        borderColor: "rgba(78, 115, 223, 1)",
        lineTension: 0.3,
        pointRadius: 0,
      })
      datasets.push({
        type: 'line',
        label: 'TigerPi4',
        xAxisID: 'x-axis-2',
        data: {
          x: timestamp4,
          y: piTemp['TigerPi4']['temperature']
        },
        backgroundColor: "rgba(78, 115, 223, 0.25)",
        borderColor: "rgba(78, 115, 223, 1)",
        lineTension: 0.3,
        pointRadius: 0,
      })
      datasets.push({
        type: 'line',
        label: 'TigerPiZeroW',
        xAxisID: 'x-axis-3',
        data: {
          x: timestampW,
          y: piTemp['TigerPiZeroW']['temperature']
        },
        backgroundColor: "rgba(78, 115, 223, 0.25)",
        borderColor: "rgba(78, 115, 223, 1)",
        lineTension: 0.3,
        pointRadius: 0,
      })

      // Update plots
      areaPlot('graphPiTemp', timestamp, datasets, 'Temperature (°C)')
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
  get_data();
  get_pi_temp();
  get_language();
})
