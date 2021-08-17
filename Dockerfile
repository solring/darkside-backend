FROM python:3
RUN mkdir /backend
COPY ./app /backend/app
COPY ./requirements.txt  /backend/.

WORKDIR /backend
RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "-b 0.0.0.0:5000", "app:app"]

EXPOSE 5000