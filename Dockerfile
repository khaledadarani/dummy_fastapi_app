FROM bitnami/python:3.11
WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./main.py main.py
#RUN apt-get purge -y --auto-remove $buildDeps
CMD python main.py
