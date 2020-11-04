FROM python:3

WORKDIR /app
ENV PYTHONUNBUFFERED 1
EXPOSE 80

COPY club_api .

COPY requirements.txt /tmp/requirements.txt 
RUN python3 -m pip install -U -r /tmp/requirements.txt

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT [ "entrypoint.sh" ]