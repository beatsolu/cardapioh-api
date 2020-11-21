FROM python:3.8.2-alpine
ENV PYTHONUNBUFFERED 1
ARG DEVELOPMENT
RUN apk update && \
    apk add \
    gcc \
    musl-dev \
    python3-dev \
    postgresql-dev \
    build-base \
    python3 \
    python3-dev \
    freetype-dev \
    fribidi-dev \
    harfbuzz-dev \
    jpeg-dev \
    lcms2-dev \
    openjpeg-dev \
    tcl-dev \
    tiff-dev \
    tk-dev \
    zlib-dev
WORKDIR cardapioh
COPY . /cardapioh
RUN pip install pipenv
RUN pipenv install --system --deploy $DEVELOPMENT
EXPOSE 8000
CMD ["gunicorn", \
     "--workers=2",\
     "--worker-class=gthread",  \
     "--worker-tmp-dir=/dev/shm",\
     "--threads=4", \
     "--log-file=-", \
     "--bind=0.0.0.0:$PORT",\
     "cardapioh.wsgi"]
