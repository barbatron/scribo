FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Copy only poetry config first for better layer caching
COPY pyproject.toml ./

# Configure poetry to not create a virtual environment in the container
RUN poetry config virtualenvs.create false

# Install dependencies (including dev dependencies for ruff)
RUN poetry install --no-interaction --no-ansi

# Copy the application code
COPY . .

# Run ruff to verify formatting and linting
RUN poetry run ruff check . && poetry run ruff format --check .

# Install only production dependencies for the final image
RUN poetry install --only main --no-interaction --no-ansi

# Set the entrypoint to run the script with the provided audio file
ENTRYPOINT ["python", "scribo.py"]
