from bokeh.plotting import figure, output_file, show

def graph_eq(data):
    die_data = {'6': 1, '7': 6, '8': 21, '9': 56, '10': 126, '11': 252, '12': 456, '13': 756, '14': 1161, '15': 1666, '16': 2247, '17': 2856, '18': 3431, '19': 3906, '20': 4221, '21': 4332, '22': 4221, '23': 3906, '24': 3431, '25': 2856, '26': 2247, '27': 1666, '28': 1161, '29': 756, '30': 456, '31': 252, '32': 126, '33': 56, '34': 21, '35': 6, '36': 1}


    x = list(die_data.keys())
    for i in range(len(x)):
        x[i] = int(x[i])
    y = list(die_data.values())

    print(x)
    print(y)

    graph = figure()
    graph.vbar(x=x, width=0.5, bottom=0, top=y, color="firebrick")

    output_file("dice_graph.html")

    show(graph)
