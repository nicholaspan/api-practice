FROM python:3

WORKDIR /scripts/

ADD * /scripts/
RUN pip install flask


CMD [ "python", "api.py" ]
