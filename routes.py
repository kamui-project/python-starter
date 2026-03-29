from flask import render_template, request, redirect, url_for

from extensions import db
from models import Greeting


def register_routes(app):

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/greetings", methods=["GET", "POST"])
    def greetings():
        if request.method == "POST":
            message = request.form.get("message", "").strip()
            if message:
                greeting = Greeting(message=message)
                db.session.add(greeting)
                db.session.commit()
            return redirect(url_for("greetings"))

        all_greetings = Greeting.query.order_by(Greeting.created_at.desc()).all()
        return render_template("greetings.html", greetings=all_greetings)

    @app.route("/health")
    def health():
        return {"status": "ok"}
