FROM python:alpine3.22

WORKDIR /app/back

COPY config.py requirements.txt alembic.ini ./

RUN pip install -r ./requirements.txt && \
    pip install uvicorn[standard]

COPY migrations ./migrations
COPY secure ./secure
COPY main.py ./
COPY shemas.py database.py ./
COPY routes ./routes
COPY models ./models

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]