import sqlite3

# Подключаемся к базе данных
conn = sqlite3.connect('бухгалтерия.db')
cursor = conn.cursor()

# Создаем таблицу для доходов
cursor.execute('''
    CREATE TABLE IF NOT EXISTS доходы (
        id INTEGER PRIMARY KEY,
        дата DATE,
        источник TEXT,
        сумма INT
    )
''')

# Создаем таблицу для счетов
cursor.execute('''
    CREATE TABLE IF NOT EXISTS счета (
        id INTEGER PRIMARY KEY,
        номер TEXT,
        баланс INT
    )
''')

# Вставляем тестовые данные для доходов
cursor.execute("INSERT INTO доходы (дата, источник, сумма) VALUES (?, ?, ?)",
               ('2023-09-20', 'Зарплата', 2500.00))

# Вставляем тестовые данные для счетов
cursor.execute("INSERT INTO счета (номер, баланс) VALUES (?, ?)", ('1234567890', 5000.00))

# Сохраняем изменения
conn.commit()

# Закрываем соединение
conn.close()
