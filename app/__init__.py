import os
from flask import Flask, render_template
from flask_cors import CORS

from app.youtube import youtube_bp


def create_app():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    app = Flask(
        __name__,
        template_folder=os.path.join(base_dir, "templates")
    )

    CORS(app)

    app.register_blueprint(
        youtube_bp,
        url_prefix="/youtube"
    )

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/health")
    def health():
        return {
            "success": True,
            "message": "Nova AI is running"
        }

    return app


app = create_app()
