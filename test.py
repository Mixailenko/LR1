import sqlite3

def create_tables():
    conn = sqlite3.connect('бухгалтерия.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS доходы (
            id INTEGER PRIMARY KEY,
            дата DATE,
            источник TEXT,
            сумма REAL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS счета (
            id INTEGER PRIMARY KEY,
            номер TEXT,
            баланс REAL
        )
    ''')

    conn.commit()
    conn.close()

def insert_test_data():
    conn = sqlite3.connect('бухгалтерия.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO доходы (дата, источник, сумма) VALUES (?, ?, ?)",
                   ('2023-09-20', 'Зарплата', 2500.00))

    cursor.execute("INSERT INTO счета (номер, баланс) VALUES (?, ?)", ('1234567890', 5000.00))

    conn.commit()
    conn.close()

def select_data(table_name):
    conn = sqlite3.connect('бухгалтерия.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

def update_data(table_name, column_name, new_value, row_id):
    conn = sqlite3.connect('бухгалтерия.db')
    cursor = conn.cursor()

    cursor.execute(f"UPDATE {table_name} SET {column_name} = ? WHERE id = ?", (new_value, row_id))

    conn.commit()
    conn.close()

def delete_data(table_name, row_id):
    conn = sqlite3.connect('бухгалтерия.db')
    cursor = conn.cursor()

    cursor.execute(f"DELETE FROM {table_name} WHERE id = ?", (row_id,))

    conn.commit()
    conn.close()

# Создаем таблицы (если они еще не созданы)
create_tables()

# Вставляем тестовые данные
insert_test_data()

# Извлекаем и выводим данные из таблицы "доходы"
print("Данные из таблицы 'доходы':")
select_data('доходы')

# Обновляем значение суммы в таблице "доходы" для записи с id=1
update_data('доходы', 'сумма', 3000.00, 1)

# Извлекаем и выводим обновленные данные из таблицы "доходы"
print("\nОбновленные данные из таблицы 'доходы':")
select_data('доходы')

# Удаляем запись с id=1 из таблицы "счета"
delete_data('счета', 1)

# Извлекаем и выводим данные из таблицы "счета" после удаления записи
print("\nДанные из таблицы 'счета' после удаления записи:")
select_data('счета')