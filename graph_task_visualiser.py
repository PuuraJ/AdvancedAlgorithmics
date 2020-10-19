VERTICES = """0 652 396
1 742 479
2 502 536
3 462 411
4 896 298
5 617 198
6 756 212
7 539 372
8 660 603
9 372 671
10 769 267
11 478 222
12 390 272
13 616 548
14 615 893
15 763 821
16 739 40
17 950 450
18 701 867
19 753 592
20 451 893
21 921 390
22 279 843
23 222 756
24 127 469
25 84 582
26 496 950
27 260 626
28 315 605
29 351 862
30 764 691
31 402 536
32 542 744
33 495 729"""

EDGES = """0 1
0 2
0 3
0 4
0 5
0 6
0 7
0 8
0 10
0 11
0 12
0 13
0 17
0 19
0 21
0 31
1 2
1 3
1 7
1 13
1 17
1 19
1 21
1 30
2 3
2 7
2 8
2 9
2 13
2 27
2 28
2 32
3 7
3 12
3 13
4 6
4 10
5 6
5 10
5 16
6 16
8 30
8 32
8 33
9 33
13 33
14 32
14 33
15 32
15 33
18 32
18 33
19 33
20 32
20 33
22 32
22 33
23 25
23 27
23 29
23 32
23 33
24 25
24 27
24 31
25 31
26 29
26 33
27 33
28 31
28 33
29 32
29 33
30 32
30 33
31 32
31 33
32 33"""


# Create a list of vertices data [[0, 652, 396], [1, 742, 479], ...]
vertices = [list(map(int, vertex_data.split())) for vertex_data in VERTICES.split("\n")]
# Create a list of edges [[0, 1], [0, 4], ...]
edges = [list(map(int, edge.split())) for edge in EDGES.split("\n")]

### Drawing parameters ###
# Edge width and color
edge_width = 1
edge_color = "blue"

# Node radius and color
node_radius = 15
node_color = "black"

# Text size and color
text_color = "orange"
text_size = 18

# Traversal text size and color
trav_color = "darkred"
trav_size = 18

# Create edges input for tool
for edge in edges:
    print(f"line {vertices[edge[0]][1]} {vertices[edge[0]][2]}"\
         f" {vertices[edge[1]][1]} {vertices[edge[1]][2]} {edge_width} {edge_color}")

# Create vertices input for tool
for vertex in vertices:
    print(f"circle {vertex[1]} {vertex[2]} {node_radius} {node_color}")

# Add text on top of vertices
for vertex in vertices:
    print(f'text "{vertex[0]}" {vertex[1]-8} {vertex[2]+8} {text_size} {text_color}')

# Add order of traversal, currently random order!
traversal_order = [31, 11, 16, 28, 5, 0, 30, 27, 20, 13, 6, 24, 9, 26, 33, 21, 29, 22, 18, 
                    8, 7, 14, 25, 4, 10, 17, 23, 2, 15, 19, 3, 12, 1, 32]

# i is the order #, k is the vertex id.
for i, k in enumerate(traversal_order):
    print(f'text "{i}" {vertices[k][1]+18} {vertices[k][2]+8} {trav_size} {trav_color}')

