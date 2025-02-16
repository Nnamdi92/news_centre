FROM python:3.12-alpine
WORKDIR /app
COPY requirement.txt requirements.txt
COPY . /app/
RUN pip install -r requirements.txt
EXPOSE 5000
EXPOSE 3306
CMD ["flask", "run"]