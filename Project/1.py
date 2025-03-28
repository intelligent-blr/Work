try:
                                # Проверка существования email в базе
                                if fetch_user_email(new_value):
                                    print("Ошибка: этот email уже используется.")
                                    continue
                            except ValueError:
                                pass  # Если email не найден, продолжаем