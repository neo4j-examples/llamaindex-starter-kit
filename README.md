# Neo4j LlamaIndex Starter Kit

## Requirements
- Run `poetry self add poetry-plugin-dotenv` if you don't want to pass env vars manually
- Copy the `env.sample` as `.env` and replace the empty values with your Neo4j credentials


## Usage
```
poetry install
poetry run uvicorn llamaindex_starter_kit.main:app --reload
```

Or if not using poetry-plugin-dotenv above:
```
NEO4J_URI=<database_uri> \
NEO4J_DATABASE=<database_name> \
NEO4J_USERNAME=<username> \
NEO4J_PASSWORD=<password> \
OPENAI_API_KEY=<api_key> \
poetry run uvicorn llamaindex_starter_kit.main:app --reload
```


Default local address will be: http://127.0.0.1:8000

To change port, append above with `--port=<port>`

## Docs
FastAPI will automatically generate a swagger doc interface at a `/docs#` path from above