"""
HTTP Playground
--------------
Practical examples of making HTTP requests using the `requests` library.
Note: Requires the `requests` library (`pip install requests`).
"""

import requests
import json

def demonstrate_get():
    print("\n--- GET Request (GitHub API) ---")
    try:
        # Get public events from GitHub
        url = "https://api.github.com/zen"
        response = requests.get(url, timeout=5)
        
        # Check if request was successful
        response.raise_for_status()
        
        print(f"Status Code: {response.status_code}")
        print(f"Zen of GitHub: {response.text}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def demonstrate_post():
    print("\n--- POST Request (httpbin) ---")
    url = "https://httpbin.org/post"
    payload = {
        "user": "python_learner",
        "task": "master_http",
        "progress": 0.75
    }
    
    try:
        # Sending JSON data
        response = requests.post(url, json=payload, timeout=5)
        response.raise_for_status()
        
        data = response.json()
        print(f"Status Code: {response.status_code}")
        print(f"Sent Data (echoed back): {data['json']}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def demonstrate_headers_and_auth():
    print("\n--- Custom Headers & Authentication Concepts ---")
    url = "https://httpbin.org/headers"
    custom_headers = {
        "User-Agent": "LearnPython-Reference-Bot/1.0",
        "X-Custom-Info": "Training-Session"
    }
    
    try:
        # Basic Auth (convenience parameter)
        # requests.get(url, auth=('user', 'pass'))
        
        response = requests.get(url, headers=custom_headers, timeout=5)
        print(f"Status Code: {response.status_code}")
        print(f"Reflected Headers: {json.dumps(response.json()['headers'], indent=2)}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def demonstrate_session():
    print("\n--- Persistent Session ---")
    # Sessions persist cookies and allow default configuration
    with requests.Session() as s:
        s.headers.update({"X-Session-ID": "12345"})
        
        # First request
        r1 = s.get("https://httpbin.org/get", timeout=5)
        # Second request (shares the session header)
        r2 = s.get("https://httpbin.org/get", timeout=5)
        
        print(f"Request 1 Status: {r1.status_code}")
        print(f"Request 2 Status: {r2.status_code}")
        print("Session headers successfully reused.")

if __name__ == "__main__":
    # Check if requests is installed
    try:
        import requests
    except ImportError:
        print("Error: 'requests' library not found. Please run 'pip install requests'.")
    else:
        demonstrate_get()
        demonstrate_post()
        demonstrate_headers_and_auth()
        demonstrate_session()
