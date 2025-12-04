# Автоматизация тестирования effective-mobile.ru

## Описание проекта
Проект содержит автоматизированные UI тесты для главной страницы сайта effective-mobile.ru с использованием Python, Playwright и паттерна Page Object.

## Технологии
- Python 3.10
- Playwright
- Pytest
- Allure
- Docker

## Структура проекта
```
project/
├── tests/               # Тесты
│   ├── test_main_page.py
│   └── conftest.py
├── pages/               # Page Object модели
│   ├── base_page.py
│   └── main_page.py
├── utils/               # Утилиты
│   ├── config.py
│   └── helpers.py
├── requirements.txt     # Зависимости Python
├── Dockerfile          # Docker конфигурация
├── pytest.ini          # Конфигурация pytest
├── .env.example        # Пример переменных окружения
└── README.md           # Документация
```

## Установка и запуск

### Локальный запуск

1. Клонировать репозиторий:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Создать виртуальное окружение:
```bash
python3.10 -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows
```

3. Установить зависимости:
```bash
pip install -r requirements.txt
playwright install chromium
```

4. Настроить переменные окружения:
```bash
cp .env.example .env
# Отредактировать .env при необходимости
```

5. Запустить тесты:
```bash
pytest tests/ -v --alluredir=allure-results
```

6. Просмотреть отчет Allure:
```bash
allure serve allure-results
```

### Запуск в Docker

1. Собрать Docker образ:
```bash
docker build -t effective-mobile-tests .
```

2. Запустить контейнер:
```bash
docker run --rm -v $(pwd)/allure-results:/app/allure-results effective-mobile-tests
```

3. Просмотреть результаты:
```bash
allure serve allure-results
```

## Запуск отдельных тестов

```bash
# Все тесты
pytest tests/

# Конкретный файл
pytest tests/test_main_page.py

# Конкретный тест
pytest tests/test_main_page.py::TestMainPage::test_navigation_sections

# С маркерами
pytest -m smoke
```

## Отчеты
После запуска тестов отчеты Allure сохраняются в директории `allure-results/`.
Для просмотра используйте команду `allure serve allure-results`.
