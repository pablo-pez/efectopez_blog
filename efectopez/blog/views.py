import requests.exceptions
from flask import Blueprint, render_template

from efectopez.utils.database import get_db_connection
from efectopez.utils.md_reader import markdown_to_html

blog = Blueprint(
    "blog",
    __name__,
    url_prefix="/blog",
    template_folder="templates/blog/",
    static_folder="static"
)


@blog.route('')
@blog.route('/')
def get_directory():
    # return "Blog directory"
    conn = get_db_connection()
    context = {
        "posts": conn.execute('SELECT * FROM posts').fetchall()
    }
    conn.close()
    return render_template("post_directory.html", **context)


@blog.route('/<postname>')
def get_post(postname: str):
    try:
        html, meta = markdown_to_html(f'blog_content/{postname}/content.md')
        context = {
            "post_title": meta['title'][0],
            "post_author": meta['authors'][0],
            "post_date": meta['date'][0],
            "post_content": html
        }
        return render_template("post.html", **context)
    except requests.exceptions.HTTPError:
        return render_template("404.html"), 404
