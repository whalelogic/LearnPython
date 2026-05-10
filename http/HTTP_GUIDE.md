# HTTP in Python

HTTP (Hypertext Transfer Protocol) is the foundation of data exchange on the web. In Python, interacting with HTTP services is primarily done using the `requests` library or built-in modules like `http.client` and `urllib`.

## Common HTTP Methods and Status Codes

### Methods

| Method | Description | Idempotent |
|---|---|---|
| `GET` | Retrieve data from a resource | Yes |
| `POST` | Submit data to be processed | No |
| `PUT` | Replace a resource completely | Yes |
| `PATCH` | Update a resource partially | No |
| `DELETE` | Remove a resource | Yes |

### Common Status Codes

| Code | Category | Meaning |
|---|---|---|
| `200` | Success | OK - Request succeeded |
| `201` | Success | Created - Resource successfully created |
| `204` | Success | No Content - Request succeeded, no body returned |
| `400` | Client Error | Bad Request - Server couldn't understand request |
| `401` | Client Error | Unauthorized - Authentication required |
| `403` | Client Error | Forbidden - Server refuses to authorize |
| `404` | Client Error | Not Found - Resource does not exist |
| `500` | Server Error | Internal Server Error - Generic server failure |

---

## The `requests` Library

`requests` is the de-facto standard for HTTP in Python. It is elegant, simple, and powerful.

### Installation
```bash
pip install requests
```

### Basic Usage

```python
import requests

# GET request
response = requests.get('https://api.github.com/events')
print(response.status_code)
print(response.json())

# POST request with JSON
data = {'key': 'value'}
response = requests.post('https://httpbin.org/post', json=data)
print(response.status_code)
```

## Advanced Patterns

### Sessions
Sessions allow you to persist certain parameters across multiple requests (like cookies or headers).

```python
import requests

with requests.Session() as session:
    session.headers.update({'Authorization': 'Bearer token'})
    # Both requests will have the auth header
    session.get('https://api.example.com/user')
    session.get('https://api.example.com/settings')
```

### Error Handling
Always check for successful status codes using `raise_for_status()`.

```python
try:
    response = requests.get('https://api.example.com/data')
    response.raise_for_status() # Raises HTTPError for 4xx/5xx
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except Exception as err:
    print(f"Other error occurred: {err}")
```

---

## Best Practices

- **Use Timeouts:** Never make a request without a timeout (`requests.get(url, timeout=5)`).
- **Check Status Codes:** Don't assume a request worked; check `response.ok` or `response.status_code`.
- **Use JSON:** When sending/receiving data, use `json=params` and `response.json()` for automatic serialization.
- **Environment Variables:** Keep API keys and secrets in environment variables, not in code.

---

## Progress Rubric

| Level | Demonstrated ability |
|---|---|
| **Beginner** | Perform basic `GET` requests and print status codes. |
| **Developing** | Use `POST` with JSON data, handle basic exceptions, and use `response.json()`. |
| **Proficient** | Use `requests.Session`, custom headers, and implement robust error handling with `raise_for_status()`. |
| **Advanced** | Handle streaming responses, custom authentication flows, and use `asyncio` with `httpx`. |

## Suggested Practice Projects

1. **GitHub Explorer:** Use the GitHub API to list your repositories and their stars.
2. **Weather CLI:** Fetch weather data from a public API based on user-provided city names.
3. **URL Checker:** A script that takes a list of URLs and reports their status codes and response times.
4. **Simple Proxy:** A Flask server that forwards requests to another API and returns the result.

## Common Gotchas

| Gotcha | Explanation | Fix |
|---|---|---|
| Missing Timeouts | Requests can hang indefinitely | Always provide a `timeout` argument |
| `response.text` vs `response.json()` | `text` is raw string, `json()` parses it | Use `json()` for API responses to get a dict/list |
| Forgetting `with` | Connections might stay open | Use `requests.Session()` with a `with` block |
| Auth in URL | Putting keys in the query string is less secure | Use headers (e.g., `Authorization`) whenever possible |
