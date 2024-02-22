FROM python:3.12
LABEL authors="joshvoyles"
ENV PYTHONUNBUFFERED=1
WORKDIR /
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "./umgc.bot.py"]