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

cursor.execute("""SELECT *
                FROM students
                WHERE id=%s""", (student_id,))
print(cursor.fetchall())


"""Создание книги, бронирование ее за студентом и проверка"""
cursor.executemany("INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)",
                   [('My New_journal', student_id), ('New_diary', student_id)])

cursor.execute("""SELECT *
                FROM books
                WHERE taken_by_student_id=%s""", (student_id,))
print(cursor.fetchall())


"""Создание группы, вступление в нее студента и проверка"""
cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)",
               ('New_mems', '24/04/2026', '30/04/2026'))

group_id = cursor.lastrowid
cursor.execute("UPDATE students SET group_id = %s WHERE id = %s", (group_id, student_id))

cursor.execute("SELECT * FROM `groups` WHERE id = %s", (group_id,))
print(cursor.fetchall())


"""Создание предметов и проверка"""
subjects = [('Новый Ежедневный мем',), ('Супер новый Ежедневный мем',)]
subject_id = []
for i in subjects:
    cursor.execute("INSERT INTO subjects (title) VALUES (%s)", i)
    subject_id.append(cursor.lastrowid)
subject1, subject2 = subject_id

cursor.execute("SELECT * FROM subjects WHERE id IN (%s, %s)", (subject1, subject2))
print(cursor.fetchall())


"Создание занятий для предметов и проверка"
lessons = [("Новая тренировка", subject1), ("Супер новая тренировка", subject2)]
lesson_id = []
for i in lessons:
    cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", i)
    lesson_id.append(cursor.lastrowid)
lesson_id1, lesson_id2 = lesson_id

cursor.execute("SELECT * FROM lessons WHERE id IN (%s, %s)", (lesson_id1, lesson_id2))
print(cursor.fetchall())


"Проставление оценки за занятие и проверка"
cursor.executemany("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
                   [(5, lesson_id1, student_id), (5, lesson_id2, student_id)])

cursor.execute("SELECT * FROM marks WHERE student_id = %s AND lesson_id IN (%s, %s)",
               (student_id, lesson_id1, lesson_id2))
print(cursor.fetchall())


"Получите информацию из базы данных"

"Все оценки студента"
cursor.execute("SELECT * FROM marks WHERE student_id = %s", (student_id,))
print(cursor.fetchall())


"Все книги, которые находятся у студента"
cursor.execute("SELECT * FROM books WHERE taken_by_student_id = %s", (student_id,))
print(cursor.fetchall())


"Для вашего студента выведите всё, что о нем есть в базе"
cursor.execute("""SELECT
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
      s.id = %s""", (student_id,))
print(cursor.fetchall())
# db.commit()

db.close()
