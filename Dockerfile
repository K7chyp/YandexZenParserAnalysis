FROM jupyter/scipy-notebook:2c80cf3537ca

RUN pip install --upgrade pip
RUN pip freeze > requirements.txt