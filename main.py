import service_layer.service as services
import report
from datetime import datetime
import data_layer.models as models

def print_header(title):
    print("\n" + "="*60)
    print(f"College Course Registration System - {title}")
    print("="*60)

# Console menu
def main_menu():
    while True:
        print_header("Main Menu")
        print("1.  Add Professor")
        print("2.  List Professors")
        print("3.  Update Professor")
        print("4.  Delete Professor")
        print("5.  Add Student")
        print("6.  List Students")
        print("7.  Update Student")
        print("8.  Delete Student")
        print("9.  Add Class")
        print("10. List Classes")
        print("11. Update Class")
        print("12. Delete Class")
        print("13. Enroll Student in Class")
        print("14. List Enrollments")
        print("15. Delete Enrollment")
        print("16. Generate Reports")
        print("17, Unpdate Enrollment(change a class)")
        #print("18. Show Sample Data")
        print("0.  Exit")
        
        choice = input("\nEnter your choice: ").strip()

        # Professor
        if choice == "1":
            first = input("First Name: ")
            last = input("Last Name: ")
            dept = input("Department: ")
            email = input("Email: ")
            services.add_professor(first, last, dept, email)

        elif choice == "2": 
            print("\n All Professors:")

            professors = services.list_professors()  # Get all professors

            # Loop through the tuple
            for p in professors:
                professor_id = p[0]
                first_name = p[1]
                last_name = p[2]
                department = p[3]
                email = p[4]
        
                print(f"ID: {professor_id:<4} | {first_name} {last_name} | {department} | {email}")

        elif choice == "3":
            try:
                pid = int(input("Professor ID to update: "))
                first = input("New First Name: ")
                last = input("New Last Name: ")
                dept = input("New Department: ")
                email = input("New Email: ")
                services.update_professor(pid, first, last, dept, email)
            except ValueError: 
                print("Invalid ID")

        elif choice == "4":
            try:
                pid = int(input("Professor ID to delete: "))
                confirm = input(f"Delete Professor ID {pid}? (y/n): ").lower()
                if confirm == 'y':
                    services.delete_professor(pid)
                else:
                    print("Cancelled.")
            except ValueError:
                print(" Invalid ID")

        # Student
        elif choice == "5":
            first = input("First Name: ")
            last = input("Last Name: ")
            email = input("Email: ")
            major = input("Major: ")
            year = input("Year: ")
            services.add_student(first, last, email, major, year)

        elif choice == "6":
            print("\n All Students:")
    
            students = services.list_students()        # Get all students first
    
            for s in students:
                student_id = s[0]
                first_name = s[1]
                last_name = s[2]
                email = s[3]
                major = s[4]
                year = s[5]
        
                print(f"ID: {student_id:<4} | {first_name} {last_name} | Email: {email} | Major: {major} | Year: {year}")

        elif choice == "7":
            try:
                sid = int(input("Student ID to update: "))
                first = input("New First Name: ")
                last = input("New Last Name: ")
                email = input("New Email: ")
                major = input("New Major: ")
                year = input("New Year: ")
                services.update_student(sid, first, last, email, major, year)
            except ValueError:
                print("Invalid ID")

        elif choice == "8":
            try:
                sid = int(input("Student ID to delete: "))
                confirm = input(f"Delete Student ID {sid}? (y/n): ").lower()
                if confirm == 'y':
                    services.delete_student(sid)
                else:
                    print("Cancelled.")
            except ValueError:
                print(" Invalid ID")

        # Class
        elif choice == "9":
            name = input("Class Name: ")
            prof_id = int(input("Professor ID: "))
            semester = input("Semester: ")
            max_stu = int(input("Max Students [30]: ") or 30)
            services.add_class(name, prof_id, semester, max_stu)

        elif choice == "10":
            print("\n All Classes:")
    
            classes = services.list_classes()        # Get all classes first
    
            for c in classes:
                class_id = c[0]
                class_name = c[1]
                professor = c[2]
                semester = c[3]
                max_students = c[4]
        
                print(f"ID: {class_id:<4} | {class_name} | Professor: {professor} | Semester: {semester} | Max: {max_students}")

        elif choice == "11":
            try:
                cid = int(input("Class ID to update: "))
                name = input("New Class Name: ")
                prof_id = int(input("New Professor ID: "))
                semester = input("New Semester: ")
                max_stu = int(input("New Max Students: ") or 30)
                services.update_class(cid, name, prof_id, semester, max_stu)
            except ValueError:
                print(" Invalid ID")

        elif choice == "12":
            try:
                cid = int(input("Class ID to delete: "))
                confirm = input(f"Delete Class ID {cid}? (y/n): ").lower()
                if confirm == 'y':
                    services.delete_class(cid)
                else:
                    print("Cancelled.")
            except ValueError:
                print(" Invalid ID")

        # Enrollment
        elif choice == "13":
            try:
                sid = int(input("Student ID: "))
                cid = int(input("Class ID: "))
                services.enroll_student(sid, cid)
            except ValueError:
                print(" Invalid IDs")

        elif choice == "14":
            print("\n All Enrollments:")
    
            enrollments = services.list_enrollments()        # Get all enrollments first
    
            for e in enrollments:
                enrollment_id = e[0]
                student_name = e[1]
                class_name = e[2]
                semester = e[3]
        
                print(f"ID: {enrollment_id:<4} | {student_name} → {class_name} ({semester})")

        elif choice == "15":
            try:
                eid = int(input("Enrollment ID to delete: "))
                confirm = input(f"Delete Enrollment ID {eid}? (y/n): ").lower()
                if confirm == 'y':
                    services.delete_enrollment(eid)
                else:
                    print("Cancelled.")
            except ValueError:
                print(" Invalid ID")

        elif choice == "16":
            report.generate_reports()

        elif choice == "17":
            try:
                eid = int(input("Enrollment ID to update: "))
                new_cid = int(input("New Class ID: "))
                services.update_enrollment(eid, new_cid)
            except ValueError:
                print(" Invalid IDs")
        
        elif choice == "18":
            services.show_sample_data()

        elif choice == "0":
            print(f"\n Goodbye! Ended at {datetime.now().strftime('%Y-%m-%d %H:%M')}")
            break

        else:
            print(" Invalid choice.")

if __name__ == "__main__":
    print(" Starting College Course Registration System...\n")
    try:
        models.init_db()
        main_menu()
    except Exception as e:
        print(f" Error: {e}")
        print(" Check MySQL Connection in data_layer/models.py")