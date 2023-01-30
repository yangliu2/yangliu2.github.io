from flask import Flask, render_template, request
from neo4j import GraphDatabase

app = Flask(__name__, static_folder='public')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/nodes", methods=["POST"])
def get_nodes():
    username = request.form["username"]
    password = request.form["password"]
    driver_url = request.form["driver_url"]
    driver = GraphDatabase.driver(driver_url, auth=(username, password))
    with driver.session() as session:
        result = session.run("MATCH (n) RETURN n")
        nodes = []
        for record in result:
            node = record["n"]
            nodes.append(node)
    return render_template("nodes.html", nodes=nodes)

if __name__ == "__main__":
    app.run()
