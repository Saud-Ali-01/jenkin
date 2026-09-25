FROM python:latest

WORKDIR /python

COPY Game.py .
CMD ["python","Game.py"]