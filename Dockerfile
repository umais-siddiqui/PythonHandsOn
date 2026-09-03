FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-install-project

COPY main.py ./
RUN uv sync --locked

CMD ["uv", "run", "main.py"]
