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
  get_language();
})
