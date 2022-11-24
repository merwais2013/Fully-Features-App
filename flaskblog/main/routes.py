from flask import Blueprint, request, render_template
from flaskblog.models import Post

main = Blueprint('main', __name__)


@main.route("/")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=2, page=page)
    return render_template("index.html", posts=posts)


@main.route("/about", methods=['GET', 'POST'])
def about():
    return render_template("about.html")

