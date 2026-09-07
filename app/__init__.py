from flask import Flask, render_templates
from flask_cors import CORS

from app.youtube import youtube_bp


def create_app():
    app = Flask(
        __name__,
        template_folder="../templates"
    )

    CORS(app)

    app.register_blueprint(
        youtube_bp,
        url_prefix="/youtube"
    )

    @app.route("/")
    def home():
        return render_templates("index.html")

    @app.route("/health")
    def health():
        return {
            "success": True,
            "message": "Nova AI is running"
        }

    return app


app = create_app()
