"""
Main entry point for the Math Microservice
This file starts the Flask application
"""

from app import create_app

# Create the Flask application instance
app = create_app()

if __name__ == '__main__':
    # Run the application in development mode
    # debug=True means the server will reload when you change code
    print("🚀 Starting Math Microservice...")
    print("📊 Available at: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)