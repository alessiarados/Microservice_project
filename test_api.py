"""
Simple test script to verify the API is working
Run this after starting your Flask application
"""

import requests
import json


def test_endpoint(url, data, operation_name):
    """Test a single API endpoint"""
    print(f"\n🧮 Testing {operation_name}...")
    print(f"📤 Sending: {data}")

    try:
        response = requests.post(url, json=data)

        if response.status_code == 200:
            result = response.json()
            print(f"✅ Success! Result: {result['result']}")
            print(f"⏱️  Execution time: {result['execution_time_ms']}ms")
        else:
            print(f"❌ Error {response.status_code}: {response.json()}")

    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API. Make sure the Flask app is running!")
    except Exception as e:
        print(f"❌ Error: {e}")


def test_health_check():
    """Test the health check endpoint"""
    print("🏥 Testing health check...")
    try:
        response = requests.get("http://localhost:5000/")
        if response.status_code == 200:
            print("✅ Health check passed!")
            print(f"📋 Response: {response.json()}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Health check error: {e}")


def main():
    """Run all tests"""
    base_url = "http://localhost:5000/api/v1"

    print("🚀 Testing Math Microservice API")
    print("=" * 50)

    # Test health check
    test_health_check()

    # Test power calculation
    test_endpoint(
        f"{base_url}/power",
        {"base": 2, "exponent": 3},
        "Power (2^3)"
    )

    # Test Fibonacci
    test_endpoint(
        f"{base_url}/fibonacci",
        {"n": 10},
        "Fibonacci (10th number)"
    )

    # Test factorial
    test_endpoint(
        f"{base_url}/factorial",
        {"n": 5},
        "Factorial (5!)"
    )

    # Test error handling
    print(f"\n🔍 Testing error handling...")
    test_endpoint(
        f"{base_url}/fibonacci",
        {"n": -1},  # Invalid input
        "Fibonacci with invalid input"
    )

    # Test new database endpoints
    print(f"\n📊 Testing database endpoints...")

    # Test history endpoint
    print("\n📜 Testing calculation history...")
    try:
        response = requests.get(f"{base_url}/history")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ History retrieved! Total records: {data['total_records']}")
            if data['calculations']:
                print(f"📋 Latest calculation: {data['calculations'][0]['operation']} = {data['calculations'][0]['result']}")
        else:
            print(f"❌ History endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"❌ History error: {e}")

    # Test stats endpoint
    print("\n📈 Testing statistics...")
    try:
        response = requests.get(f"{base_url}/stats")
        if response.status_code == 200:
            stats = response.json()
            print(f"✅ Stats retrieved!")
            print(f"📊 Total calculations: {stats.get('total_calculations', 0)}")
            print(f"🔢 Operations count: {stats.get('operations_count', {})}")
        else:
            print(f"❌ Stats endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Stats error: {e}")

    print(f"\n✨ Testing complete!")


if __name__ == "__main__":
    main()