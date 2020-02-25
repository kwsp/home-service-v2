import React from 'react';
import axios from 'axios';
import * as d3 from 'd3';

import fetchHomeAPI from './fetchData'
import apiBaseURL from './config'


class LinePlot extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            data: props.data,
            xTitle: props.xTitle,
            yTitle: props.yTitle,
            width: props.width,
            height: props.height,
            margin: props.margin
        }
    }

    fetchData() {
        axios({
            method: 'get',
            url: this.props.url,
            params: this.props.api_params
        });
    }



    render() {

        const h = this.state.height - 2 * this.state.margin;
        const w = this.state.width - 2 * this.state.margin;

        //number formatter
        const xFormat = d3.format('.2')

        //x scale
        const x = d3.scaleLinear()
          .domain(d3.extent(this.state.data, d => d.a)) //domain: [min,max] of a
          .range([this.state.margin, w]);

        //y scale
        const y = d3.scaleLinear().domain([0, d3.max(this.state.data, d=>d.b)]).range([h, this.state.margin]);

        const line = d3.line()
          .x(d => x(d.a))
          .y(d => y(d.b))
          .curve(d3.curveCatmullRom.alpha(0.5)) //curve line
     

        const xTicks = x.ticks(6).map(d => (
            x(d) > this.state.margin && x(d) < w ? 
              <g transform={`translate(${x(d)},${h + this.state.margin})`}>  
                <text>{xFormat(d)}</text>
                <line x1='0' y1='0' y2='5' transform="translate(0,-20)"/>
              </g>
            : null
        ))

        
        const yTicks = y.ticks(5).map(d => (
            y(d) > 10 && y(d) < h ? 
              <g transform={`translate(${this.state.margin},${y(d)})`}>  
                <text x="-12" y="5">{xFormat(d)}</text>
                <line x1='5' y1='0' y2='0' transform="translate(-5,0)"/>
                <line className='gridline' x1={w - this.state.margin} y1='0' y2='0' transform="translate(-5,0)"/> 
              </g>
            : null
        ))


        return  (
          <svg width={this.state.width} height={this.state.height}>
             <line className="axis" x1={this.state.margin} x2={w} y1={h} y2={h}/>
             <line className="axis" x1={this.state.margin} x2={this.state.margin} y1={this.state.margin} y2={h}/>
             <path d={line(this.state.data)}/>
             <g className="axis-labels">
               {xTicks}
             </g>
             <g className="axis-labels">
               {yTicks}
             </g>
          </svg>
        )

    }
}

export default LinePlot;
