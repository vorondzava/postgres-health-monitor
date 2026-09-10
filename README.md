# PostgreSQL Health Monitor

Первый Небольшой учебный проект для проверки состояния PostgreSQL через SQL-запросы.

## Purpose

Проект создан для изучения DBA-задач:
- мониторинг активности PostgreSQL;
- анализ использования места;
- поиск проблем с блокировками.

## Features

- Active queries monitoring
- Database size analysis
- Table size analysis
- Waiting locks detection

## Структура проекта

postgres-health-monitor/
├── README.md
└── sql/
    ├── activity.sql
    ├── database_size.sql
    ├── table_size.sql
    ├── locks.sql
    └── health_report_draft.sql

## Technologies

- PostgreSQL
- SQL
- DBeaver
- Git/GitHub