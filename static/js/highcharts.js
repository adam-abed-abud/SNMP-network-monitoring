var chart;

/**
 * Request data from the server, add it to the graph and set a timeout
 * to request again
 */
function requestDataPort1() {
    $.ajax({
        url: '/live-data',
        success: function(point) {
            var series = chart.series[0],
                shift = series.data.length > 20; // shift if the series is
                                                 // longer than 20

            // add the point
            chart.series[0].addPoint(point, true, shift);
            chart.series[1].addPoint([point[0], point[2]], true, shift);

            // call it again after one second
            setTimeout(requestDataPort1, 1000);
        },
        cache: false
    });
}



function requestDataPort3() {
    $.ajax({
        url: '/live-data',
        success: function(point) {
            var series = chart2.series[0],
                shift = series.data.length > 20; // shift if the series is
                                                 // longer than 20

            // add the point
            chart2.series[0].addPoint([point[0], point[3]], true, shift);
            chart2.series[1].addPoint([point[0], point[4]], true, shift);


            // call it again after one second
            setTimeout(requestDataPort3, 1000);
        },
        cache: false
    });
}


function requestDataPort13() {
    $.ajax({
        url: '/live-data',
        success: function(point) {
            var series = chart3.series[0],
                shift = series.data.length > 20; // shift if the series is
                                                 // longer than 20

            // add the point
            chart3.series[0].addPoint([point[0], point[5]], true, shift);
            chart3.series[1].addPoint([point[0], point[6]], true, shift);


            // call it again after one second
            setTimeout(requestDataPort13, 1000);
        },
        cache: false
    });
}


function requestDataPort15() {
    $.ajax({
        url: '/live-data',
        success: function(point) {
            var series = chart4.series[0],
                shift = series.data.length > 20; // shift if the series is
                                                 // longer than 20

            // add the point
            chart4.series[0].addPoint([point[0], point[7]], true, shift);
            chart4.series[1].addPoint([point[0], point[8]], true, shift);


            // call it again after one second
            setTimeout(requestDataPort15, 1000);
        },
        cache: false
    });
}






$(document).ready(function() {
    chart = new Highcharts.Chart({
        chart: {
            renderTo: 'data-container-port-1',
            defaultSeriesType: 'spline',
            events: {
                load: requestDataPort1
            }
        },
        title: {
            text: 'PORT 1'
        },
        xAxis: {
            minPadding: 0.4,
            maxPadding: 0.4,
            title: {
                text: 'Time',
                margin: 20
            },
            type: 'datetime',
            tickPixelInterval: 150,
            maxZoom: 20 * 1000
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: 'Throughput [B/s]',
                margin: 80
            }
        },
        series: [{
            name: 'INPUT',
            data: []
        }, {
            name: 'OUTPUT',
            //data: []
        }]
    });
});




$(document).ready(function() {
    chart2 = new Highcharts.Chart({
        chart: {
            renderTo: 'data-container-port-3',
            defaultSeriesType: 'spline',
            events: {
                load: requestDataPort3
            }
        },
        title: {
            text: 'PORT 3'
        },
        xAxis: {
            minPadding: 0.4,
            maxPadding: 0.4,
            title: {
                text: 'Time',
                margin: 20
            },
            type: 'datetime',
            tickPixelInterval: 150,
            maxZoom: 20 * 1000
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: 'Throughput [B/s]',
                margin: 80
            }
        },
        series: [{
            name: 'INPUT',
            data: []
        }, {
            name: 'OUTPUT',
            data: []
        }]
    });
});




$(document).ready(function() {
    chart3 = new Highcharts.Chart({
        chart: {
            renderTo: 'data-container-port-13',
            defaultSeriesType: 'spline',
            events: {
                load: requestDataPort13
            }
        },
        title: {
            text: 'PORT 13'
        },
        xAxis: {
            minPadding: 0.4,
            maxPadding: 0.4,
            title: {
                text: 'Time',
                margin: 20
            },
            type: 'datetime',
            tickPixelInterval: 150,
            maxZoom: 20 * 1000
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: 'Throughput [B/s]',
                margin: 80
            }
        },
        series: [{
            name: 'INPUT',
            data: []
        }, {
            name: 'OUTPUT',
            data: []
        }]
    });
});




$(document).ready(function() {
    chart4 = new Highcharts.Chart({
        chart: {
            renderTo: 'data-container-port-15',
            defaultSeriesType: 'spline',
            events: {
                load: requestDataPort15
            }
        },
        title: {
            text: 'PORT 15'
        },
        xAxis: {
            minPadding: 0.4,
            maxPadding: 0.4,
            title: {
                text: 'Time',
                margin: 20
            },
            type: 'datetime',
            tickPixelInterval: 150,
            maxZoom: 20 * 1000
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: 'Throughput [B/s]',
                margin: 80
            }
        },
        series: [{
            name: 'INPUT',
            data: []
        }, {
            name: 'OUTPUT',
            data: []
        }]
    });
});

