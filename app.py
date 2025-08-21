import os
from flask import Flask
from flask_smorest import Api  # or use 'from flask_restful import Api' if you use Flask-RESTful
from resources import fibs as FibsBluePrint

from dotenv import load_dotenv

def create_app():
  app = Flask(__name__)

  @app.route("/ping")
  def hello():
      return {"message": "pong"}

  load_dotenv()

  app.config["PROPAGATE_EXCEPTIONS"] = True
  app.config["API_TITLE"] = os.getenv("API_TITLE", "Fibonacci REST API")
  app.config["API_VERSION"] = "v1"
  app.config["OPENAPI_VERSION"] = "3.0.3"
  app.config["OPENAPI_URL_PREFIX"] = "/"

  api = Api(app)

  api.register_blueprint(FibsBluePrint)

  return app
