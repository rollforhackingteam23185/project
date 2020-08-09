from flask import Flask, render_template, request
import diceparser

def process_input(string):
    user = string

    indexnum = 0
    tokens = []

    user = user.replace(" ", "")
    print(user)

    for i in range(len(user)):
        if user[i].isdigit():
            continue
        else:
            tokens.append(user[indexnum:i])
            tokens.append(user[i])
            indexnum = i+1
            print(user[i])
            print(indexnum)
            print(tokens)
    tokens.append(user[indexnum:])
    return tokens


app = Flask(__name__)

values_dict = {}


@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == "POST":
        global values_dict
        equation = request.form["formula"]
        tokens = process_input(equation)
        values_dict = diceparser.parse(tokens)

    return render_template("index.html")


@app.route('/graph', methods=["POST", "GET"])
def graph():
    from bokeh.plotting import figure, output_file, show
    from bokeh.embed import components
    from bokeh.resources import CDN

    die_data = values_dict

    x = list(die_data.keys())
    for i in range(len(x)):
        x[i] = int(x[i])
    y = list(die_data.values())

    print(x)
    print(y)

    graph = figure()
    graph.vbar(x=x, width=0.5, bottom=0, top=y, color="firebrick")

    script1, div1 = components(graph)
    cdn_js = CDN.js_files[0]

    return render_template("dice_graph.html", script1=script1, div1=div1, cdn_js=cdn_js)


if __name__ == '__main__':
    app.run(debug=True)
