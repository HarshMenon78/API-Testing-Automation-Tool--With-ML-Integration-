import requests
import time

def run_test_case(data, model=None):
    """
    Runs an API test case and returns actual results.
    data should include: url, method, headers, body
    """
    url = data.get("url")
    method = data.get("method", "GET").upper()
    headers = data.get("headers", {})
    body = data.get("body", None)

    start_time = time.time()

    try:
        # Make the actual API call
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, headers=headers, json=body)
        elif method == "PUT":
            response = requests.put(url, headers=headers, json=body)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, json=body)
        else:
            return {
                "status": "Test Failed",
                "message": f"Unsupported method: {method}"
            }

        end_time = time.time()
        execution_time_ms = int((end_time - start_time) * 1000)

        # Build the test result
        return {
            "status": "Test Passed" if response.status_code in range(200, 300) else "Test Failed",
            "url_tested": url,
            "method": method,
            "status_code": response.status_code,
            "response_body": response.json() if "application/json" in response.headers.get("Content-Type", "") else response.text,
            "execution_time_ms": execution_time_ms,
            "message": "Request successful" if response.status_code in range(200, 300) else "Request failed"
        }

    except Exception as e:
        return {
            "status": "Test Failed",
            "message": f"Error: {str(e)}"
        }
