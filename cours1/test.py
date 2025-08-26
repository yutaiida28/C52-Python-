#!/usr/bin/env python3
# Student Management System
# A comprehensive system to manage students, courses, and grades

import json
import datetime
from typing import List, Dict, Optional

# Global configuration
DEBUG = True
VERSION = "1.0.0"
MAX_STUDENTS = 1000

class Student:
    def __init__(self, student_id: int, name: str, email: str, age: int):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.age = age
        self.courses = []
        self.grades = {}
        self.enrollment_date = datetime.datetime.now()
    
    def add_course(self, course_name: str):
        if course_name not in self.courses:
            self.courses.append(course_name)
            self.grades[course_name] = []
        return True
    
    def add_grade(self, course_name: str, grade: float):
        if course_name in self.courses:
            if 0 <= grade <= 100:
                self.grades[course_name].append(grade)
                return True
        return False
    
    def get_average_grade(self, course_name: str = None):
        if course_name:
            if course_name in self.grades and len(self.grades[course_name]) > 0:
                return sum(self.grades[course_name]) / len(self.grades[course_name])
            return 0.0
        
        # Overall average
        total_grades = []
        for course_grades in self.grades.values():
            total_grades.extend(course_grades)
        
        if len(total_grades) > 0:
            return sum(total_grades) / len(total_grades)
        return 0.0
    
    def __str__(self):
        return f"Student({self.student_id}, {self.name}, {self.email})"
    
    def __repr__(self):
        return self.__str__()

class Course:
    def __init__(self, course_code: str, name: str, credits: int, instructor: str):
        self.course_code = course_code
        self.name = name
        self.credits = credits
        self.instructor = instructor
        self.enrolled_students = []
        self.max_capacity = 50
    
    def enroll_student(self, student_id: int):
        if len(self.enrolled_students) < self.max_capacity:
            if student_id not in self.enrolled_students:
                self.enrolled_students.append(student_id)
                return True
        return False
    
    def remove_student(self, student_id: int):
        if student_id in self.enrolled_students:
            self.enrolled_students.remove(student_id)
            return True
        return False
    
    def get_enrollment_count(self):
        return len(self.enrolled_students)
    
    def is_full(self):
        return len(self.enrolled_students) >= self.max_capacity
    
    def __str__(self):
        return f"Course({self.course_code}, {self.name}, {self.instructor})"

class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.next_student_id = 1
        
    def add_student(self, name: str, email: str, age: int):
        # Check if email already exists
        for student in self.students.values():
            if student.email == email:
                raise ValueError("Student with this email already exists")
        
        student = Student(self.next_student_id, name, email, age)
        self.students[self.next_student_id] = student
        self.next_student_id += 1
        return student.student_id
    
    def remove_student(self, student_id: int):
        if student_id in self.students:
            # Remove from all courses
            student = self.students[student_id]
            for course_name in student.courses:
                if course_name in self.courses:
                    self.courses[course_name].remove_student(student_id)
            
            del self.students[student_id]
            return True
        return False
    
    def add_course(self, course_code: str, name: str, credits: int, instructor: str):
        if course_code in self.courses:
            raise ValueError("Course with this code already exists")
        
        course = Course(course_code, name, credits, instructor)
        self.courses[course_code] = course
        return True
    
    def enroll_student_in_course(self, student_id: int, course_code: str):
        if student_id not in self.students:
            return False, "Student not found"
        
        if course_code not in self.courses:
            return False, "Course not found"
        
        student = self.students[student_id]
        course = self.courses[course_code]
        
        if course.is_full():
            return False, "Course is full"
        
        if course_code in student.courses:
            return False, "Student already enrolled in this course"
        
        # Enroll student
        student.add_course(course_code)
        course.enroll_student(student_id)
        
        return True, "Enrollment successful"
    
    def add_grade_to_student(self, student_id: int, course_code: str, grade: float):
        if student_id not in self.students:
            return False, "Student not found"
        
        student = self.students[student_id]
        return student.add_grade(course_code, grade), "Grade added successfully"
    
    def get_student_transcript(self, student_id: int):
        if student_id not in self.students:
            return None
        
        student = self.students[student_id]
        transcript = {
            'student_info': {
                'id': student.student_id,
                'name': student.name,
                'email': student.email,
                'age': student.age,
                'enrollment_date': student.enrollment_date.strftime("%Y-%m-%d")
            },
            'courses': []
        }
        
        for course_code in student.courses:
            course_info = {
                'course_code': course_code,
                'course_name': self.courses[course_code].name if course_code in self.courses else "Unknown",
                'grades': student.grades[course_code],
                'average': student.get_average_grade(course_code)
            }
            transcript['courses'].append(course_info)
        
        transcript['overall_gpa'] = student.get_average_grade()
        return transcript
    
    def get_course_statistics(self, course_code: str):
        if course_code not in self.courses:
            return None
        
        course = self.courses[course_code]
        stats = {
            'course_info': {
                'code': course.course_code,
                'name': course.name,
                'instructor': course.instructor,
                'credits': course.credits
            },
            'enrollment': {
                'current': course.get_enrollment_count(),
                'capacity': course.max_capacity,
                'available_spots': course.max_capacity - course.get_enrollment_count()
            },
            'grades_statistics': {}
        }
        
        # Calculate grade statistics
        all_grades = []
        for student_id in course.enrolled_students:
            if student_id in self.students:
                student = self.students[student_id]
                if course_code in student.grades:
                    all_grades.extend(student.grades[course_code])
        
        if all_grades:
            stats['grades_statistics'] = {
                'count': len(all_grades),
                'average': sum(all_grades) / len(all_grades),
                'min': min(all_grades),
                'max': max(all_grades),
                'passing_rate': len([g for g in all_grades if g >= 60]) / len(all_grades) * 100
            }
        
        return stats
    
    def search_students(self, query: str):
        results = []
        query = query.lower()
        
        for student in self.students.values():
            if (query in student.name.lower() or 
                query in student.email.lower() or 
                str(student.student_id) == query):
                results.append(student)
        
        return results
    
    def get_top_students(self, limit: int = 10):
        student_averages = []
        
        for student in self.students.values():
            avg = student.get_average_grade()
            if avg > 0:
                student_averages.append((student, avg))
        
        # Sort by average grade (descending)
        student_averages.sort(key=lambda x: x[1], reverse=True)
        
        return student_averages[:limit]
    
    def export_data(self, filename: str):
        data = {
            'students': {},
            'courses': {}
        }
        
        # Export students
        for student_id, student in self.students.items():
            data['students'][student_id] = {
                'name': student.name,
                'email': student.email,
                'age': student.age,
                'courses': student.courses,
                'grades': student.grades,
                'enrollment_date': student.enrollment_date.isoformat()
            }
        
        # Export courses
        for course_code, course in self.courses.items():
            data['courses'][course_code] = {
                'name': course.name,
                'credits': course.credits,
                'instructor': course.instructor,
                'enrolled_students': course.enrolled_students,
                'max_capacity': course.max_capacity
            }
        
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            return True, f"Data exported to {filename}"
        except Exception as e:
            return False, f"Export failed: {str(e)}"
    
    def import_data(self, filename: str):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            # Import students
            for student_id, student_data in data['students'].items():
                student = Student(
                    int(student_id),
                    student_data['name'],
                    student_data['email'],
                    student_data['age']
                )
                student.courses = student_data['courses']
                student.grades = student_data['grades']
                student.enrollment_date = datetime.datetime.fromisoformat(student_data['enrollment_date'])
                self.students[int(student_id)] = student
            
            # Import courses
            for course_code, course_data in data['courses'].items():
                course = Course(
                    course_code,
                    course_data['name'],
                    course_data['credits'],
                    course_data['instructor']
                )
                course.enrolled_students = course_data['enrolled_students']
                course.max_capacity = course_data['max_capacity']
                self.courses[course_code] = course
            
            # Update next_student_id
            if self.students:
                self.next_student_id = max(self.students.keys()) + 1
            
            return True, f"Data imported from {filename}"
        except Exception as e:
            return False, f"Import failed: {str(e)}"
    
    def generate_report(self):
        report = []
        report.append("=== STUDENT MANAGEMENT SYSTEM REPORT ===")
        report.append(f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"System Version: {VERSION}")
        report.append("")
        
        # System overview
        report.append("SYSTEM OVERVIEW:")
        report.append(f"  Total Students: {len(self.students)}")
        report.append(f"  Total Courses: {len(self.courses)}")
        report.append("")
        
        # Course enrollment summary
        report.append("COURSE ENROLLMENT SUMMARY:")
        for course_code, course in self.courses.items():
            enrollment_rate = (course.get_enrollment_count() / course.max_capacity) * 100
            report.append(f"  {course_code}: {course.get_enrollment_count()}/{course.max_capacity} ({enrollment_rate:.1f}%)")
        report.append("")
        
        # Top students
        top_students = self.get_top_students(5)
        if top_students:
            report.append("TOP 5 STUDENTS BY GPA:")
            for i, (student, avg) in enumerate(top_students, 1):
                report.append(f"  {i}. {student.name} (ID: {student.student_id}) - GPA: {avg:.2f}")
        report.append("")
        
        # Grade distribution
        all_grades = []
        for student in self.students.values():
            for grades_list in student.grades.values():
                all_grades.extend(grades_list)
        
        if all_grades:
            report.append("GRADE DISTRIBUTION:")
            grade_ranges = {
                'A (90-100)': len([g for g in all_grades if g >= 90]),
                'B (80-89)': len([g for g in all_grades if 80 <= g < 90]),
                'C (70-79)': len([g for g in all_grades if 70 <= g < 80]),
                'D (60-69)': len([g for g in all_grades if 60 <= g < 70]),
                'F (0-59)': len([g for g in all_grades if g < 60])
            }
            
            for grade_range, count in grade_ranges.items():
                percentage = (count / len(all_grades)) * 100
                report.append(f"  {grade_range}: {count} ({percentage:.1f}%)")
        
        return "\n".join(report)

def create_sample_data(sms):
    """Create sample data for testing"""
    # Add sample students
    students_data = [
        ("Alice Johnson", "alice.j@email.com", 20),
        ("Bob Smith", "bob.smith@email.com", 22),
        ("Charlie Brown", "charlie.b@email.com", 19),
        ("Diana Prince", "diana.p@email.com", 21),
        ("Eve Adams", "eve.adams@email.com", 20)
    ]
    
    student_ids = []
    for name, email, age in students_data:
        student_id = sms.add_student(name, email, age)
        student_ids.append(student_id)
    
    # Add sample courses
    courses_data = [
        ("CS101", "Introduction to Computer Science", 3, "Dr. Wilson"),
        ("MATH201", "Calculus II", 4, "Prof. Johnson"),
        ("ENG102", "English Composition", 3, "Dr. Brown"),
        ("PHYS101", "General Physics", 4, "Prof. Davis")
    ]
    
    for course_code, name, credits, instructor in courses_data:
        sms.add_course(course_code, name, credits, instructor)
    
    # Enroll students in courses and add grades
    enrollments = [
        (1, "CS101", [85, 92, 88]),
        (1, "MATH201", [78, 84, 90]),
        (2, "CS101", [95, 87, 91]),
        (2, "ENG102", [82, 79, 85]),
        (3, "MATH201", [70, 75, 73]),
        (3, "PHYS101", [88, 90, 86]),
        (4, "CS101", [93, 89, 94]),
        (4, "ENG102", [87, 91, 89]),
        (5, "PHYS101", [76, 80, 78])
    ]
    
    for student_id, course_code, grades in enrollments:
        sms.enroll_student_in_course(student_id, course_code)
        for grade in grades:
            sms.add_grade_to_student(student_id, course_code, grade)

def interactive_menu(sms):
    """Interactive command-line menu"""
    while True:
        print("\n=== STUDENT MANAGEMENT SYSTEM ===")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Enroll Student in Course")
        print("4. Add Grade")
        print("5. View Student Transcript")
        print("6. View Course Statistics")
        print("7. Search Students")
        print("8. View Top Students")
        print("9. Generate Report")
        print("10. Export Data")
        print("11. Import Data")
        print("12. Load Sample Data")
        print("0. Exit")
        
        choice = input("\nEnter your choice: ").strip()
        
        if choice == "1":
            name = input("Enter student name: ")
            email = input("Enter student email: ")
            try:
                age = int(input("Enter student age: "))
                student_id = sms.add_student(name, email, age)
                print(f"Student added with ID: {student_id}")
            except ValueError as e:
                print(f"Error: {e}")
            except:
                print("Error: Invalid age")
        
        elif choice == "2":
            course_code = input("Enter course code: ")
            name = input("Enter course name: ")
            try:
                credits = int(input("Enter course credits: "))
                instructor = input("Enter instructor name: ")
                sms.add_course(course_code, name, credits, instructor)
                print("Course added successfully")
            except ValueError as e:
                print(f"Error: {e}")
            except:
                print("Error: Invalid credits")
        
        elif choice == "3":
            try:
                student_id = int(input("Enter student ID: "))
                course_code = input("Enter course code: ")
                success, message = sms.enroll_student_in_course(student_id, course_code)
                print(message)
            except:
                print("Error: Invalid student ID")
        
        elif choice == "4":
            try:
                student_id = int(input("Enter student ID: "))
                course_code = input("Enter course code: ")
                grade = float(input("Enter grade (0-100): "))
                success, message = sms.add_grade_to_student(student_id, course_code, grade)
                print(message)
            except:
                print("Error: Invalid input")
        
        elif choice == "5":
            try:
                student_id = int(input("Enter student ID: "))
                transcript = sms.get_student_transcript(student_id)
                if transcript:
                    print(json.dumps(transcript, indent=2))
                else:
                    print("Student not found")
            except:
                print("Error: Invalid student ID")
        
        elif choice == "6":
            course_code = input("Enter course code: ")
            stats = sms.get_course_statistics(course_code)
            if stats:
                print(json.dumps(stats, indent=2))
            else:
                print("Course not found")
        
        elif choice == "7":
            query = input("Enter search query: ")
            results = sms.search_students(query)
            if results:
                for student in results:
                    print(f"ID: {student.student_id}, Name: {student.name}, Email: {student.email}")
            else:
                print("No students found")
        
        elif choice == "8":
            try:
                limit = int(input("Enter number of top students to show (default 10): ") or "10")
                top_students = sms.get_top_students(limit)
                if top_students:
                    for i, (student, avg) in enumerate(top_students, 1):
                        print(f"{i}. {student.name} (ID: {student.student_id}) - GPA: {avg:.2f}")
                else:
                    print("No students with grades found")
            except:
                print("Error: Invalid number")
        
        elif choice == "9":
            report = sms.generate_report()
            print(report)
        
        elif choice == "10":
            filename = input("Enter filename for export: ")
            success, message = sms.export_data(filename)
            print(message)
        
        elif choice == "11":
            filename = input("Enter filename for import: ")
            success, message = sms.import_data(filename)
            print(message)
        
        elif choice == "12":
            create_sample_data(sms)
            print("Sample data loaded successfully")
        
        elif choice == "0":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

def main():
    """Main function"""
    print("Initializing Student Management System...")
    sms = StudentManagementSystem()
    
    if DEBUG:
        print("Debug mode enabled")
        print(f"Maximum students: {MAX_STUDENTS}")
    
    interactive_menu(sms)

if __name__ == "__main__":
    main()