# insomnia-raw-response

A minimal test HTTP server using Python's standard library.

## Endpoint

- `GET /file`
- Returns the file `test.txt.p7s`
- Response headers:
  - `Content-Type: application/x-p7s`
  - `Content-Disposition: attachment; filename="test.txt.p7s"`

## Run

```bash
python3 main.py
```

The server starts at `http://0.0.0.0:8080`.

## Optional: curl

```bash
curl -i http://localhost:8080/file
```

Save the file locally:

```bash
curl -OJ http://localhost:8080/file
```
