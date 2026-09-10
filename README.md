# Sprint_6 — Автотесты для сервиса «Яндекс.Самокат»

Учебный проект с автотестами для сервиса аренды самокатов
[«Яндекс.Самокат»](https://qa-scooter.praktikum-services.ru/).

## Что проверяют тесты

1. **Выпадающий список «Вопросы о важном»** — при клике на стрелку
   раскрывается соответствующий текст ответа (8 вопросов, отдельный тест на каждый).
2. **Заказ самоката** — полный позитивный сценарий:
   - две точки входа (кнопка «Заказать» вверху и внизу страницы);
   - заполнение формы заказа;
   - подтверждение и появление окна «Заказ оформлен».
   Тесты параметризованы двумя наборами данных.
3. **Навигация по логотипам**:
   - клик по логотипу «Самокат» ведёт на главную страницу;
   - клик по логотипу «Яндекс» открывает Дзен в новом окне.

## Технологии

- Python 3.12
- Selenium WebDriver 4.16
- Pytest 7.4
- Allure (отчётность)
- Mozilla Firefox

## Структура проекта

```
Sprint_6/
├── allure_results/       # Результаты тестов для Allure (создаётся при запуске)
├── locators/             # Локаторы элементов
│   ├── __init__.py
│   ├── base_locators.py
│   ├── header_page_locators.py
│   ├── main_page_locators.py
│   └── order_page_locators.py
├── pages/                # Page Object
│   ├── __init__.py
│   ├── base_page.py
│   ├── header_page.py
│   ├── main_page.py
│   └── order_page.py
├── tests/                # Тесты
│   ├── __init__.py
│   ├── test_questions.py
│   ├── test_order_flow.py
│   └── test_logo_navigation.py
├── conftest.py           # Фикстуры (драйвер Firefox)
├── pytest.ini            # Настройки pytest
├── requirements.txt      # Зависимости
└── README.md
```

## Установка

1. Клонировать репозиторий и перейти в папку проекта:
   ```bash
   git clone <ссылка-на-репозиторий>
   cd Sprint_6
   ```

2. Установить зависимости:
   ```bash
   py -m pip install -r requirements.txt
   ```

3. Убедиться, что установлен браузер **Mozilla Firefox**
   (драйвер `geckodriver` Selenium подхватывает автоматически).

## Запуск тестов

Запустить все тесты:
```bash
py -m pytest
```

Запустить конкретный файл:
```bash
py -m pytest tests/test_order_flow.py
```

Запустить конкретный тест:
```bash
py -m pytest tests/test_questions.py::TestQuestions::test_answer_text_is_correct
```

## Allure-отчёт

Запустить тесты с сохранением результатов:
```bash
py -m pytest --alluredir=allure_results
```

Сгенерировать и открыть отчёт в браузере:
```bash
allure serve allure_results
```

Либо сгенерировать статический отчёт:
```bash
allure generate allure_results -o allure_report --clean
allure open allure_report
```

## Особенности реализации

- **Page Object Model** — логика работы со страницами вынесена
  в классы `pages/`, локаторы — в `locators/`.
- **Параметризация** — используется в `test_questions.py` (8 вопросов)
  и `test_order_flow.py` (2 набора данных, 2 точки входа).
- **Явные ожидания** — `WebDriverWait` в `BasePage` для стабильности тестов.
- **Общие элементы** — вынесены в `base_page.py` и `base_locators.py`.
