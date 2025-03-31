else:
    while True:
        # Проверка имени
        first_name = input("Необходимо выполнить регистрацию. "
                           "Введите, пожалуйста, ваше имя: ").title()
        if not first_name:
            print("Данное поле не может быть пустым.")
            continue  # Если имя пустое, запрашиваем снова

        # Проверка фамилии
        last_name = input("Введите вашу фамилию: ").title()
        if not last_name:
            print("Данное поле не может быть пустым.")
            continue  # Если фамилия пустая, запрашиваем снова

        # Проверка email
        while True:
            email = input("Последним шагом необходимо ввести email: ").strip()

            if not email:
                print("Ошибка: Email не может быть пустым.")
                continue  # Если email пустой, запрашиваем снова

            email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            if not re.match(email_pattern, email):
                print("Ошибка: Некорректный email. Попробуйте снова.")
                continue  # Заставляем ввести корректный email

            if fetch_user_email(email):
                print("Данный email уже зарегистрирован. Пожалуйста, введите другой.")
                choice = input("Хотите ввести другой email? (да/нет): ").strip().lower()
                if choice != "да":
                    print("К сожалению, вы не выполнили регистрацию.")
                    exit()
            else:
                break  # Email прошел все проверки, можно выходить из цикла

        # Если все данные введены корректно, добавляем пользователя
        add_user_to_database(input_login, first_name, last_name, email)
        print(f"Регистрация прошла успешно! Добро пожаловать {first_name} {last_name}!")
        break  # Прерываем основной цикл, так как регистрация завершена
