# Проект FitLife - MVP версия 0.9 !!!ВЕРСИЯ ДЛЯ ПРОХОЖДЕНИЯ PYTEST!!!
# Прошу посмотреть файл fit_life_work_version.py
# 1. Знакомство
user_name = input('Введите имя: ')
user_age = int(input('Введите возраст: '))

# 2. Сбор данных
user_weight = (float(input('Введите вес: ')))
user_height = (float(input('Введите рост: ')))

# 3. Логика расчетов
bmi = user_weight / user_height ** 2

# Подсчет воды: вес * 30 мл / 1000
water_needed = user_weight * 30 / 1000

# 4. Вывод красивого результата
print(f'Привет {user_name}')
print(f'твой возраст : {user_age}')
print(f'твой ИМТ : {bmi:.1f}')
print(f'норма воды : {water_needed}')
print("Расчет окончен. Будьте здоровы!")
