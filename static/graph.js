new p5();

var canvasX = window.innerWidth
|| document.documentElement.clientWidth
|| document.body.clientWidth;

var canvasY =  window.innerHeight
|| document.documentElement.clientHeight
|| document.body.clientHeight;

function setup(){
	var width = getGraphWidth()
	if (width <= canvasX)
		width = canvasX;
    createCanvas(canvasX + 2000,canvasY);
	frameRate(60);
	startX = 400;
	startY = 100;
	scoreElem = createDiv('Дерево решений');
    scoreElem.position(startX-50, startY-50);
	scoreElem.class('score');
	sample = graphSample()
	drawTree(sample[0], sample[1])
}

function graphSample(){
	n1 = new Node(startX,startY,1)
	n2 = new Node(startX-50,startY+50,2)
	n3 = new Node(startX+50,startY+50,3)
	nodes = [n1,n2,n3]
	e1 = new Edge(n1, n2)
	e2 = new Edge(n1, n3)
	edges = [e1,e2]
	return [nodes,edges]
}

function drawTree(nodes, edges){
	edges.forEach(function(element) {
		line(element.start.x,element.start.y,element.end.x,element.end.y);
  	});
	nodes.forEach(function(element) {
		ellipse(element.x, element.y, 25, 25);
  	});
}

function getGraphWidth(){

}

function parseResponse(){
	
}

class Node{
	constructor(x,y, id)
	{
		this.x = x;
		this.y = y;
		this.id = id;
	}
}

class Edge{
	constructor(start_node,end_node)
	{
		this.start = start_node
		this.end = end_node
	}
}