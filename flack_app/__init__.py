# from docx import Document
from flask import Flask, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

# from routes import input_profession_page

db = SQLAlchemy()


def start_app():
    app = Flask(__name__, instance_relative_config=False)

    app.secret_key = "ylkv0bCqPliokdenmvtcTtx19gVnGBsL"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://sea_team:123456@localhost:5432/sea_db.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        from . import routes  # Import routes
        db.create_all()  # Create database tables for our data models

        return app
    # app.run(debug=True)


#
# @app.route("/")
# def render_main_page():
#     return redirect(url_for('input_profession'))


if __name__ == '__main__':
    start_app()
