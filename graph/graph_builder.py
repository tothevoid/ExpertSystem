#nodes and spaces width
width = 50
#layers distance
height = 50

startX = 1000
startY = 100
totalNodes = 0

updated_nodes = []
edges = []
counter = 0

def get_graph(new_edges = None):
    global edges
    root = GraphNode(1)
    root.x = startX
    root.y = startY
    if new_edges == None or len(new_edges) == 0:
        edges = get_sample(root)
    else:
        edges = new_edges
    updated_nodes.append(root)
    calculate_coordinates(root)
    return edges, updated_nodes

def get_sample(root):
	n2 = GraphNode(2)
	n3 = GraphNode(3)
	n4 = GraphNode(4)
	n5 = GraphNode(5)
	n6 = GraphNode(6)
	n7 = GraphNode(7)
	n8 = GraphNode(8)
	n9 = GraphNode(9)
	n10 = GraphNode(10)

	# n11 = Node(11)
	# n12 = Node(12)
	# n13 = Node(13)

	# n14 = Node(14)
	# n15 = Node(15)
	# n16 = Node(16)

	# n17 = Node(16)
	# n18 = Node(16)

	e1 =  GraphEdge(root, n2)
	e2 =  GraphEdge(root, n3)
	e3 =  GraphEdge(n2, n6)
	e4 =  GraphEdge(n2, n7)
	e5 =  GraphEdge(n3, n4)
	e6 =  GraphEdge(n3, n5)
	e7 =  GraphEdge(n3, n8)
	e8 =  GraphEdge(n3, n9)
	e9 =  GraphEdge(n5, n10)

	# e10 = Edge(n8, n11)
	# e11 = Edge(n8, n12)
	# e12 = Edge(n8, n13)

	# e13 = Edge(n4, n14)
	# e14 = Edge(n4, n15)
	# e15 = Edge(n4, n16)

	# e16 = Edge(n16, n17)
	# e17 = Edge(n16, n18)
    #,e10,e11,e12,e13,e14,e15,e16,e17
	return [ e1,e2,e3,e4,e5,e6,e7,e8,e9]

def calculate_coordinates(root):
    childs = list(filter(lambda x: x.start.id == root.id, edges))
    if len(childs) == 0:
        return
    childs = [child.end for child in childs]
    offsets = get_offset(childs, root.x)

    for ix,child in enumerate(childs):
        newChild = child
        newChild.x = offsets[ix] 
        newChild.y = root.y + height * 2
        updated_nodes.append(newChild)
        calculate_coordinates(newChild)

def get_offset(childs, centerX):
    widths = get_childs_width(childs)
    total_sum = sum(widths)
    offsets = []
    if total_sum == 0:
        left = centerX + width/2 - ((len(widths) * 2 - 1) * width) /2
        for ix, child in enumerate(childs):
            left = left + width * 2  if ix!=0 else left 
            offsets.append(left)
    else:
        summary_size = 0
        distance = width * 15 if centerX == startX else width * 2.5
        for ix, size in enumerate(widths):
            summary_size += width * (2 * size - 1) + distance * ix
        current_offset = centerX + width/2 - summary_size/2

        if len(widths) == 0:
            return [0]
        if len(widths) == 1:
            offsets.append(centerX)
        elif len(widths) == 2:
            offsets.append(centerX + width/2 - summary_size/2)
            offsets.append(centerX + summary_size/2)
        elif len(widths) > 2:
            offsets.append(current_offset)
            offsets.append(current_offset+summary_size)
            step = summary_size/(len(widths)-1)
            for ix,size in enumerate(widths):
                if ix == 0 or ix == len(widths)-1:
                    continue
                current_offset += step
                offsets.append(current_offset)
    return offsets

def get_childs_width(childs):
    width = []
    for parent in childs:
        current_id = parent.id
        child_width = 0
        for node in edges:
            if (node.start.id == current_id):
                child_width+=1
        width.append(child_width)
    return width

class GraphEdge:
    def __init__(self,start_node,end_node):
        self.start = start_node
        self.end = end_node

class GraphNode:
    def __init__(self, node_id, description = '', rule = ''):
        self.x = 0
        self.y = 0
        self.id = node_id
        self.description = description
        self.rule = rule