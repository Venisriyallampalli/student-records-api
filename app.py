from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {"id": 1, "name": "Likhita", "course": "Computer Science", "grade": "A"},
    {"id": 2, "name": "Rahul", "course": "Information Technology", "grade": "B"},
    {"id": 3, "name": "Sneha", "course": "Electronics", "grade": "A+"}
]

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to the Student Records Management API",
        "endpoints": {
            "GET /students": "Get all student records",
            "GET /students/<id>": "Get a student record by ID",
            "POST /students": "Add a new student record",
            "PUT /students/<id>": "Update an existing student record",
            "DELETE /students/<id>": "Delete a student record"
        }
    }), 200

# 1. GET all students
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify({"success": True, "data": students, "total": len(students)}), 200

# 2. GET a single student by ID
@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if not student:
        return jsonify({"success": False, "error": f"Student with ID {student_id} not found"}), 404
    return jsonify({"success": True, "data": student}), 200

# 3. POST - Create a new student
@app.route("/students", methods=["POST"])
def create_student():
    data = request.get_json()
    if not data or "name" not in data or "course" not in data:
        return jsonify({"success": False, "error": "Fields 'name' and 'course' are required"}), 400

    new_id = max([s["id"] for s in students], default=0) + 1
    new_student = {
        "id": new_id,
        "name": data["name"],
        "course": data["course"],
        "grade": data.get("grade", "N/A")
    }
    students.append(new_student)
    return jsonify({"success": True, "message": "Student created successfully", "data": new_student}), 201

# 4. PUT - Update an existing student
@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if not student:
        return jsonify({"success": False, "error": f"Student with ID {student_id} not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"success": False, "error": "Request body must be valid JSON"}), 400

    student["name"] = data.get("name", student["name"])
    student["course"] = data.get("course", student["course"])
    student["grade"] = data.get("grade", student["grade"])

    return jsonify({"success": True, "message": "Student updated successfully", "data": student}), 200

# 5. DELETE - Remove a student
@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    global students
    student = next((s for s in students if s["id"] == student_id), None)
    if not student:
        return jsonify({"success": False, "error": f"Student with ID {student_id} not found"}), 404

    students = [s for s in students if s["id"] != student_id]
    return jsonify({"success": True, "message": f"Student with ID {student_id} deleted successfully"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
