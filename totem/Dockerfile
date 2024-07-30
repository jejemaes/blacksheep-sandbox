FROM python:3.11

WORKDIR /usr/src/
EXPOSE 8000

# Recommended Python flags
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install Python packages requirements
COPY ./requirements.txt /usr/src/requirements.txt
RUN --mount=type=ssh pip install --no-cache-dir \
    -r /usr/src/requirements.txt

# Install runtime dependencies
RUN apt-get -qq update && \
    apt-get install -q -y --no-install-recommends \
    curl

# Copy project source files
COPY ./ ./

# Run
CMD ["unvicorn", "/usr/src/app/main:app", "--port", "8000"]