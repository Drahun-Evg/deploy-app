FROM python:3
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /usr/support
COPY requirements.txt /usr/support/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /usr/support/

COPY start.sh /usr/support/start.sh
RUN chmod +x /usr/support/start.sh
ENTRYPOINT '/usr/support/start.sh'
