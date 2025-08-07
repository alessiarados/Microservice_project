""Math Microservice API""
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

🏗️ Architecture
The service follows a clean MVC (Model-View-Controller) pattern:
app/
├── __init__.py          # Flask application factory
├── models.py            # Pydantic models for data validation
├── views.py             # API endpoints and Swagger documentation
├── controllers.py       # Business logic for mathematical operations
└── database.py          # Database operations and management
Key Components

Models: Pydantic models ensure type safety and validation
Views: Flask-RESTX resources with automatic OpenAPI documentation
Controllers: Pure business logic separated from web layer
Database: SQLite with proper connection management and error handling

📋 Requirements

Python 3.8+
Flask 2.3.3+
See requirements.txt for full dependencies

🛠️ Installation & Setup

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
📖 API Documentation
Interactive Documentation
Visit http://localhost:5000/ to access the Swagger UI with interactive API documentation.
Available Endpoints
Mathematical Operations
MethodEndpointDescriptionPOST/api/v1/powerCalculate base^exponentPOST/api/v1/fibonacciGet nth Fibonacci numberPOST/api/v1/factorialCalculate n! factorial
Monitoring & Analytics
MethodEndpointDescriptionGET/api/v1/healthHealth checkGET/api/v1/historyGet calculation historyGET/api/v1/statsGet usage statistics
Request/Response Examples
Power Calculation
bashcurl -X POST http://localhost:5000/api/v1/power \
  -H "Content-Type: application/json" \
  -d '{"base": 2, "exponent": 3}'
Response:
json{
  "operation": "power",
  "input_data": {"base": 2, "exponent": 3},
  "result": 8.0,
  "timestamp": "2025-01-15T10:30:00",
  "execution_time_ms": 0.12
}
Fibonacci Calculation
bashcurl -X POST http://localhost:5000/api/v1/fibonacci \
  -H "Content-Type: application/json" \
  -d '{"n": 10}'
Response:
json{
  "operation": "fibonacci",
  "input_data": {"n": 10},
  "result": 55,
  "timestamp": "2025-01-15T10:30:00",
  "execution_time_ms": 0.05
}
Factorial Calculation
bashcurl -X POST http://localhost:5000/api/v1/factorial \
  -H "Content-Type: application/json" \
  -d '{"n": 5}'
Response:
json{
  "operation": "factorial",
  "input_data": {"n": 5},
  "result": 120,
  "timestamp": "2025-01-15T10:30:00",
  "execution_time_ms": 0.03
}
🧪 Testing
Run the comprehensive test suite:
bash# Start the service first
python main.py

# In another terminal, run tests
python test_api.py
The test script will:

✅ Test all mathematical operations
✅ Validate error handling
✅ Check database persistence
✅ Verify statistics endpoints
✅ Test health monitoring

📊 Data Validation & Limits
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
