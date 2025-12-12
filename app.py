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
    """Display the add-post form or handle the submission of a new post."""
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

    return render_template("add.html")


@app.route("/delete/<int:post_id>")
def delete(post_id):
    """Delete a blog post by its ID and redirect back to the homepage."""
    posts = load_posts()
    updated_posts = [post for post in posts if post["id"] != post_id]

    if len(updated_posts) != len(posts):
        save_posts(updated_posts)

    return redirect(url_for("index"))

@app.route("/update/<int:post_id>", methods=["GET", "POST"])
def update(post_id):
    """Display a form to update a post or handle the submitted changes."""
    posts = load_posts()
    post_index = None
    post = None

    # Find the post with this ID
    for index, item in enumerate(posts):
        if item["id"] == post_id:
            post_index = index
            post = item
            break

    if post is None:
        return "Post not found", 404

    if request.method == "POST":
        # Read updated data from the form
        author = request.form.get("author", "").strip()
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()

        if not author or not title or not content:
            error_message = "All fields are required."
            return render_template(
                "update.html",
                post=post,
                error=error_message,
            )

        # Update the post in the list
        posts[post_index]["author"] = author
        posts[post_index]["title"] = title
        posts[post_index]["content"] = content

        # Save all posts back to JSON
        save_posts(posts)

        # Redirect to home after successful update
        return redirect(url_for("index"))

    # GET request → show the form with the current data
    return render_template("update.html", post=post)



@app.route("/", methods=["GET"])
def index():
    """Render the homepage and show all blog posts."""
    blog_posts = load_posts()
    return render_template("index.html", posts=blog_posts)


if __name__ == "__main__":
    app.run(debug=True)
