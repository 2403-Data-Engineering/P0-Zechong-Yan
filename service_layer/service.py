import data_layer.models as models

# Professor Services
def add_professor(first_name, last_name, department, email): 
    models.add_professor(first_name, last_name, department, email)
    print("Professor added successfully!")

def list_professors():
    return models.list_professors()

# Student Services
def add_student(first_name, last_name, email, major, year):
    models.add_student(first_name, last_name, email, major, year)
    print("Student added successfully!")

def list_students():
    return models.list_students()

# Class Services
def add_class(class_name, professor_id, semester, max_students=30):
    models.add_class(class_name, professor_id, semester, max_students)
    print("Class added successfully!")

def list_classes():
    return models.list_classes()

# Enrollment Services
def enroll_student(student_id, class_id):
    models.enroll_student(student_id, class_id)

def list_enrollments():
    return models.list_enrollments()

# Update & Delete Services

# Professor
def update_professor(professor_id, first_name, last_name, department, email):
    models.update_professor(professor_id, first_name, last_name, department, email)
    print("Professor updated successfully!")

def delete_professor(professor_id):
    models.delete_professor(professor_id)
    print("Professor deleted successfully!")

# Student
def update_student(student_id, first_name, last_name, email, major, year):
    models.update_student(student_id, first_name, last_name, email, major, year)
    print("Student updated successfully!")

def delete_student(student_id):
    models.delete_student(student_id)
    print("Student deleted successfully!")

# Class
def update_class(class_id, class_name, professor_id, semester, max_students):
    models.update_class(class_id, class_name, professor_id, semester, max_students)
    print("Class updated successfully!")

def delete_class(class_id):
    models.delete_class(class_id)
    print("Class deleted successfully!")

# Enrollment
def delete_enrollment(enrollment_id):
    models.delete_enrollment(enrollment_id)
    print("Enrollment deleted successfully!")

# Update Enrollment Service
def update_enrollment(enrollment_id, new_class_id):
    models.update_enrollment(enrollment_id, new_class_id)

# DUMMY DATA
def show_sample_data():
    print("\n Sample Data:")
    print("   Professors : Alice Smith, Bob Johnson")
    print("   Students   : Emma Davis, Liam Wilson")
    print("   Classes    : Introduction to Programming, Calculus I")