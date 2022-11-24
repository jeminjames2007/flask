FROM python:3.10
EXPOSE 5000
WORKDIR /app/
COPY . .
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install -r requirements.txt
CMD ["flask","run","--host","0.0.0.0"]

#docker-compose up