from flask import Flask
from views import views

# def create_app():
#     application = Flask(__name__)
#     # application.config['SECRET_KEY'] = "helloworld"

#     from views import views

#     # application.register_blueprint(views, url_prefix="/")

#     return application

# # if __name__ == "__main__":
# application = create_app()
# application.run() #debug=True)

# application = Flask(__name__)


application = Flask(__name__)
# application.config['SECRET_KEY'] = "helloworld"
# application.register_blueprint(views, url_prefix="/")
# application.run(debug=True)


@application.route('/')
def hello_world():
    return 'Hola Mundo'