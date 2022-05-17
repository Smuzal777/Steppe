# Steppe

### Степь. Расчёт прибыли от культур.✨
-------------------------------------
### Технологии
**[Python 3.10](https://www.python.org/)**
**[JSON](https://www.json.org/)**
**[PyCharm 2022.1.1](https://www.jetbrains.com/ru-ru/pycharm/)**
**[prettytable 3.3.0](https://pypi.org/project/prettytable/)**
-----------------------------------------
### Описание проекта:
Проект позволяет расчитать максимальную прибыль от продажи культур
---------------------------
Данные хранятся в формате JSON

Входные данные:
```

{
    "name": "string",
    "price": number,
    "usage": number,
    "farming_cost": number,
    "storage_cost": number,
    "output": number,
    "income": number,
    "humidity": number,
    "temperature": number,
    "humidity_response": number,
    "temperature_response": number
}

    name - название культуры
    price - цена семян за тонну
    usage - расход семян (кг/га)
    farming_cost - затраты на выращивание (руб/га)
    storage_cost - затраты на хранение (руб/ц)
    output - урожайность (ц/га)
    income - стоимость урожая (руб/т)
    humidity - оптимальная влажность
    temperature - оптимальная температура
    humidity_response - снижение урожайности при отклонении условий по влажности
    temperature_response - снижение урожайности при отклонении условий по температуре

```

Выходные данные можно сохранить в формате JSON:
```

{
    "name": "string",
    "income_calculated": number,
    "plan_income": number,
    "farm_cost": number,
    "storage_cost": number
}

    name - название культуры
    income_calculated - прибыль от культуры (руб)
    plan_income - доход от продажи (руб)
    farm_cost - затраты на посевы и выращивание (руб)
    storage_cost - затраты на хранение (руб)

```
