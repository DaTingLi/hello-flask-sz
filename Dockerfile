ARG PYVER=3.11
FROM python:${PYVER}-slim

# Build argument for PyPI mirror (supports domestic mirrors)
ARG PIP_INDEX_URL=https://pypi.org/simple

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install production dependencies only
RUN pip install --no-cache-dir --timeout 120 -i "${PIP_INDEX_URL}" -r requirements.txt

# Copy application code
COPY app.py .

# Expose port (container port, fixed at 8003)
EXPOSE 8003

# Run the application
CMD ["python", "app.py"]
