from flask import Flask, render_template, request
from model import get_top_k_documents

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    query = request.form["query"]
    top_docs = get_top_k_documents(query)
    return render_template("index.html", results=top_docs)

if __name__ == "__main__":
    app.run(debug=True)
