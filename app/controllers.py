"""
Controllers - Business logic for mathematical operations
This file contains the actual mathematical functions
"""

import time
from typing import Union


class MathController:
    """
    Controller class that handles all mathematical operations
    """

    @staticmethod
    def calculate_power(base: Union[int, float], exponent: Union[int, float]) -> float:
        """
        Calculate base raised to the power of exponent (base^exponent)

        Args:
            base: The base number
            exponent: The exponent number

        Returns:
            float: Result of base^exponent

        Raises:
            ValueError: If inputs are invalid
        """
        try:
            result = base ** exponent
            return float(result)
        except Exception as e:
            raise ValueError(f"Error calculating power: {str(e)}")

    @staticmethod
    def calculate_fibonacci(n: int) -> int:
        """
        Calculate the nth Fibonacci number
        Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

        Args:
            n: Position in Fibonacci sequence (0-based)

        Returns:
            int: The nth Fibonacci number

        Raises:
            ValueError: If n is negative or too large
        """
        if n < 0:
            raise ValueError("Fibonacci position cannot be negative")
        if n > 1000:  # Prevent very large calculations
            raise ValueError("Fibonacci position too large (max 1000)")

        if n == 0:
            return 0
        elif n == 1:
            return 1

        # Use iterative approach for efficiency
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b

        return b

    @staticmethod
    def calculate_factorial(n: int) -> int:
        """
        Calculate the factorial of n (n!)
        Factorial: n! = n × (n-1) × (n-2) × ... × 1

        Args:
            n: Number to calculate factorial for

        Returns:
            int: The factorial of n

        Raises:
            ValueError: If n is negative or too large
        """
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if n > 100:  # Prevent very large calculations
            raise ValueError("Number too large for factorial calculation (max 100)")

        if n == 0 or n == 1:
            return 1

        result = 1
        for i in range(2, n + 1):
            result *= i

        return result


# Create a global instance to use in views
math_controller = MathController()