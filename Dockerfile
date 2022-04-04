FROM python:3.9-slim

RUN pip install --no-cache-dir "https://github.com/Renaud11232/dark-offelsalat/archive/refs/heads/master.zip"

ENTRYPOINT ["dark-offelsalat"]