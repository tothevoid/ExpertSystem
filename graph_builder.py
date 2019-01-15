from base import Base
from db import Db
from sqlalchemy.sql import select

from characteristic import Characteristic
from muscle_group import MuscleGroup
from node import Node
from exercise import Exercise
from node_rule import NodeRule
from relation import Relation
from rule import Rule

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

class GraphNode:
    def __init__(self, node_id, explanation = '', description = '', rule = ''):
        self.x = 0
        self.y = 0
        self.id = node_id
        self.explanation = explanation
        self.description = description
        self.rule = rule

class GraphEdge:
    def __init__(self, start_node: GraphNode,end_node: GraphNode):
        self.start = start_node
        self.end = end_node    

def getGraphNodeList():
    """Возвращает список узлов"""
    db = Db(Base)
    conn = db.engine.connect()
    s1 = select([Node.id])
    #s1 = select([Node.id, Rule.explanation, Characteristic.name, Rule.operator, Rule.right_operand]).where(NodeRule.node == Node.id).where(Rule.id == NodeRule.rule).where(Characteristic.id == Rule.left_operand)
    nodes = conn.execute(s1)
    graphNodeListFirst = []
    for row in nodes:
        node = GraphNode(row[0])
        graphNodeListFirst.append(node)
        s4 = select([Exercise.description]).where(Node.id == row[0]).where(Exercise.id == Node.excercise)
        descr = conn.execute(s4).first()
        if descr != None:
            node.description = descr[0]
        ruleNodes = conn.execute(s4)
        s2 = select([NodeRule]).where(NodeRule.node == row[0])
        ruleNodes = conn.execute(s2)
        for ruleNode in ruleNodes:
            s3 = select([Rule.explanation, Characteristic.name, Rule.operator, Rule.right_operand]).where(Rule.id == ruleNode.rule).where(Characteristic.id == Rule.left_operand)
            rule = conn.execute(s3).first()
            if node.explanation == "":
                node.explanation = rule[0]
                node.rule = "{0} {1} {2}".format(rule[1], rule[2], rule[3])
            else:
                node.explanation += "\n"+ rule[0]             
                node.rule += "\n"+ "{0} {1} {2}".format(rule[1], rule[2], rule[3])
    return graphNodeListFirst

def getGraphEdgeList(graphNodeList):
    db = Db(Base)
    conn = db.engine.connect()
    s1 = select([Relation.parent, Relation.child])
    nodes = conn.execute(s1)
    graphEdgeListResult = []
    for row in nodes:
        parentNode = None
        childNode = None
        for node in graphNodeList:
            if node.id == row['parent']:
                parentNode = node
            if node.id == row['child']:
                childNode = node
            if parentNode != None and childNode != None:
                break
        graphEdgeListResult.append(GraphEdge(parentNode,childNode))
    return graphEdgeListResult
   
def get_graph(isSample = True):
    global edges
    root = GraphNode(1)
    root.x = startX
    root.y = startY
    if isSample:
        edges = get_sample(root)
    else:
        nodes = getGraphNodeList()
        edges = getGraphEdgeList(nodes)
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

    e1 =  GraphEdge(root, n2)
    e2 =  GraphEdge(root, n3)
    e3 =  GraphEdge(n2, n6)
    e4 =  GraphEdge(n2, n7)
    e5 =  GraphEdge(n3, n4)
    e6 =  GraphEdge(n3, n5)
    e7 =  GraphEdge(n3, n8)
    e8 =  GraphEdge(n3, n9)
    e9 =  GraphEdge(n5, n10)

    edgeList = [e1,e2,e3,e4,e5,e6,e7,e8,e9]
    return edgeList

def calculate_coordinates(root):
    if root == None:
        return
    childs = []
    for elm in edges:
       if  elm.start != None and elm.start.id == root.id:
            childs.append(elm)
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