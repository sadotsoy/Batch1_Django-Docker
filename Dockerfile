FROM python:3.5
WORKDIR /djangoApp
COPY djangoApp/damnificados/requirements.txt /djangoApp/requirements.txt
RUN pip install -r requirements.txt
COPY djangoApp/damnificados/ /djangoApp
CMD sh auto.sh
