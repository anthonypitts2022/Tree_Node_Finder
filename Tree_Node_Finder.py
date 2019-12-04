#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 19:18:03 2019

@author: Anthony Pitts, anthony.pitts@columbia.edu

Description: Searches a tree for a specfified node name

"""

class Node:
    
    #name of Node
    Name = None
    
    #list of all child nodes
    Children = []
    
    def __init__(self, name = "", children = []):
        #initialize the name and children values
        self.Name = name
        self.Children = children
        
    def get_name(self):
        return self.Name;
    
    def set_name(self, new_name):
        self.Name = new_name
        return self.Name
    
    def get_children(self):
        return self.Children;
    
    def set_children(self, new_children):
        self.Children = new_children
        return self.Children
    
    
def main():
    
    #create nodes
    Start = Node("Start")
    A1 = Node("A1")
    D1 = Node("D1")
    E1 = Node("E1")
    A2 = Node("A2")
    B1 = Node("B1")
    Find_Me = Node("FindMe")
    B2 = Node("B2")
    C1 = Node("C1")   
    
    #add the children lists to each node
    Start.set_children([A1, A2])
    A1.set_children([D1])
    D1.set_children([E1])
    A2.set_children([B1, B2])
    B1.set_children([Find_Me])
    B2.set_children([C1])
    
    #find the specified node in the tree
    found = find_node(Start, "FindMe")
    if(not found):
        print("This node is not in the tree.")
    
  
#recursive method for traversing the tree
#returns boolean of whether or not node was found
def find_node(node, target_name):
    node_name = node.get_name()
    
    #print current node
    print(node_name)
    
    #if this node is target node
    if(node_name == target_name):
        return True
    
    #iterate through each child node
    for child in node.get_children():
        #if node was found, return True and stop searching
        if(find_node(child, target_name)):
            return True
        
    return False
    

if __name__ == "__main__":
    main()
    
