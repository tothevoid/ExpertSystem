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

function setup(){
	// var width = getGraphWidth()
	// if (width <= canvasX)
	// 	width = canvasX;
    createCanvas(canvasX + 2000,canvasY);
	frameRate(60);
	startX = 400;
	startY = 100;
	scoreElem = createDiv('Дерево решений');
    scoreElem.position(startX-50, startY-50);
	scoreElem.class('score');
	var root = new Node(1);
	root.x = startX;
	root.y = startY;
	edges = graphSample(root);
	calculateCoordinates(root, edges);
	drawNodes(root);
}

function graphSample(root){
	n2 = new Node(2)
	n3 = new Node(3)
	n4 = new Node(4)
	n5 = new Node(5)
	n6 = new Node(6)
	n7 = new Node(7)
	// n8 = new Node(8)
	nodes = [root,n2,n3,n4,n5,n6,n7]
	e1 = new Edge(root, n2)
	e2 = new Edge(root, n3)
	e3 = new Edge(n3, n4)
	e4 = new Edge(n3, n5)
	e5 = new Edge(n2, n6)
	e6 = new Edge(n2, n7)
	// e7 = new Edge(n3, n8)
	return [e1,e2,e3,e4,e5,e6]
}

var updated_nodes = [];

function calculateCoordinates(root, edges){
	var childs = edges.filter(obj => {
		return obj.start.id === root.id;
	});
	result = [];
	var len = childs.length;
	if (len == 0)
		return;
	// if (len % 2 == 0){
	// 	// left = root.x + width/2 - (len * width - (width/2))
	// 	childs.forEach(function(child, ix){
	// 		child = child.end;
	// 		child.x = left + ix * width * 2
	// 		child.y = root.y + height * 2
	// 		result.push(child)
	// 	});
	// }
	// else{
	// 	// left = root.x + width/2 - ((len-1) * width - (width/2))
		
	// }
	res = []
	childs.forEach(function(child){
		res.push(child.end);
	});

	offsets = getOffset(res, edges, root.x);

	childs.forEach(function(child, ix){
		child = child.end;
		child.x = offsets[ix] 
		child.y = root.y + height * 2
		updated_nodes.push(child)
		line(root.x,root.y,child.x,child.y);
	});

	childs.forEach(function(child, ix){
		child = child.end;
		child.x = offsets[ix] 
		child.y = root.y + height * 2
		calculateCoordinates(child, edges)
	});

}

function drawNodes(root){
	ellipse(root.x, root.y, height, width);
	text(root.id, root.x-5, root.y+5);
	updated_nodes.forEach(function(node){
		ellipse(node.x, node.y, height, width);
		text(node.id, node.x-5, node.y+5);
	});
}

function getOffset(childs, edges, centerX){
	var widths = getChildsWidth(edges, childs)
	var summary_size = 0
	var distance = width
	widths.forEach(function(size, ix) {
		summary_size += width * (2 * size - 1) + distance * ix; 
	});
	var offsets = []
	var current_offset = centerX + width/2 - summary_size/2;
	if (widths.length == 0){
		return [0];
	}
	if (widths.length == 1){
		offsets.push(centerX)
	}
	else if(widths.length == 2){
		offsets.push(centerX + width/2 - summary_size/2)
		offsets.push(centerX + summary_size/2)
	}
	else if(widths.length > 2){
		offsets.push(current_offset)
		offsets.push(current_offset+summary_size)
		//+distance*(widths.length-1)
		step = current_offset+summary_size/(widths.length-1)
		widths.forEach(function(size, ix) {
			if (ix == 0 || ix == widths.length-1)
				return true;
			// left = current_offset + width/2 + (size * width - (width/2) * ix) + distance+distance;
			current_offset += distance * ix + (summary_size / widths.length) * ix;
			offsets.push(current_offset);
		});
	}
	return offsets;
}

function add(a, b) {
	return a + b;
}

function getChildsWidth(nodes, childs){
	var width = [];
	childs.forEach(function(parent) {
		var id = parent.id;
		var child_width = 0;
		nodes.forEach(function(node){
			if (node.start.id == id){
				child_width+=1;
			}
		});
		width.push(child_width)
	});
	return width;
}

class Node{
	constructor(id)
	{
		this.x = 0;
		this.y = 0;
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