---
weight: 3
bookFlatSection: false
title: "Chapter 3"
description: "Structure of networks"
---

# Chapter 3: Structure of networks

1.  The ______ centrality of a node N1, is the reciprocal of the sum of the shortest distances between N1 and all other nodes.  
a.  Closeness  
b.  Betweenness  
c.  Degree  
d.  None of the above  
**Ans: a**

2.  What is the command for finding the degrees of each node in the network, A is the adjacency matrix?  
a.  `degrees = sum(A)`  
b.  `degrees = nnz(A)`  
c.  `degrees = nonzeros(A)`  
d.  None.  
**Ans: a**

3.  A complex biological graph is typically unaffected by random perturbations because…  
a.  Random perturbations cancel each other.  
b.  Random perturbations always attack peripheral nodes.  
c.  Random perturbations rarely affect essential nodes in a scale-free network.  
d.  There is no exact reason.  
**Ans: c**

4.  Pick the best suitable reason.  
A complete undirected graph has zero network motifs because… (more than one reason might be true)  
a.  Undirected graphs do not have motifs.  
b.  A complete graph is too sparse to have motifs.  
c.  Every node is connected to one another, and hence no rewiring is possible.  
d.  None of the motifs are statistically significant.  
**Ans: c, d**

5.  In a neural network from the brain to ear, all signals from the brain to ear and vice versa should pass through a neuron X. What would this mean?  
a.  X will have the highest clustering coefficient.  
b.  X is the highest degree node in the neural network.  
c.  X will have the highest betweenness centrality.  
d.  All the above is true.  
**Ans: c**

6.  We know that a network model of a biological system helps us to understand the system. But how is rewiring the network helpful? More than one statement might be true.  
a.  It helps us to distinguish our network from random networks that can be arrived at by chance.  
b.  The rewired network should show the same properties as the original network. Only then our network is correct.  
c.  Rewiring is done to study the stability of the network.  
d.  It helps us to study the statistical significance of our network parameters.  
**Ans: a, d**

7.  The information about a network is attached as a [text file](bio-diseasome.mtx), which can be uploaded into MATLAB using the command `readmatrix(filename, 'FileType', 'text')`.  
Answer the following based on this network.   
i)  What is the maximum degree of a node in this network?  
**Ans: 50**  
ii) How many nodes have a degree of 26?  
**Ans: 2**  
iii)    How many nodes have all their neighboring nodes interacting with one another?  
**Ans: 266**  
iv) What is the characteristic pathlength of this network? Round off to two decimal points.  
**Ans: 6.50 to 6.51**

8.  Which of the following gene networks are directed graphs?  
a.  Gene-regulatory networks  
b.  Co-expression networks  
c.  Gene interaction networks  
d.  Transcriptional regulatory networks  
e.  Gene expression network  
**Ans: a, d**

9.  Construct a regular lattice in MATLAB with 100 nodes and each node having 10 neighbors. What is the characteristic pathlength of the network? Round off the answer to 2 decimal points.  
**Ans: 5.4 to 5.5**

10.  Randomly remove 120 nodes from the regular lattice in **Question 9**. What will be the mean clustering coefficient of the network? Round off the answer to 2 decimal points.  
**Ans: 0.3 to 0.44**

11.  If a network has metabolites and reactions as nodes, with edges between metabolites and reactions, reactions and metabolites it is a _________.  
a.  Substrate graph  
b.  Hypergraph  
c.  Bipartite graph  
d.  Reaction graph  
**Ans: c**