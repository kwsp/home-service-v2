// // Plots

var cacheSensorData;

function get_data() {
  var url = "/home_api/get_curr_data";
  $.ajax({
    url: url,
    type: 'GET',
    async: true,
    data: null,
    success: (sensorData) => {
      cacheSensorData = sensorData;
      // Update cards
      var len = sensorData.timestamp.length-1;
      var str = sensorData.temperature[len] + " C"
      document.getElementById('temperatureStatus').innerHTML = str;
      var str = sensorData.activity[len];
      document.getElementById('activityStatus').innerHTML = str;

      // Update plots
      areaPlot('graphTemperature', sensorData.timestamp, sensorData.temperature, 'Temperature (°C)')
      areaPlot('graphActivity', sensorData.timestamp, sensorData.activity, 'Activity (count)')
    }
  })
}

$(function() {
  "use strict";
  get_data();

})
