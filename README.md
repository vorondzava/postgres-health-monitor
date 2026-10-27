# PostgreSQL Health Monitor

Небольшой учебный проект на Python для мониторинга состояния PostgreSQL с помощью SQL-запросов.

## Purpose

Проект создан для практики DBA-задач, автоматизации сбора метрик PostgreSQL и изучения тестирования Python-приложений.

## Features

- Мониторинг активных подключений и долгих запросов.
- Получение размера базы данных и таблиц.
- Обнаружение блокировок.
- Определение статуса мониторинга: `OK`, `WARNING` или `CRITICAL`.
- Настраиваемые пороги предупреждений для длительных запросов и использования подключений.
- Логирование событий и ошибок.
- Проверка конфигурации подключения.
- Автоматические тесты основной логики.

## Technologies

- Python
- PostgreSQL
- Psycopg 3
- python-dotenv
- pytest
- SQL
- Git / GitHub

## Project structure

```text
postgres-health-monitor/
├── src/
│   ├── main.py
│   ├── database.py
│   ├── config.py
│   ├── monitor.py
│   └── report.py
├── sql/
├── tests/
│   └── test_report.py
├── .env.example
├── .gitignore
├── pytest.ini
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

- `main.py` — точка входа и последовательность выполнения мониторинга.
- `database.py` — подключение к PostgreSQL.
- `config.py` — чтение и проверка настроек.
- `monitor.py` — сбор данных о состоянии базы.
- `report.py` — анализ метрик и формирование статуса.
- `sql/` — SQL-запросы проекта.
- `tests/` — автоматические тесты.

## Requirements

- Python 3.13 или совместимая версия.
- Доступный сервер PostgreSQL.
- Git — для клонирования репозитория.

## Installation

Клонируйте репозиторий и перейдите в его каталог:

```bash
git clone <repository-url>
cd postgres-health-monitor
```

Создайте виртуальное окружение:

```bash
python -m venv .venv
```

Активируйте его в PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Установите зависимости:

```bash
python -m pip install -r requirements-dev.txt
```

## Configuration

Создайте локальный файл `.env` в корне проекта и укажите параметры подключения к PostgreSQL:

```dotenv
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database
DB_USER=your_user
DB_PASSWORD=your_password

LONG_QUERY_MINUTES=5
CONNECTION_USAGE_WARNING=80
CONNECTION_USAGE_CRITICAL=90
```

Замените примеры своими значениями. Не публикуйте реальные пароли и не добавляйте `.env` в Git.

## Run

Из корневого каталога проекта выполните:

```bash
python src/main.py
```

Программа соберёт доступные метрики, определит статус мониторинга и запишет события в `monitor.log`.

## Tests

Запустите автоматические тесты из корневого каталога:

```bash
python -m pytest -v
```

## Logging

События и ошибки записываются в файл `monitor.log`. Этот файл является локальным и исключён из Git.

## Project status

Учебный проект для практики мониторинга PostgreSQL, Python-автоматизации и тестирования. Не предназначен для использования в качестве полноценной промышленной системы мониторинга без дополнительной проверки и доработки.
