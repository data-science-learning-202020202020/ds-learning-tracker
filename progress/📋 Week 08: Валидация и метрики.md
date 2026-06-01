# Неделя 8: Валидация моделей и выбор метрик
🎯 Итог: Правильно валидировать модели; выбирать метрики под бизнес-задачу

## 🗓️ День 1
### Кросс-валидация: Stratified K-Fold
🔗 [Scikit-learn: cross_val_score](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html)
✅ Завершение: Применить `StratifiedKFold` к классификации

### Практика: временная валидация для time series
🔗 [Kaggle Notebook: Time Series CV](https://www.kaggle.com/code/residentmario/time-series-cross-validation)
✅ Завершение: Реализовать `TimeSeriesSplit`

### Самостоятельная задача: выбор стратегии валидации
📝 Задание: Обосновать выбор CV-стратегии для своего датасета
✅ Завершение: Текст + код в `week8_day1_task.ipynb`

### Заметки
> 

## 🗓️ День 2
### Метрики классификации: precision, recall, F1, ROC-AUC
🔗 [Scikit-learn: Classification Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics)
✅ Завершение: Рассчитать все метрики для одной модели

### Практика: выбор метрики под задачу
🔗 [Kaggle Discussion: Choosing Metrics](https://www.kaggle.com/general/31877)
✅ Завершение: Ответить: когда максимизировать recall, а когда precision?

### Самостоятельная задача: метрики для оттока
📝 Задание: Выбрать и обосновать главную метрику для задачи оттока
✅ Завершение: Обоснование в `week8_day2_task.ipynb`

### Заметки
> 

## 🗓️ День 3
### Кривые обучения и валидации
🔗 [Scikit-learn: learning_curve](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.learning_curve.html)
✅ Завершение: Построить learning curve для своей модели

### Практика: диагностика bias/variance
🔗 [Kaggle Notebook: Bias-Variance Tradeoff](https://www.kaggle.com/code/residentmario/bias-variance-tradeoff)
✅ Завершение: Определить, переобучена или недообучена модель

### Самостоятельная задача: улучшение модели
📝 Задание: Предложить 2 способа улучшить модель на основе кривых
✅ Завершение: План в `week8_day3_task.ipynb`

### Заметки
> 

## 🗓️ День 4
### Калибровка вероятностей
🔗 [Scikit-learn: CalibratedClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html)
✅ Завершение: Откалибровать модель, сравнить reliability curve

### Практика: когда калибровка критична
🔗 [Kaggle Discussion: Probability Calibration](https://www.kaggle.com/general/32075)
✅ Завершение: Ответить: в каких задачах важны точные вероятности?

### Самостоятельная задача: калибровка для скоринга
📝 Задание: Откалибровать модель для кредитного скоринга
✅ Завершение: График до/после в `week8_day4_task.ipynb`

### Заметки
> 

## 🗓️ День 5
### Сравнение моделей: статистические тесты
🔗 [MLxtend: paired_ttest_5x2cv](https://rasbt.github.io/mlxtend/user_guide/evaluate/paired_ttest_5x2cv/)
✅ Завершение: Сравнить 2 модели через статистический тест

### Практика: выбор лучшей модели
🔗 [Kaggle Notebook: Model Comparison](https://www.kaggle.com/code/residentmario/comparing-classifiers)
✅ Завершение: Обосновать выбор финальной модели

### Самостоятельная задача: финальный выбор
📝 Задание: Сравнить 3 модели, выбрать лучшую с обоснованием
✅ Завершение: Отчёт в `week8_day5_task.ipynb`

### Заметки
> 

## 🗓️ День 6 — Мини-проект
### Полный отчёт по валидации модели
🔗 [Dataset: Choose your own from Kaggle]
📝 Задание:
1. Выбрать задачу и датасет
2. Обучить 2-3 модели
3. Провести корректную валидацию
4. Сравнить по бизнес-метрике, выбрать лучшую
5. Подготовить 1-страничный отчёт для стейкхолдера
✅ Завершение: Запушить `week8_project.ipynb` + `report.md`

- [ ] Проект выполнен, отчёт готов

## 🗓️ День 7 — Повторение
- [ ] Пройти квиз по валидации
- [ ] Сохранить отчёт в портфолио
- [ ] Отдых
