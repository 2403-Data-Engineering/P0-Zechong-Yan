
-- Drop tables in reverse order to avoid foreign key issues
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS professors;

-- Professors
CREATE TABLE professors (
    professor_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE
);

-- Students
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE,
    major VARCHAR(100),
    year INT
);

-- Classes (references Professor)
CREATE TABLE classes (
    class_id INT AUTO_INCREMENT PRIMARY KEY,
    class_name VARCHAR(200) NOT NULL,
    professor_id INT,
    semester VARCHAR(50) NOT NULL,
    max_students INT DEFAULT 30,
    FOREIGN KEY (professor_id) REFERENCES professors(professor_id)
);

-- Enrollments (Many-to-Many between Students and Classes)
CREATE TABLE enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    class_id INT,
    enrollment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (class_id) REFERENCES classes(class_id),
    UNIQUE(student_id, class_id)
);

"""
-- Dummy Data
INSERT IGNORE INTO professors (first_name, last_name, department, email) VALUES 
('Alice', 'Smith', 'Computer Science', 'alice.smith@university.edu'),
('Bob', 'Johnson', 'Mathematics', 'bob.johnson@university.edu');

INSERT IGNORE INTO students (first_name, last_name, email, major, year) VALUES 
('Emma', 'Davis', 'emma.davis@student.edu', 'Computer Science', 2),
('Liam', 'Wilson', 'liam.wilson@student.edu', 'Mathematics', 3);

INSERT IGNORE INTO classes (class_name, professor_id, semester, max_students) VALUES 
('Introduction to Programming', 1, 'Fall 2026', 25),
('Calculus I', 2, 'Fall 2026', 30);

INSERT IGNORE INTO enrollments (student_id, class_id) VALUES 
(1, 1),
(2, 2);
"""