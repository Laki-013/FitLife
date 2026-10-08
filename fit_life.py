# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30  # Стандартная рекомендация для поддержания водного баланса
ML_IN_LITER = 1000
TARGET_BMI = 21.75  # Значение середины нормального ИМТ


# Функция интерпритации ИМТ
def get_bmi_category(bmi):
    """Описание ИМТ"""
    # В соответствии с рекомендациями ВОЗ разработана интерпретация ИМТ
    if bmi < 16:
        return 'выраженный дефицит массы тела'
    elif 16 <= bmi < 18.5:
        return 'недостаточная масса тела (дефицит)'
    elif 18.5 <= bmi < 25:
        return 'в норме! Так держать!'
    elif 25 <= bmi < 30:
        return 'избыточная масса тела (предожирение)'
    elif 30 <= bmi < 35:
        return 'ожирение I степени'
    elif 35 <= bmi < 40:
        return 'ожирение II степени'
    elif 40 < bmi:
        return 'ожирение III степени'


# Функция подсчета разницы до рекомендованого веса
def calculate_weight_goal(user_weight, user_height, current_bmi):
    """Функция подсчета разницы до рекомендованого веса"""
    # Рекомедованный вес по ВОЗ
    weight_goal = TARGET_BMI * (user_height ** 2)
    # Разница между текущим весом и рекомендованным
    weight_difference = user_weight - weight_goal
    absolut_weight_difference = abs(weight_difference)
    # Разница между текущим ИМТ и рекомендованным
    bmi_difference = abs(current_bmi - TARGET_BMI)

    if bmi_difference <= 3.25:
        return 'У вас отличный вес, его не нужно корректировать'
    else:
        if weight_difference > 0:
            return ('Вам рекомендуется похудеть'
                    f' на {absolut_weight_difference:.1f} кг.')
        else:
            return ('Вам рекомендуется набрать'
                    f' {absolut_weight_difference:.1f} кг.')


# 1. Знакомство
user_name = input('Привет! Давайте начнем! Как вас зовут? ')
print(f'{user_name}, приятно познакомиться!')

# Получение возраста пользователя через цикл (функции не проходят pytest)
while True:
    user_age = input('Сколько вам полных лет? (Укажите целое число): ')
    try:
        user_age = int(user_age)

        # Проверка диапазона
        if user_age < 14:
            print('❌ Слишком мало! Возраст должен быть не меньше 14 лет.')
            continue
        if user_age > 90:
            print('❌ Слишком много! Возраст должен быть не больше 90 лет.')
            continue
        break

    except ValueError:
        print('❌ Ошибка: нужно ввести целое число (только цифры).')

# 2. Сбор данных
# Получение веса пользователя через цикл (функции не проходят pytest)
while True:
    user_weight = input('Укажите пожалуйста ваш вес в кг (Например: 96): ')
    normalized_weight = user_weight.replace(',', '.')

    try:
        user_weight = float(normalized_weight)

        # Проверка диапазона
        if user_weight < 30:
            print('❌ Слишком мало! Вес должен быть не меньше 30 кг.')
            continue
        if user_weight > 200:
            print('❌ Слишком много! Вес должен быть не больше 200 кг.')
            continue
        break

    except ValueError:
        print('❌ Ошибка: пожалуйста, введите корректное'
              ' число (можно с точкой или запятой).')
# Получение роста пользователя через цикл (функции не проходят pytest)
while True:
    user_height = input('Укажите пожалуйста ваш рост в метрах'
                        ' (Например: 1.98): ')
    normalized_user_height = user_height.replace(',', '.')

    try:
        user_height = float(normalized_user_height)

        # Проверка диапазона
        if user_height < 1.0:
            print('❌ Слишком мало! Рост должен быть не меньше 1 метра.')
            continue
        if user_height > 2.5:
            print('❌ Слишком много! Рост должен быть не больше 2.5 метров.')
            continue
        break

    except ValueError:
        print('❌ Ошибка: пожалуйста, введите корректное'
              ' число (можно с точкой или запятой).')


# 3. Логика расчетов
# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = user_weight / (user_height ** 2)
bmi_description = get_bmi_category(bmi)  # Описание ИМТ по ВОЗ
weight_recommendations = calculate_weight_goal(user_weight, user_height, bmi)

# Подсчет воды: (вес * 30 мл) / 1000 (для удобства переводим в литры)
water_needed_l = (user_weight * WATER_PER_KG) / ML_IN_LITER

# 4. Вывод красивого результата
print()
print(f'{user_name}, теперь я многое знаю o вас!')
print()
print(f'Ваш возраст: {user_age}')
print()
print(f'Ваш ИМТ (индекс массы тела): {bmi:.1f}')
print()
print(f'По данным BO3 ваш ИМТ можно интерпритировать как: {bmi_description}')
print()
print(weight_recommendations)
print()
print(' ⚠️    Помните: ИМТ — это лишь ориентир. Для точной оценки состояния'
      ' здоровья проконсультируйтесь c врачом')
print()
print(f'Рекомендуемое количество воды в день {water_needed_l:.2f} л.')
print()
print('Расчет окончен. Будьте здоровы!')
