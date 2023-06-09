# test_task_encost
- Тестовое задание на позицию python-разработчик в компанию ООО «Энкост»
- В папке проекта (test_task) находится заготовка web-приложения на фреймворке PlotlyDash. В файле testDB.db находится тестовая база данных sqlite (описание полей базы данных представлено ниже).
- Задание заключается в разработке приложения, которое позволяет просматривать данные из бд в различных форматах:
  *	Вывод общей информации в правой верхней карточке
  *	Вывод в виде круговой диаграммы причин состояний (plotly.express.pie)
  *	Вывод диаграммы ганта длительностей состояний (plotly.express.timeline)
  *	Вывод дополнительной информации для длительностей при наведении (свойство hovertemplate)
  *	Дополнительно: фильтрация по состояниям (необходимо использование callback).

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/kittygram2plus.git
```

```
cd test_task_encost
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```


Запустить проект:

```
python3 test_task/app.py
```
