FROM python:3.9-slim-buster

ARG MOTD="Default MOTD"
ARG PORT=8000

ENV MOTD=${MOTD}
ENV PORT=${PORT}

COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE ${PORT}

CMD ["python", "motd.py"]
