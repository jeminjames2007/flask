FROM python:3.10
EXPOSE 5000
WORKDIR /app/
COPY . .
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install -r requirements.txt
CMD ["flask","run","--host","0.0.0.0"]

#docker build -t rest-api-flask .
#docker run -i -t -d -p 6080:5000 rest-api-flask