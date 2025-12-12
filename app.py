import json
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

DATA_FILE = os.path.join(app.root_path, "data/posts.json")


def load_posts():
    """Load blog posts from the JSON file and return them as a list."""
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, encoding="utf-8") as file:
        return json.load(file)


def save_posts(posts):
    """Save the given list of posts back to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(posts, file, ensure_ascii=False, indent=4)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        author = request.form.get("author", "").strip()
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()

        posts = load_posts()

        if posts:
            new_id = max(post["id"] for post in posts) + 1
        else:
            new_id = 1

        new_post = {
            "id": new_id,
            "author": author,
            "title": title,
            "content": content,
        }

        posts.append(new_post)
        save_posts(posts)

        return redirect(url_for("index"))

    # GET: Formular anzeigen
    return render_template("add.html")



@app.route("/", methods=["GET"])
def index():
    blog_posts = load_posts()  # so wie du es schon hast
    return render_template("index.html", posts=blog_posts)



if __name__ == "__main__":
    app.run(debug=True)
