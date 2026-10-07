# Тут начинается нормальный код, над которым я работал
# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30  # Стандартная рекомендация для поддержания водного баланса
ML_IN_LITER = 1000
TARGET_BMI = 21.75  # Значение середины нормального ИМТ


# Функция проверки ввода и преобразования в заданный тип данных
def get_number(prompt_message, type_func, min_val=None, max_val=None):
    """Функция проверки ввода и преобразования в заданный тип данных"""
    while True:
        user_input = input(prompt_message)
        # 1. Нормализация для float (запятая -> точка), иначе оставляем
        if type_func == float:
            normalized_input = user_input.replace(',', '.')
        else:
            normalized_input = user_input

        try:
            # 2. Проверяем число ли это, приводим к заданному типу данных
            value = type_func(normalized_input)

            # 3. Проверка диапазона (логика общая для обоих типов)
            if min_val is not None and value < min_val:
                print('❌ Слишком мало! Значение'
                      f' должно быть не меньше {min_val}.')
                continue

            if max_val is not None and value > max_val:
                print('❌ Слишком много! Значение'
                      f' должно быть не больше {max_val}.')
                continue

            return value

        except ValueError:
            # 4. Сообщение об ошибке
            if type_func == float:
                error_msg = ('Введите корректное число (можно c точкой'
                             ' или запятой, например: 1.75 или 1,75)')
            else:
                error_msg = 'Введите только целое число(без запятых и точек)'
            print(f'❌ Ошибка: {error_msg}.')


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
    # Разница между текущим ИМТ и рекомендованным
    bmi_difference = abs(current_bmi - TARGET_BMI)

    if bmi_difference <= 3.25:
        return 'У вас отличный вес, его не нужно корректировать'
    else:
        if weight_difference > 0:
            return ('Вам рекомендуется похудеть'
                    f' на {abs(weight_difference):.1f} кг.')
        else:
            return ('Вам рекомендуется набрать'
                    f' {abs(weight_difference):.1f} кг.')


# 1. Знакомство
user_name = input('Привет! Давайте начнем! Как вас зовут? ')
print(f'{user_name}, приятно познакомиться!')
user_age = get_number('Сколько вам полных лет? '
                      '(Укажите целое число): ', int, 14, 90)

# 2. Сбор данных
user_weight = get_number('Укажите пожалуйста ваш вес в кг '
                         '(Например: 96): ', float, 30, 200)
user_height = get_number('Укажите пожалуйста ваш рост в метрах '
                         '(Например: 1.98): ', float, 1, 2.5)

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
