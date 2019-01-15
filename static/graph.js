new p5();

var canvasX = window.innerWidth
|| document.documentElement.clientWidth
|| document.body.clientWidth;

var canvasY =  window.innerHeight
|| document.documentElement.clientHeight
|| document.body.clientHeight;

//nodes and spaces width
const width = 50;
//layers distance
const height = 50;

const startX = 1000;
const startY = 100;
var totalNodes = 0;

const updated_nodes = [];
var edges;
var nodes = [];
var counter = 0;
var awaitingToProcess = []

function setup(){
	// var width = getGraphWidth()
	// if (width <= canvasX)
	// 	width = canvasX;
    createCanvas(canvasX + 2000,canvasY);
	frameRate(60);
	getGraph();
}

var lastX = 0;
var lastY = 0;

function draw(){
	if (lastX == mouseX && lastY == mouseY){
		return
	}
	if (nodes.length != 0){
		nodes.forEach(function(node){
			lastX = node.x;
			lastY = node.y;
			if (mouseX <= lastX + 15 && mouseX >= lastX - 15 && mouseY >= lastY - 15 && mouseY <= lastY + 15){
				document.getElementById('info').innerHTML = node.description + "\n" + node.rule;
			} 
		});
	}
}

function getGraph(){
    $.ajax({
        url: "/get_graph",
        type: "GET",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        success: function(data){
			// parts = data.split('\n')
			// nodes = JSON.parse(parts[0])
			// edges = JSON.parse(parts[1])
			nodes = data.nodes;
			drawGraph(data.nodes,data.edges);
        }
    })
}

function drawGraph(nodes, edges){
	edges.forEach(function(edge){
		var start = nodes.filter(obj => {
			return obj.id === edge.start.id;
		});
		var end = nodes.filter(obj => {
			return obj.id === edge.end.id;
		});
		line(start[0].x,start[0].y,end[0].x,end[0].y);
	});

	nodes.forEach(function(node){
		ellipse(node.x, node.y, height, width);
		text(node.id, node.x-5, node.y+5);
	});
}

class GraphNode{
	constructor(id, x, y, description, rule){
		this.x = x;
		this.y = y;
		this.id = id;
		this.description = description;
        this.rule = rule;
	}
}
class GraphEdge{
	constructor(start_node,end_node){
		this.start = start_node
		this.end = end_node
	}
}