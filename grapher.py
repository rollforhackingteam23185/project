from bokeh.plotting import figure, output_file, show

die_data = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}

x = list(die_data.keys())
y = list(die_data.values())

print(x)
print(y)

graph = figure()
graph.hbar_stack(x, y)

output_file("dice_graph.html")

show(graph)
