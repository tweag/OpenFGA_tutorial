FROM python:3.12-slim

WORKDIR /app

# Copy project files including README.md
COPY pyproject.toml uv.lock README.md ./
COPY fga_example ./fga_example

# Install UV and use it to install dependencies with --system flag
RUN pip install --no-cache-dir uv && \
    uv pip install --system --no-cache-dir .

EXPOSE 8000

CMD ["uvicorn", "fga_example.main:app", "--host", "0.0.0.0", "--port", "8000"]