// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// Area Chart Example
//var dataset = {
//    x: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
//    y: [0, 10000, 5000, 15000, 10000, 20000, 15000, 25000, 20000, 30000, 25000, 40000],
//    label: "Earnings",
//}

charts = Object(); 

function areaPlot(id, xlabel, ydata, label) {
  var ctx = $("#"+id);
  var myLineChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: xlabel,  
      datasets: [{
        data: ydata,
        label: label,
        lineTension: 0.3,
        // backgroundColor: "rgba(78, 115, 223, 0.25)",
        borderColor: "rgba(78, 115, 223, 1)",
        pointRadius: 0,
      }],
    },
    options: {
      maintainAspectRatio: false,
      layout: {
        padding: {
          left: 2,
          right: 5,
          top: 10,
          bottom: -5 
        }
      },
      scales: {
        xAxes: [{
          type: 'time',
          time: {
            displayFormats: {
              second: 'MMM YYYY'
            }, 
          },
          gridLines: {
            // color: "rgb(234, 236, 244)",
            // zeroLineColor: "rgb(234, 236, 244)",
            display: true,
            drawBorder: true,
            borderDash: [2],
            zeroLineBorderDash: [2]
          },
          ticks: {
            fontColor: "rgb(234, 236, 244)",
          }
        }],
        
        yAxes: [{
          scaleLabel: {
            display: true,
            labelString: label,
            fontColor: "rgb(234, 236, 244)",
            fontSize: 13
          },
          ticks: {
            maxTicksLimit: 5,
            // padding: 10,
            fontColor: "rgb(234, 236, 244)",
            // callback: function(value, index, values) {
            //   return (value).toFixed(1);
            // }
          },
          gridLines: {
            color: "rgb(234, 236, 244)",
            zeroLineColor: "rgb(234, 236, 244)",
            drawBorder: false,
            borderDash: [2],
            zeroLineBorderDash: [2]
          },
        }],
      },
      legend: {
        display: false 
      },
      tooltips: {
        backgroundColor: "rgb(255,255,255)",
        bodyFontColor: "#858796",
        titleFontColor: '#6e707e',
        borderColor: '#dddfeb',
        borderWidth: 1,
        xPadding: 10,
        yPadding: 10,
        displayColors: false,
        intersect: false,
        mode: 'index',
        // callbacks: {
        //   label: function(tooltipItem, chart) {
        //     var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
        //     return datasetLabel + ': ' + tooltipItem.yLabel;
        //   }
        // }
      }
    }
  }); 
  charts[id] = myLineChart;
}

function areaPlotMulti(id, datasets, label) {
  var ctx = $("#"+id);
  var myLineChart = new Chart(ctx, {
    type: 'scatter',
    data: {datasets},
    options: {
      maintainAspectRatio: false,
      layout: {
        padding: {
          left: 2,
          right: 5,
          top: 10,
          bottom: -5 
        }
      },
      scales: {
        xAxes: [{
          type: 'time',
          time: {
            displayFormats: {
              second: 'MMM YYYY'
            }
          },
          gridLines: {
            // color: "rgb(234, 236, 244)",
            // zeroLineColor: "rgb(234, 236, 244)",
            display: true,
            drawBorder: true,
            borderDash: [2],
            zeroLineBorderDash: [2]
          },
          ticks: {
            fontColor: "rgb(234, 236, 244)",
          }
        }],
        
        yAxes: [{
          scaleLabel: {
            display: true,
            labelString: label,
            fontColor: "rgb(234, 236, 244)",
            fontSize: 13
          },
          ticks: {
            maxTicksLimit: 5,
            padding: 10,
            fontColor: "rgb(234, 236, 244)",
            // callback: function(value, index, values) {
            //   return (value).toFixed(1);
            // }
          },
          gridLines: {
            color: "rgb(234, 236, 244)",
            zeroLineColor: "rgb(234, 236, 244)",
            drawBorder: false,
            borderDash: [2],
            zeroLineBorderDash: [2]
          },
        }],
      },
      tooltips: {
        backgroundColor: "rgb(255,255,255)",
        bodyFontColor: "#858796",
        //color: "#858796",
        titleFontColor: '#6e707e',
        //borderColor: '#dddfeb',
        borderWidth: 1,
        xPadding: 10,
        yPadding: 10,
        intersect: false,
        mode: 'nearest',
        callbacks: {
           title: function(tooltipItem, chart){
              return tooltipItem[0].xLabel.format('DD/MM/YYYY HH:mm:ss');
           },
           label: function(tooltipItem, chart) {
             var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
             return ' '+datasetLabel + ': ' + tooltipItem.yLabel;
          }
        }
      }
    }
  });
  charts[id] = myLineChart;
}

//areaPlot("myAreaChart", dataset);
