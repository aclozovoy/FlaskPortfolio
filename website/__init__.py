from flask import Flask

def create_app():
    application = Flask(__name__)
    application.config['SECRET_KEY'] = "helloworld"

    from .views import views

    application.register_blueprint(views, url_prefix="/")


    return application