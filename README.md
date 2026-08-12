# Del campo a tu oficina

A FastAPI web application containerized to run on port `5010`.

## What was added

- FastAPI app entrypoint in `app/main.py`
- Python package initializer in `app/__init__.py`
- Static photo folder at `static/photos/` with `.gitkeep`
- `.gitignore` and `.dockerignore` to keep uploaded photos out of Git and Docker images
- `docker-compose.yml` updated for port `5010`, container restart policy, and a reusable static volume

## Run locally

Build and run the application:

```bash
docker compose build
docker compose up
```

Then open `http://localhost:5010`.

The web app also exposes a health endpoint at:

```bash
http://localhost:5010/health
```

## Docker Compose and scaling

The Compose file is configured with `deploy.replicas: 1` by default. To scale the web service up to 3 containers manually, use:

```bash
docker compose up --scale web=3
```

For automatic scaling, deploy with Docker Swarm or another orchestrator. Example Swarm commands:

```bash
docker swarm init
docker stack deploy -c docker-compose.yml delcampo
```

## Photo uploads

Place local photos in `static/photos/` and they will be served from the homepage. Uploaded photo files are ignored by Git except the `.gitkeep` placeholder.
