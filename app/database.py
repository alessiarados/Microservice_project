"""
Database setup and operations for storing API requests
SQLite database to persist all mathematical calculations
"""

import sqlite3
import json
import os
from datetime import datetime
from typing import List, Dict, Any


class DatabaseManager:
    """
    Manages SQLite database operations for storing calculation requests
    """

    def __init__(self, db_path: str = "math_calculations.db"):
        """
        Initialize database manager

        Args:
            db_path: Path to SQLite database file
        """
        self.db_path = db_path
        self.init_database()

    def init_database(self):
        """
        Initialize the database and create tables if they don't exist
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Create calculations table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS calculations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    operation TEXT NOT NULL,
                    input_data TEXT NOT NULL,
                    result REAL NOT NULL,
                    execution_time_ms REAL NOT NULL,
                    timestamp TEXT NOT NULL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')

            conn.commit()
            conn.close()

            print(f"✅ Database initialized: {self.db_path}")

        except Exception as e:
            print(f"❌ Database initialization error: {e}")

    def save_calculation(self, operation: str, input_data: Dict[str, Any],
                         result: float, execution_time_ms: float) -> bool:
        """
        Save a calculation request to the database

        Args:
            operation: Type of mathematical operation (power, fibonacci, factorial)
            input_data: Dictionary with input parameters
            result: Calculation result
            execution_time_ms: Time taken for calculation in milliseconds

        Returns:
            bool: True if saved successfully, False otherwise
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            timestamp = datetime.now().isoformat()
            input_json = json.dumps(input_data)

            cursor.execute('''
                INSERT INTO calculations 
                (operation, input_data, result, execution_time_ms, timestamp)
                VALUES (?, ?, ?, ?, ?)
            ''', (operation, input_json, result, execution_time_ms, timestamp))

            conn.commit()
            conn.close()

            print(f"💾 Saved {operation} calculation: {input_data} = {result}")
            return True

        except Exception as e:
            print(f"❌ Error saving calculation: {e}")
            return False

    def get_calculation_history(self, limit: int = 100) -> List[Dict[str, Any]]:
        """
        Retrieve calculation history from database

        Args:
            limit: Maximum number of records to retrieve

        Returns:
            List of calculation records
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cursor.execute('''
                SELECT id, operation, input_data, result, execution_time_ms, timestamp, created_at
                FROM calculations 
                ORDER BY created_at DESC 
                LIMIT ?
            ''', (limit,))

            records = cursor.fetchall()
            conn.close()

            # Convert to list of dictionaries
            history = []
            for record in records:
                history.append({
                    'id': record[0],
                    'operation': record[1],
                    'input_data': json.loads(record[2]),
                    'result': record[3],
                    'execution_time_ms': record[4],
                    'timestamp': record[5],
                    'created_at': record[6]
                })

            return history

        except Exception as e:
            print(f"❌ Error retrieving history: {e}")
            return []

    def get_operation_stats(self) -> Dict[str, Any]:
        """
        Get statistics about API usage

        Returns:
            Dictionary with usage statistics
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Total calculations
            cursor.execute('SELECT COUNT(*) FROM calculations')
            total_calculations = cursor.fetchone()[0]

            # Calculations by operation
            cursor.execute('''
                SELECT operation, COUNT(*) as count 
                FROM calculations 
                GROUP BY operation
            ''')
            operations_count = dict(cursor.fetchall())

            # Average execution time by operation
            cursor.execute('''
                SELECT operation, AVG(execution_time_ms) as avg_time 
                FROM calculations 
                GROUP BY operation
            ''')
            avg_times = dict(cursor.fetchall())

            conn.close()

            return {
                'total_calculations': total_calculations,
                'operations_count': operations_count,
                'average_execution_times': avg_times
            }

        except Exception as e:
            print(f"❌ Error getting stats: {e}")
            return {}

    def clear_history(self) -> bool:
        """
        Clear all calculation history (useful for testing)

        Returns:
            bool: True if cleared successfully
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cursor.execute('DELETE FROM calculations')
            conn.commit()
            conn.close()

            print("🗑️  Calculation history cleared")
            return True

        except Exception as e:
            print(f"❌ Error clearing history: {e}")
            return False


# Create global database manager instance
db_manager = DatabaseManager()