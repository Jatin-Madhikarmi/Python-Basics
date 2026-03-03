# import graphviz

# # Create a Digraph object (for a directed graph)
# dot = graphviz.Digraph(comment='The Round Table')

# # Add nodes
# dot.node('A', 'King Arthur')
# dot.node('B', 'Sir Bedevere the Wise')
# dot.node('L', 'Sir Lancelot the Brave')

# # Add edges
# dot.edge('A', 'B', 'man-at-arms')
# dot.edge('B', 'L', 'knight')
# dot.edge('L', 'A', 'king')

# # Render the graph and open it for viewing
# dot.render('round-table.gv', view=True)


from graphviz import Digraph

g = Digraph('G')
g.attr(rankdir='LR') # Left-to-Right layout

# Adding nodes with specific styling
g.node('c1', 'Commit 1', color='lightblue2', style='filled')
g.node('c2', 'Commit 2', color='lightblue2', style='filled')
g.node('f1', 'Feature 1', color='gold', style='filled')

# Bulk adding edges
g.edges([('c1', 'c2'), ('c2', 'f1')])

print(g.source) # This prints the DOT code you were writing manually!