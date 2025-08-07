"""
Views - API endpoints with Swagger documentation
This file defines the URLs and how to handle requests with interactive documentation
"""

from flask import request
from flask_restx import Namespace, Resource, fields
from pydantic import ValidationError
import time

from app.models import (
    PowerRequest, FibonacciRequest, FactorialRequest,
    MathResponse, ErrorResponse
)
from app.controllers import math_controller
from app.database import db_manager

# Create a Namespace (like Blueprint but for flask-restx)
math_ns = Namespace('math', description='Mathematical operations')

# Define Swagger models for documentation
power_input_model = math_ns.model('PowerInput', {
    'base': fields.Float(required=True, description='The base number', example=2.0),
    'exponent': fields.Float(required=True, description='The exponent number', example=3.0)
})

fibonacci_input_model = math_ns.model('FibonacciInput', {
    'n': fields.Integer(required=True, description='Position in Fibonacci sequence (0-1000)', example=10)
})

factorial_input_model = math_ns.model('FactorialInput', {
    'n': fields.Integer(required=True, description='Number for factorial calculation (0-100)', example=5)
})

math_response_model = math_ns.model('MathResponse', {
    'operation': fields.String(description='Type of operation performed'),
    'input_data': fields.Raw(description='The input parameters'),
    'result': fields.Raw(description='The calculation result'),
    'timestamp': fields.String(description='When the calculation was performed'),
    'execution_time_ms': fields.Float(description='How long the calculation took in milliseconds')
})

error_response_model = math_ns.model('ErrorResponse', {
    'error': fields.String(description='Error message'),
    'operation': fields.String(description='Operation that failed'),
    'timestamp': fields.String(description='When the error occurred'),
    'status_code': fields.Integer(description='HTTP status code')
})


def create_error_response(error_msg: str, operation: str, status_code: int = 400):
    """
    Helper function to create consistent error responses

    Args:
        error_msg: The error message
        operation: Which operation failed
        status_code: HTTP status code to return
    """
    error_response = ErrorResponse(
        error=error_msg,
        operation=operation,
        status_code=status_code
    )
    return error_response.model_dump(), status_code


@math_ns.route('/power')
class PowerCalculation(Resource):
    @math_ns.doc('calculate_power')
    @math_ns.expect(power_input_model)
    def post(self):
        """
        Calculate base raised to the power of exponent (base^exponent)

        Returns the result of base^exponent calculation.
        """
        start_time = time.time()

        try:
            # Get JSON data from request
            data = request.get_json()
            print(f"🔍 DEBUG: Received data: {data}")

            if not data:
                return create_error_response("No JSON data provided", "power", 400)

            # Validate input using Pydantic
            print(f"🔍 DEBUG: Creating PowerRequest...")
            power_request = PowerRequest(**data)
            print(f"🔍 DEBUG: PowerRequest created successfully: base={power_request.base}, exponent={power_request.exponent}")

            # Perform calculation
            print(f"🔍 DEBUG: Calling math_controller.calculate_power...")
            result = math_controller.calculate_power(
                power_request.base,
                power_request.exponent
            )
            print(f"🔍 DEBUG: Calculation result: {result}")

            # Calculate execution time
            execution_time = (time.time() - start_time) * 1000
            print(f"🔍 DEBUG: Execution time: {execution_time}ms")

            # Save to database
            print(f"🔍 DEBUG: Saving to database...")
            db_manager.save_calculation(
                operation="power",
                input_data={"base": power_request.base, "exponent": power_request.exponent},
                result=result,
                execution_time_ms=round(execution_time, 2)
            )

            # Create response using Pydantic
            print(f"🔍 DEBUG: Creating MathResponse...")
            response = MathResponse(
                operation="power",
                input_data={"base": power_request.base, "exponent": power_request.exponent},
                result=result,
                execution_time_ms=round(execution_time, 2)
            )
            print(f"🔍 DEBUG: MathResponse created: {response.model_dump()}")

            return response.model_dump(), 200

        except ValidationError as e:
            return create_error_response(f"Invalid input: {str(e)}", "power", 400)
        except ValueError as e:
            return create_error_response(str(e), "power", 400)
        except Exception as e:
            return create_error_response(f"Internal error: {str(e)}", "power", 500)


@math_ns.route('/fibonacci')
class FibonacciCalculation(Resource):
    @math_ns.doc('calculate_fibonacci')
    @math_ns.expect(fibonacci_input_model)
    def post(self):
        """
        Calculate the nth Fibonacci number

        Returns the nth number in the Fibonacci sequence (0, 1, 1, 2, 3, 5, 8, 13, ...).
        """
        start_time = time.time()

        try:
            data = request.get_json()

            if not data:
                return create_error_response("No JSON data provided", "fibonacci", 400)

            # Validate input using Pydantic
            fib_request = FibonacciRequest(**data)

            # Perform calculation
            result = math_controller.calculate_fibonacci(fib_request.n)

            # Calculate execution time
            execution_time = (time.time() - start_time) * 1000

            # Save to database
            db_manager.save_calculation(
                operation="fibonacci",
                input_data={"n": fib_request.n},
                result=result,
                execution_time_ms=round(execution_time, 2)
            )

            # Create response using Pydantic
            response = MathResponse(
                operation="fibonacci",
                input_data={"n": fib_request.n},
                result=result,
                execution_time_ms=round(execution_time, 2)
            )

            return response.model_dump(), 200

        except ValidationError as e:
            return create_error_response(f"Invalid input: {str(e)}", "fibonacci", 400)
        except ValueError as e:
            return create_error_response(str(e), "fibonacci", 400)
        except Exception as e:
            return create_error_response(f"Internal error: {str(e)}", "fibonacci", 500)


@math_ns.route('/factorial')
class FactorialCalculation(Resource):
    @math_ns.doc('calculate_factorial')
    @math_ns.expect(factorial_input_model)
    def post(self):
        """
        Calculate the factorial of n (n!)

        Returns n! = n × (n-1) × (n-2) × ... × 1
        """
        start_time = time.time()

        try:
            data = request.get_json()

            if not data:
                return create_error_response("No JSON data provided", "factorial", 400)

            # Validate input using Pydantic
            factorial_request = FactorialRequest(**data)

            # Perform calculation
            result = math_controller.calculate_factorial(factorial_request.n)

            # Calculate execution time
            execution_time = (time.time() - start_time) * 1000

            # Save to database
            db_manager.save_calculation(
                operation="factorial",
                input_data={"n": factorial_request.n},
                result=result,
                execution_time_ms=round(execution_time, 2)
            )

            # Create response using Pydantic
            response = MathResponse(
                operation="factorial",
                input_data={"n": factorial_request.n},
                result=result,
                execution_time_ms=round(execution_time, 2)
            )

            return response.model_dump(), 200

        except ValidationError as e:
            return create_error_response(f"Invalid input: {str(e)}", "factorial", 400)
        except ValueError as e:
            return create_error_response(str(e), "factorial", 400)
        except Exception as e:
            return create_error_response(f"Internal error: {str(e)}", "factorial", 500)


@math_ns.route('/health')
class HealthCheck(Resource):
    @math_ns.doc('health_check')
    def get(self):
        """
        Health check endpoint

        Returns the current status of the API service.
        """
        return {
            "status": "healthy",
            "api_version": "v1",
            "available_endpoints": [
                "POST /api/v1/power",
                "POST /api/v1/fibonacci",
                "POST /api/v1/factorial",
                "GET /api/v1/history",
                "GET /api/v1/stats"
            ]
        }, 200


@math_ns.route('/history')
class CalculationHistory(Resource):
    @math_ns.doc('get_calculation_history')
    def get(self):
        """
        Get calculation history

        Returns a list of all previous calculations stored in the database.
        """
        try:
            history = db_manager.get_calculation_history(limit=50)
            return {
                "total_records": len(history),
                "calculations": history
            }, 200
        except Exception as e:
            return {"error": f"Failed to retrieve history: {str(e)}"}, 500


@math_ns.route('/stats')
class CalculationStats(Resource):
    @math_ns.doc('get_calculation_stats')
    def get(self):
        """
        Get API usage statistics

        Returns statistics about API usage including total calculations and performance metrics.
        """
        try:
            stats = db_manager.get_operation_stats()
            return stats, 200
        except Exception as e:
            return {"error": f"Failed to retrieve stats: {str(e)}"}, 500