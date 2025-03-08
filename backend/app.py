from flask import Flask
import dotenv

from backend.config import config
from backend.routes import license_routes


dotenv.load_dotenv()


def create_app(config_name="default"):
    flask_app = Flask(__name__)

    flask_app.config.from_object(config.config_mapper[config_name])
    flask_app.register_blueprint(license_routes.licenses)

    return flask_app


if __name__ == '__main__':
    app = create_app()
    app.run()
