# Neo4j LlamaIndex Starter Kit

## Usage
```
poetry install
poetry run uvicorn llamaindex_starter_kit.main:app --reload
```

Default local address will be: http://127.0.0.1:8000

To change port, append above with `--port=<port>`

## Docs
FastAPI will automatically generate a swagger doc interface at a `/docs#` path from above