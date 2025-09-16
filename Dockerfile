FROM ghcr.io/astral-sh/uv:debian

WORKDIR /app

COPY . .

RUN uv sync

RUN chmod +x docker/run-server.sh

CMD ["/app/docker/run-server.sh"]
