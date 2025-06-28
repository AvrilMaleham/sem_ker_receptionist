FROM python:3.10-slim

WORKDIR /app

# Install uv tool and sync dependencies
COPY pyproject.toml .
RUN pip install --no-cache-dir uv && uv sync

# Copy the rest of the project
COPY . .

CMD ["uv", "run", "python", "main.py"]

