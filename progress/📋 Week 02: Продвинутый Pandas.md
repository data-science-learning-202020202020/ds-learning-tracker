# Неделя 2: Продвинутый Pandas
🎯 Итог: Чистить, преобразовывать и объединять данные; работать с пропусками и датами

## 🗓️ День 1
### Обработка пропущенных значений
🔗 [Kaggle Learn: Data Cleaning - Lesson 1](https://www.kaggle.com/learn/data-cleaning)
✅ Завершение: Пройти упражнения по `dropna()`, `fillna()`

### Практика: заполнение пропусков
🔗 [Google Colab: Handling Missing Data](https://colab.research.google.com/github/WillKoehrsen/Data-Analysis-Notebooks/blob/master/Handling%20Missing%20Data.ipynb)
✅ Завершение: Применить 3 стратегии заполнения на датасете

### Самостоятельная задача: анализ пропусков
📝 Задание: Загрузить любой датасет с Kaggle, визуализировать пропуски
✅ Завершение: Код в `week2_day1_task.ipynb`

### Заметки
> 

## 🗓️ День 2
### Преобразование типов и работа со строками
🔗 [Pandas: Working with Text Data](https://pandas.pydata.org/docs/user_guide/text.html)
✅ Завершение: Применить `.str.lower()`, `.str.contains()`, `.str.extract()`

### Практика: парсинг дат
🔗 [Kaggle Notebook: Parsing Dates](https://www.kaggle.com/code/rtatman/data-cleaning-challenge-parsing-dates/)
✅ Завершение: Конвертировать строковые даты в datetime

### Самостоятельная задача: очистка текста
📝 Задание: Очистить колонку с названиями товаров (удалить спецсимволы, привести к нижнему регистру)
✅ Завершение: Код в `week2_day2_task.ipynb`

### Заметки
> 

## 🗓️ День 3
### Объединение таблиц: merge, concat, join
🔗 [Kaggle Learn: Pandas - Lesson 7](https://www.kaggle.com/learn/pandas)
✅ Завершение: Пройти упражнения по `merge()` с разными `how`

### Практика: соединение датасетов
🔗 [Google Colab: Merge Practice](https://colab.research.google.com/github/justmarkham/pandas-videos/blob/master/pandas_merging_concatenating.ipynb)
✅ Завершение: Объединить 3 таблицы по ключам

### Самостоятельная задача: E-commerce анализ
📝 Задание: Объединить таблицы заказов и клиентов, найти топ-5 покупателей
✅ Завершение: Код в `week2_day3_task.ipynb`

### Заметки
> 

## 🗓️ День 4
### Работа с группами: groupby + agg
🔗 [Kaggle Learn: Pandas - Lesson 3](https://www.kaggle.com/learn/pandas)
✅ Завершение: Пройти упражнения по агрегации

### Практика: кастомная агрегация
🔗 [Pandas: GroupBy Advanced](https://pandas.pydata.org/docs/user_guide/groupby.html)
✅ Завершение: Создать 3 кастомные агрегатные функции

### Самостоятельная задача: отчёт по продажам
📝 Задание: Сгруппировать данные по категории и месяцу, посчитать сумму и среднее
✅ Завершение: Таблица в `week2_day4_task.ipynb`

### Заметки
> 

## 🗓️ День 5
### Pivot tables и reshaping данных
🔗 [Kaggle Notebook: Pivot Tables](https://www.kaggle.com/code/alexisbcook/pivot-tables)
✅ Завершение: Создать сводную таблицу с 2 уровнями индексации

### Практика: melt и pivot
🔗 [Pandas: Reshaping and Pivot Tables](https://pandas.pydata.org/docs/user_guide/reshaping.html)
✅ Завершение: Преобразовать wide → long и обратно

### Самостоятельная задача: анализ временных рядов
📝 Задание: Преобразовать данные о продажах в формат для временного анализа
✅ Завершение: Код в `week2_day5_task.ipynb`

### Заметки
> 

## 🗓️ День 6 — Мини-проект
### Полный пайплайн очистки данных
🔗 [Dataset: FIFA 19 Player Stats](https://www.kaggle.com/datasets/karangadiya/fifa19)
📝 Задание:
1. Загрузить данные, оценить качество
2. Обработать пропуски, преобразовать типы
3. Создать 3 новых признака (например, "цена за рейтинг")
4. Сохранить очищенный датасет
✅ Завершение: Запушить `week2_project.ipynb` + `cleaned_data.csv`

- [ ] Проект выполнен, файлы запушены

## 🗓️ День 7 — Повторение
- [ ] Пройти квиз по Pandas
- [ ] Перечитать заметки
- [ ] Отдых
