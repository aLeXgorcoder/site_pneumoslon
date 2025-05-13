# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry
ENV POETRY_VERSION=1.8.2
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Копируем pyproject.toml и poetry.lock
COPY pyproject.toml poetry.lock /app/

# Устанавливаем зависимости без создания виртуального окружения
ENV POETRY_VIRTUALENVS_CREATE=false
RUN poetry install --no-interaction --no-ansi

# Копируем исходный код проекта
COPY . /app

# Открываем порт
EXPOSE 8000

# Команда по умолчанию
CMD ["python", "site_pneumoslon/manage.py", "runserver", "0.0.0.0:8000"]
