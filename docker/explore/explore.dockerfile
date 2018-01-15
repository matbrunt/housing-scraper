FROM jupyter/pyspark-notebook:latest

USER root

COPY ./requirements.txt /home/jovyan/requirements.txt
RUN pip3 install -r /home/jovyan/requirements.txt

ENV PYTHONPATH /home/jovyan/work/scripts:$PYTHONPATH

COPY ./ipython_config.py /home/jovyan/.ipython/profile_default/ipython_config.py
COPY ./custom.css /home/jovyan/.jupyter/custom/custom.css
COPY ./jupyter_notebook_config.py /home/jovyan/.jupyter/jupyter_notebook_config.py

RUN chown -R jovyan:users /home/jovyan

USER 1000