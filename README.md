# Transloth

API for translating text between languages, using **ollama** and **FastAPI**. Development environment in **Docker**.

It is called **Transloth** because the bigger the model is the slower it gets locally, like a sloth.

## Usage

Build ollama and web services:

```bash
make build
```

Start the services:

```bash
make start
```

After starting the services, the API will be available at `http://localhost:8000`.

## Example

Request:

```requests
POST localhost:8000/translate
Content-Type: application/json

{
    "text": "Hello, world!",
    "source: "english",
    "target: "spanish"
}
```

**Source and target has to be named explicitly.**

Response:

```json
{
    "text": "Hola, mundo!"
}
```

## API documentation

The API documentation is available at `http://localhost:8000/docs` in _openapi_ format.

## Development

Access ollama container shell:

```bash
make shell-ollama
```

Access web container shell:

```bash
make shell-web
```

Inspect ollama logs:

```bash
make logs-ollama
```

Inspect web logs:

```bash
make logs-web
```

Send two test requests with curl:
```bash
make test-request
```

Run quality checks:

```bash
make lint
```

Fix quality issues:

```bash
make fix;
```
