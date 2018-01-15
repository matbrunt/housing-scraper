FROM python:3.6

ENV TZ=Europe/London
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY ./requirements.txt /usr/src/requirements.txt
RUN pip3 install -r /usr/src/requirements.txt

ENV PYTHONPATH=/usr/src/app/scripts