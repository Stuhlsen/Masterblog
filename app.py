import json
import os
from flask import Flask, render_template

app = Flask(__name__)

# Pfad zur JSON-Datei (hier angenommen im gleichen Ordner wie app.py)
DATA_FILE = os.path.join(app.root_path, "data/posts.json")


def load_posts():
    """Load blog posts from the JSON file and return them as a list."""
    with open(DATA_FILE, encoding="utf-8") as file:
        posts = json.load(file)
    return posts


@app.route("/")
def index():
    """Render the homepage with all blog posts."""
    blog_posts = load_posts()
    return render_template("index.html", posts=blog_posts)


if __name__ == "__main__":
    app.run(debug=True)
