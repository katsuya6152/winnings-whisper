FROM golang:1.22.0-alpine3.19

WORKDIR /app

COPY app/* ./
RUN go mod tidy

RUN go install github.com/cosmtrek/air@latest

CMD ["air", "-c", ".air.toml"]