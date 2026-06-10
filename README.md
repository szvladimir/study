# Study

A small FastAPI application that demonstrates two example API endpoints:

- `GET /` — health/status check.
- `POST /weather` — fetches weather data for a city from `wttr.in` and returns the current temperature in Celsius.
- `POST /poem` — generates a short poem using OpenAI chat completions.

## Architecture

- `app/main.py` is the main application entrypoint.
- The app uses `FastAPI` for HTTP routing and request handling.
- `pydantic` models validate request bodies.
- `httpx` makes asynchronous outbound calls to `wttr.in`.
- `openai` is used to call an OpenAI model for poem generation.
- `Dockerfile` builds a container image and starts the app with `uvicorn`.

## Key files

- `app/main.py` — defines the FastAPI app, endpoints, request models, and business logic.
- `requirements.txt` — lists the Python dependencies.
- `Dockerfile` — containerizes the application and starts the server.

## Execution flow

1. Start the app with `uvicorn app.main:app --host 0.0.0.0 --port 8000`.
2. `GET /` returns a JSON status response.
3. `POST /weather` accepts `{"city": "CityName"}`, fetches weather data from `https://wttr.in/{city}?format=j1`, and returns the current temperature.
4. `POST /poem` accepts `{"poet": "PoetName", "topic": "Topic"}`, builds a prompt, sends it to OpenAI, and returns the generated poem.

## Known limitations

- All logic is in `app/main.py`; the app is not fully modular.
- `app/` contains empty folders (`api/`, `clients/`, `db/`, `models/`, `services/`) that are not used.
- Error handling is minimal and returns raw error strings.
- There is no authentication, rate limiting, or caching.
- The app requires `OPENAI_API_KEY` to be set in the environment.
- `requests` is imported but unused in the current code.
- No tests are included, and the README was originally only a placeholder.
