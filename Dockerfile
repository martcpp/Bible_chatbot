FROM astral-sh/uv:python3.12-alpine AS builder

# Enable bytecode compilation for faster startup
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

WORKDIR /app

# Install dependencies first (better caching)
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

# Final slim stage
FROM python:3.12-alpine
WORKDIR /app

# Copy the virtual environment from the builder
COPY --from=builder /app/.venv /app/.venv
COPY . /app

# Place the venv at the start of the PATH
ENV PATH="/app/.venv/bin:$PATH"

CMD ["python", "src/run.py"]
