FROM jupyter/scipy-notebook:2c80cf3537ca

RUN pip install --upgrade pip
RUN pip install --upgrade pymystem3
RUN pip install --upgrade gensim
RUN pip install --upgrade wordcloud
RUN pip install --upgrade numpy
RUN pip install --upgrade matplotlib
RUN pip install --upgrade pandas
RUN pip install --upgrade scipy
RUN pip install --upgrade python-Levenshtein