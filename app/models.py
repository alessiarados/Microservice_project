"""
Pydantic models for data validation
These models define what data we expect from API requests and responses
"""

from pydantic import BaseModel, Field, validator
from typing import Union
from datetime import datetime


class PowerRequest(BaseModel):
    """
    Model for power calculation requests
    Validates that we receive proper base and exponent values
    """
    base: Union[int, float] = Field(..., description="The base number")
    exponent: Union[int, float] = Field(..., description="The exponent number")

    @validator('base', 'exponent')
    def validate_numbers(cls, v):
        """Ensure the numbers are reasonable"""
        if abs(v) > 10000:
            raise ValueError('Number too large (max absolute value: 10000)')
        return v


class FibonacciRequest(BaseModel):
    """
    Model for Fibonacci calculation requests
    Validates that we receive a proper position value
    """
    n: int = Field(..., ge=0, le=1000, description="Position in Fibonacci sequence (0-1000)")


class FactorialRequest(BaseModel):
    """
    Model for factorial calculation requests
    Validates that we receive a proper number for factorial
    """
    n: int = Field(..., ge=0, le=100, description="Number for factorial calculation (0-100)")


class MathResponse(BaseModel):
    """
    Standard response model for all mathematical operations
    This ensures all responses have the same structure
    """
    operation: str = Field(..., description="Type of operation performed")
    input_data: dict = Field(..., description="The input parameters")
    result: Union[int, float] = Field(..., description="The calculation result")
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat(),
                          description="When the calculation was performed")
    execution_time_ms: float = Field(..., description="How long the calculation took in milliseconds")


class ErrorResponse(BaseModel):
    """
    Standard error response model
    Used when something goes wrong
    """
    error: str = Field(..., description="Error message")
    operation: str = Field(..., description="Operation that failed")
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())
    status_code: int = Field(..., description="HTTP status code")