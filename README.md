# insomnia-raw-response

Мінімальний тестовий HTTP-сервер на стандартній бібліотеці Python.

## Endpoint

- `GET /file`
- Повертає файл `test.txt.p7s`
- Заголовки відповіді:
  - `Content-Type: application/x-p7s`
  - `Content-Disposition: attachment; filename="test.txt.p7s"`

## Run

```bash
python3 main.py
```

Сервер запускається на `http://0.0.0.0:8080`.

## Optional: curl

```bash
curl -i http://localhost:8080/file
```

Зберегти файл локально:

```bash
curl -OJ http://localhost:8080/file
```
