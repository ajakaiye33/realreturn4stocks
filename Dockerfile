# Use a specific Python image
FROM python:3.8.13-slim-buster as builder

# Create app directory
WORKDIR /app

# Install build dependencies and compile wheels
COPY requirements.txt ./requirements.txt
RUN pip install --upgrade pip && \
    pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r requirements.txt

# Use a clean image to produce the final image
FROM python:3.8.13-slim-buster

# Create a non-root user
RUN useradd -m myuser
USER myuser

# Copy only the dependencies installation from the 1st stage image
COPY --from=builder /wheels /wheels
COPY --from=builder /app/requirements.txt .

# Install packages
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --find-links=/wheels -r requirements.txt && \
    rm -rf /wheels && \
    rm -f requirements.txt

# Set work directory
WORKDIR /app

# Copy other application files
COPY . .

# Set Streamlit configuration
EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501"]
