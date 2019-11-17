var FramePlots = {};

function framePlot(div, title, datasets, options={}) {
    if (typeof FramePlots[div] === "undefined") {
        let data = [];
        for (k in datasets) {
            data.push({
                x: Array(datasets[k].length).fill().map((e, i) => i),
                y: datasets[k],
                name: k,
                mode: 'scatter'
            });
        }
        let layout = {
            title: {
                text: title
            },
            margin: {
                t: 80,
                l: 60,
                r: 60,
                b: 60
            }
        };
        if (options.yrange) {
            layout.yaxis = {
                range: options.yrange,
            }
        }
        if (options.xrange) {
            layout.xaxis = {
                range: options.xrange,
            }
        }
        FramePlots[div] = Plotly.newPlot(div, data, layout, { responsive: true });
    } else {
        let update = { x: [], y: [] }
        for (k in datasets) {
            update.x.push(Array(datasets[k].length).fill().map((e, i) => i));
            update.y.push(datasets[k]);
        }
        Plotly.restyle(div, update);
    }
}
