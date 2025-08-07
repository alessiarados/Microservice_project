**Math Microservice API**

A production-ready microservice that provides mathematical calculation APIs with persistent storage, interactive documentation, and comprehensive monitoring capabilities.

Features:

Mathematical Operations: Power, Fibonacci, and Factorial calculations

RESTful API: Clean, well-documented REST endpoints

Interactive Documentation: Swagger UI for easy API exploration

Data Persistence: SQLite database for storing all calculations

Data Validation: Pydantic models for robust input validation

Performance Monitoring: Execution time tracking for all operations

Error Handling: Comprehensive error responses with proper HTTP status codes

Calculation History: View and analyze previous calculations

Usage Statistics: API usage metrics and analytics

Production Ready: Following microservices best practices

**Architecture**

The service follows a clean MVC (Model-View-Controller) pattern:
app/
├── __init__.py          # Flask application factory
├── models.py            # Pydantic models for data validation
├── views.py             # API endpoints and Swagger documentation
├── controllers.py       # Business logic for mathematical operations
└── database.py          # Database operations and management


**Key Components**

Models: Pydantic models ensure type safety and validation

Views: Flask-RESTX resources with automatic OpenAPI documentation

Controllers: Pure business logic separated from web layer

Database: SQLite with proper connection management and error handling

**Requirements**

Python 3.8+
Flask 2.3.3+
See requirements.txt for full dependencies

**Installation & Setup**

Clone the repository
bashgit clone <repository-url>
cd math-microservice

Create virtual environment
bashpython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies
bashpip install -r requirements.txt

Start the service
bashpython main.py

The service will start on http://localhost:5000

**API Documentation**

Interactive Documentation
Visit http://localhost:5000/ to access the Swagger UI with interactive API documentation.

**Data Validation & Limits**

Input Constraints

Power: Base and exponent ≤ 10,000 (absolute value)
Fibonacci: n must be 0-1,000
Factorial: n must be 0-100

Error Handling
The API provides detailed error messages for:

Invalid input formats
Out-of-range values
Server errors
Missing parameters

**API Standards**

REST: Follows RESTful principles
JSON: All requests/responses in JSON format
HTTP Status Codes: Proper status codes for all responses
OpenAPI 3.0: Full Swagger documentation
Semantic Versioning: API versioning support

**Current Implementation**

Input validation and sanitization
Error message sanitization
SQL injection prevention



