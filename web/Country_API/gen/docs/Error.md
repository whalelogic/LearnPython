# Error


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | The HTTP status code or a custom error code. |
**message** | **str** | A human-readable error message. |

## Example

```python
from openapi_client import Error

# TODO update the JSON string below
json = "{}"
# create an instance of Error from a JSON string
error_instance = Error.from_json(json)
# print the JSON string representation of the object
print(Error.to_json())

# convert the object into a dict
error_dict = error_instance.to_dict()
# create an instance of Error from a dict
error_from_dict = Error.from_dict(error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

---

## Error Model Usage Guide

This model represents API error responses in the generated client.

### Why this matters

Reliable error handling is required for:

- user-friendly messages
- retry logic
- alerting and monitoring
- debugging API integrations

If you ignore error payloads, client code becomes brittle and hard to support.

## Field Semantics

### `code`

- Usually aligns with HTTP status (for example `400`, `404`, `500`).
- Can also represent domain-specific numeric error codes.
- Should always be interpreted together with `message`.

### `message`

- Human-readable detail about what failed.
- Safe to log.
- Should not be parsed for logic when numeric/code fields exist.

## Recommended Handling Pattern

```python
def handle_error(err: Error) -> str:
    if err.code == 400:
        return "Request invalid. Check required fields and formats."
    if err.code == 401:
        return "Authentication failed. Check credentials or token."
    if err.code == 404:
        return "Resource not found. Verify endpoint or identifier."
    if err.code >= 500:
        return "Server issue. Retry later or escalate."
    return err.message
```

## Retry Decision Table

| Code range | Typical meaning | Retry? |
|---|---|---|
| 400-499 | Client-side request issue | Usually no |
| 401/403 | Auth/permission issue | No, fix credentials/permissions |
| 404 | Missing resource | No, verify identifier |
| 409 | Conflict/state issue | Maybe after state refresh |
| 429 | Rate limited | Yes, with backoff |
| 500-599 | Server/transient issue | Yes, with capped retries |

## Logging Guidance

When logging this model, include:

- timestamp
- request ID / correlation ID
- endpoint
- status code
- sanitized message

Avoid logging secrets, tokens, or raw sensitive payloads.

## Serialization Notes

Use `to_dict()` or `to_json()` for transport/logging snapshots.

Use `from_dict()` / `from_json()` when parsing error payloads from the API.

If fields are missing, your client should fail gracefully and produce a fallback message.

## Fallback Error Strategy

If response parsing fails:

1. Capture HTTP status code.
2. Keep raw body excerpt (truncated).
3. Build a generic `Error` value in local code.
4. Return a safe, readable message.

Example fallback message:

- `"Request failed with status 502; could not parse error body."`

## Client-Side UX Recommendations

- Show concise user text.
- Keep technical detail in logs.
- Map known `code` values to actionable suggestions.
- Include retry hint when appropriate.

## Monitoring Recommendations

Track metrics grouped by:

- `code`
- endpoint
- operation type
- time window

Alert on sudden spikes in:

- 5xx errors
- 429 rate limits
- auth failures

## Practice Prompts

1. Implement `code -> user message` mapping.
2. Add exponential backoff for transient errors.
3. Add structured logging with request IDs.
4. Add unit tests for 400/404/429/500 handling.
5. Add fallback handling for malformed error payloads.

## Quick Self-Check

- Do you distinguish retriable and non-retriable errors?
- Do logs include enough context for debugging?
- Are user messages safe and understandable?
- Are secrets excluded from logs?
- Do tests cover unhappy paths?

## Related Docs

- [DefaultApi.md](DefaultApi.md)
- [Country.md](Country.md)
- [../README.md](../README.md)
