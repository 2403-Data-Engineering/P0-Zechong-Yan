import mysql.connector

DB_CONFIG = {
    "host": "revature-2403.cs1m8i0ouruo.us-east-1.rds.amazonaws.com",
    "user": "admin",
    "password": "revature",                
    "database": "zechongyanP0"
}
# Connection method to the database
def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def init_db():
    print("Initializing database...")

    conn = get_connection()
    # cursor object talk to the database
    cursor = conn.cursor()

    # Read and execute schema.sql
    with open("schema.sql", "r", encoding="utf-8") as f:
        schema = f.read()

    # Reading from schema.sql
    statements = []
    for stmt in schema.split(';'):
        cleaned = stmt.strip()
        if cleaned:                    # if the statement is not empty
            statements.append(cleaned)

    for statement in statements:
        try:
            cursor.execute(statement)
        except mysql.connector.Error as err: # check if the table already exist
            if "already exists" not in str(err).lower(): # print the error message
                print(f"   Warning: {err}")

    conn.commit()
    conn.close()
    print("Schema loaded successfully from schema.sql!")
    print("All tables and relationships are ready in database 'zechongyanP0'.")

# CRUD Functions
def add_professor(first_name, last_name, department, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO professors (first_name, last_name, department, email)
                      VALUES (%s, %s, %s, %s)""", (first_name, last_name, department, email))
    conn.commit()
    conn.close()

def list_professors():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM professors")
    return cursor.fetchall()

def add_student(first_name, last_name, email, major, year):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO students (first_name, last_name, email, major, year)
                      VALUES (%s, %s, %s, %s, %s)""", (first_name, last_name, email, major, year))
    conn.commit()
    conn.close()

def list_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()

def add_class(class_name, professor_id, semester, max_students=30):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO classes (class_name, professor_id, semester, max_students)
                      VALUES (%s, %s, %s, %s)""", (class_name, professor_id, semester, max_students))
    conn.commit()
    conn.close()

def list_classes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT c.class_id, c.class_name, 
                             CONCAT(p.first_name, ' ', p.last_name) as professor, 
                             c.semester, c.max_students 
                      FROM classes c LEFT JOIN professors p ON c.professor_id = p.professor_id""")
    return cursor.fetchall()

def enroll_student(student_id, class_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO enrollments (student_id, class_id) VALUES (%s, %s)", (student_id, class_id))
        conn.commit()
        print("Student enrolled successfully.")
    except:
        print("Student is already enrolled in this class.")
    conn.close()

def list_enrollments():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT e.enrollment_id, CONCAT(s.first_name, ' ', s.last_name) as student, 
                             c.class_name, c.semester 
                      FROM enrollments e 
                      JOIN students s ON e.student_id = s.student_id 
                      JOIN classes c ON e.class_id = c.class_id""")
    return cursor.fetchall()

# Update and Delete 
def update_professor(professor_id, first_name, last_name, department, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""UPDATE professors 
                      SET first_name=%s, last_name=%s, department=%s, email=%s 
                      WHERE professor_id=%s""", 
                   (first_name, last_name, department, email, professor_id))
    conn.commit()
    conn.close()

def delete_professor(professor_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM professors WHERE professor_id = %s", (professor_id,))
    conn.commit()
    conn.close()

def update_student(student_id, first_name, last_name, email, major, year):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""UPDATE students 
                      SET first_name=%s, last_name=%s, email=%s, major=%s, year=%s 
                      WHERE student_id=%s""", 
                   (first_name, last_name, email, major, year, student_id))
    conn.commit()
    conn.close()

def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    conn.commit()
    conn.close()

def update_class(class_id, class_name, professor_id, semester, max_students):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""UPDATE classes 
                      SET class_name=%s, professor_id=%s, semester=%s, max_students=%s 
                      WHERE class_id=%s""", 
                   (class_name, professor_id, semester, max_students, class_id))
    conn.commit()
    conn.close()

def delete_class(class_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM classes WHERE class_id = %s", (class_id,))
    conn.commit()
    conn.close()

# Update Enrollment (change class for a student)
def update_enrollment(enrollment_id, new_class_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""UPDATE enrollments 
                          SET class_id = %s 
                          WHERE enrollment_id = %s""", 
                       (new_class_id, enrollment_id))
        conn.commit()
        print("Enrollment updated successfully!")
    except mysql.connector.Error as err:
        print(f"Error updating enrollment: {err}")
    finally:
        conn.close()

def delete_enrollment(enrollment_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM enrollments WHERE enrollment_id = %s", (enrollment_id,))
    conn.commit()
    conn.close()

