import mysql.connector as mysql

""" Подключение к БД"""
db = mysql.connect(
    user='st-onl',
    password='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

"""Создание студента и проверка"""
cursor.execute("INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)",
               ('Борис', 'Лапкин', None))
student_id = cursor.lastrowid

cursor.execute(f"""SELECT *
                FROM students
                WHERE id='{student_id}'
                """)
print(cursor.fetchall())


"""Создание книги, бронирование ее за студентом и проверка"""
cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)", ('My New_journal', student_id))
cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)", ('New_diary', student_id))

cursor.execute(f"""
                SELECT *
                FROM books
                WHERE taken_by_student_id='{student_id}'
                """)
print(cursor.fetchall())


"""Создание группы, вступление в нее студента и проверка"""
cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)",
               ('New_mems', '24/04/2026', '30/04/2026'))

group_id = cursor.lastrowid
cursor.execute(f"UPDATE students SET group_id = {group_id} WHERE id = {student_id}")

cursor.execute(f"SELECT * FROM `groups` WHERE id = '{group_id}'")
print(cursor.fetchall())


"""Создание предметов и проверка"""
cursor.execute("INSERT INTO subjects (title) VALUES (%s)",
               ('Новый Ежедневный мем',))
subject_1 = cursor.lastrowid
cursor.execute("INSERT INTO subjects (title) VALUES (%s)",
               ('Супер новый Ежедневный мем',))
subject_2 = cursor.lastrowid

cursor.execute(f"SELECT * FROM subjects WHERE id IN ({subject_1}, {subject_2})")
print(cursor.fetchall())


"Создание занятий для предметов и проверка"
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)",
               ("Новая тренировка", subject_1))
lesson_id1 = cursor.lastrowid

cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)",
               ("Супер новая тренировка", subject_2))
lesson_id2 = cursor.lastrowid

cursor.execute(f"SELECT * FROM lessons WHERE id IN ({lesson_id1}, {lesson_id2})")
print(cursor.fetchall())


"Проставление оценки за занятие и проверка"
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
               (5, lesson_id1, student_id))
mark_id1 = cursor.lastrowid

cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
               (5, lesson_id2, student_id))
mark_id2 = cursor.lastrowid

cursor.execute(f"SELECT * FROM marks WHERE id IN ({mark_id1}, {mark_id2})")
print(cursor.fetchall())


"Получите информацию из базы данных"

"Все оценки студента"
cursor.execute(f"SELECT * FROM marks WHERE student_id={student_id}")
print(cursor.fetchall())


"Все книги, которые находятся у студента"
cursor.execute(f"SELECT * FROM books WHERE taken_by_student_id ={student_id}")
print(cursor.fetchall())


"Для вашего студента выведите всё, что о нем есть в базе"
cursor.execute(f"""SELECT
      g.title as Название_группы,
      CONCAT(s.name, ' ', s.second_name) as Студент,
      b.title as Книга_из_библиотеки,
      s2.title Предмет,
      l.title as Занятие,
      m.value as Оценка
    FROM
      students as s
      INNER JOIN books as b ON s.id = b.taken_by_student_id
      INNER JOIN marks m ON m.student_id = s.id
      INNER JOIN `groups` g ON s.group_id = g.id
      INNER JOIN lessons l ON m.lesson_id = l.id
      INNER JOIN subjects s2 ON l.subject_id = s2.id
    WHERE
      s.id = {student_id}""")
print(cursor.fetchall())
db.commit()

db.close()
