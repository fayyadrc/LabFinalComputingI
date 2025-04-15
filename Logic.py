
DATA_FILE = "studentrecords.txt"
students = []
recent_stack = []
student_queue = []



def convert_number_system(number):
    """Convert a decimal number to binary, octal, and hexadecimal."""
    try:
        number = int(number)
        return {
            'binary': bin(number)[2:],
            'octal': oct(number)[2:],
            'hex': hex(number)[2:].upper()
        }
    except ValueError:
        return None


def convert_to_binary(number):
    """Convert a number to its binary representation (both integer and floating point)."""
    try:
        number = float(number)
        integer_binary = bin(int(number))[2:]
        if '.' in str(number):
            fractional_part = number - int(number)
            binary_fraction = ""
            count = 0
            while fractional_part != 0 and count < 10:
                fractional_part *= 2
                binary_fraction += str(int(fractional_part))
                fractional_part -= int(fractional_part)
                count += 1
            return f"Integer Binary: {integer_binary}, Approx Float: {integer_binary}.{binary_fraction}"
        return f"Integer Binary: {integer_binary}"
    except ValueError:
        return None


def factorial(number):
    """Calculate factorial recursively."""
    if number == 0:
        return 1
    return number * factorial(number - 1)


def fibonacci(number):
    """Calculate Fibonacci number recursively."""
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


def load_students():
    """Load student records from file into the global students list."""
    global students
    students.clear()
    try:
        if not os.path.exists(DATA_FILE):
            return

        with open(DATA_FILE, 'r') as file:
            lines = file.readlines()
            if not lines:
                return

            header = lines[0].strip().split(',')
            course_headers = header[2:]

            for line in lines[1:]:
                parts = line.strip().split(',')
                if len(parts) < 2:
                    continue

                name, student_id = parts[0], parts[1]
                grades = {
                    course_headers[i]: int(parts[i + 2])
                    for i in range(len(course_headers))
                    if i + 2 < len(parts) and parts[i + 2].strip()
                }
                average = sum(grades.values()) / len(grades) if grades else 0
                students.append({
                    'name': name,
                    'student_id': student_id,
                    'grades': grades,
                    'average': round(average, 2)
                })
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load student records: {str(e)}")


def save_students():
    """Save the global students list to file."""
    try:
        if not students:
            return

        all_courses = sorted({course for student in students for course in student['grades']})
        with open(DATA_FILE, 'w') as file:
            file.write("Name,Student ID," + ",".join(all_courses) + "\n")
            for student in students:
                grades = [str(student['grades'].get(course, "")) for course in all_courses]
                file.write(f"{student['name']},{student['student_id']}," + ",".join(grades) + "\n")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save student records: {str(e)}")


def search_student(query):
    """Search for students by name or ID."""
    return [
        student for student in students
        if query.lower() in student['name'].lower() or query == student['student_id']
    ]


def update_student(name, student_id, courses, grades):
    """Add or update a student record."""
    try:
        grades_dict = {
            course: int(grade)
            for course, grade in zip(courses, grades)
            if grade.strip()
        }
        average = sum(grades_dict.values()) / len(grades_dict) if grades_dict else 0

        # Check if student exists
        for student in students:
            if student['student_id'] == student_id:
                student['name'] = name
                student['grades'] = grades_dict
                student['average'] = round(average, 2)
                return True

        # If not, add new student
        students.append({
            'name': name,
            'student_id': student_id,
            'grades': grades_dict,
            'average': round(average, 2)
        })
        return True
    except ValueError:
        messagebox.showerror("Error", "Grades must be numeric values")
        return False


def delete_student(student_id):
    """Delete a student record by ID."""
    global students
    students = [student for student in students if student['student_id'] != student_id]


def sort_students():
    """Sort students by average grade in descending order using insertion sort."""
    if not students:
        return students

    for i in range(1, len(students)):
        current_student = students[i]
        current_average = float(current_student['average'])
        j = i - 1

        while j >= 0 and float(students[j]['average']) < current_average:
            students[j + 1] = students[j]
            j -= 1

        students[j + 1] = current_student

    return students



def push_to_recent_stack(student):
    """Add a student to the recent stack (last 5 items only)."""
    recent_stack.append(student)
    if len(recent_stack) > 5:
        recent_stack.pop(0)


def add_request_to_queue(request_data):
    """Add a student request to the queue."""
    student_queue.append(request_data)
    if len(student_queue) > 10:
        student_queue.pop(0)

