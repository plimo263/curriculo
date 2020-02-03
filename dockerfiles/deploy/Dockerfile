FROM python:3.5

RUN apt-get update && apt-get install tzdata && apt-get clean && \
pip3 install gunicorn flask pymongo pillow pycep-correios requests validate-docbr

ENV TZ='America/Sao_Paulo'

WORKDIR /dados

EXPOSE 5000

ENTRYPOINT gunicorn -t 360 -w 4 -b 0.0.0.0:5000 --access-logfile - index:app
