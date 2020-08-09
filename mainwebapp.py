from flask import Flask, render_template, request
import diceparser
import grapher

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


@app.route('/', methods=["POST"])
def home():
    if request.method == "POST":
        equation = request.form["formula"]
        tokens = process_input(equation)
        values_dict = diceparser.parse(tokens)
        grapher.graph_eq(values_dict)

    return render_template("index.html")

@app.route('/graph')
def graph():
    return render_template("dice_graph.html")


if __name__ == '__main__':
    app.run(debug=True)
