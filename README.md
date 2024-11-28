
# Online Course Management API

This API manages instructors, courses, and lessons. The RESTful API is built using **Django Rest Framework (DRF)** and provides functionalities for adding, listing, updating, and deleting data.


## Installation

1. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database**:

   Run Django migrations:

   ```bash
   python manage.py migrate
   ```

4. **Start the server**:

   ```bash
   python manage.py runserver
   ```

## API Endpoints

### **1. Instructor API**

- **GET /api/instructors/**  
  List all instructors.

- **POST /api/instructors/**  
  Add a new instructor.

### **2. Course API**

- **GET /api/courses/**  
  List all courses.

- **POST /api/courses/**  
  Add a new course.

### **3. Lesson API**

- **GET /api/lessons/**  
  List all lessons.

- **POST /api/lessons/**  
  Add a new lesson.

## Model Structure

### **Instructor**

- **name**: Instructor's name.
- **email**: Instructor's email (unique).
- **specialization**: Instructor's area of expertise.

### **Course**

- **title**: Course title.
- **description**: Course description.
- **start_date**: Start date of the course.
- **end_date**: End date of the course.
- **instructor**: Instructor responsible for the course (Foreign Key).

### **Lesson**

- **title**: Lesson title.
- **content**: Lesson content.
- **course**: Related course (Foreign Key).
- **order**: Lesson order number (must be positive).

## Serializers

- **InstructorSerializer**: Serializes the Instructor model.
    - Validates that the email is unique.

- **CourseSerializer**: Serializes the Course model.
    - Validates that the course's start date is before the end date.

- **LessonSerializer**: Serializes the Lesson model.
    - Validates that the lesson order number is positive.

## Validations

1. **Instructor email must be unique.**
   - If the email is already taken, an error is returned.

2. **The start date of the course must be before the end date.**

3. **Lesson order number must be positive.**

## API Usage

1. **Add a new instructor**:

   `POST /api/instructors/`

   **Body**:

   ```json
   {
     "name": "Ali Akbar",
     "email": "ali.akbar@example.com",
     "specialization": "Math"
   }
   ```

2. **Add a new course**:

   `POST /api/courses/`

   **Body**:

   ```json
   {
     "title": "Advanced Math",
     "description": "A detailed course on algebra and calculus.",
     "start_date": "2024-01-01",
     "end_date": "2024-06-01",
     "instructor": 1
   }
   ```

3. **Add a new lesson**:

   `POST /api/lessons/`

   **Body**:

   ```json
   {
     "title": "Algebra Basics",
     "content": "Introduction to algebra.",
     "course": 1,
     "order": 1
   }
   ```
