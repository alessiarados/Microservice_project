"""
Flask application factory with Swagger UI
This creates and configures the Flask app with interactive API documentation
"""

from flask import Flask
from flask_restx import Api


def create_app():
    """
    Create and configure the Flask application with Swagger UI

    Returns:
        Flask: Configured Flask application instance
    """
    # Create Flask application instance
    app = Flask(__name__)

    # Basic configuration
    app.config['DEBUG'] = True
    app.config['TESTING'] = False

    # Create API instance with Swagger documentation
    api = Api(
        app,
        version='1.0.0',
        title='Math Microservice API',
        description='A microservice for mathematical calculations',
        doc='/',  # Swagger UI will be available at the root URL
    )

    # Register namespaces (equivalent to blueprints in flask-restx)
    from app.views import math_ns
    api.add_namespace(math_ns, path='/api/v1')

    return app