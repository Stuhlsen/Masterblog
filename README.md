# Masterblog

A small learning project: a minimal blog application built with Flask.  
Blog posts are stored in a JSON file on disk and can be created, edited and deleted via a simple web interface.

---

## Features

- List all blog posts on the home page
- Create new posts via a form (`/add`)
- Edit existing posts (`/update/<id>`)
- Delete posts (`/delete/<id>`)
- Posts are persisted in a JSON file (`data/posts.json`)
- Simple HTML/CSS frontend using Flask templates

---

## Tech Stack

- Python 3.13+ (works with any modern Python 3)
- [Flask](https://flask.palletsprojects.com/)
- HTML & CSS (Jinja2 templates)
- JSON file as lightweight data store

---
