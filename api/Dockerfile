FROM python:3.11-slim

# Install curl to get uv
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Install uv
RUN curl -Ls https://astral.sh/uv/install.sh | sh

# Set workdir
WORKDIR /app

# Copy project files
COPY . /app

# Create virtual env (optional but good practice)
RUN uv venv && \
    .venv/bin/uv pip sync

# Use uvicorn with the venv Python
CMD [".venv/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
