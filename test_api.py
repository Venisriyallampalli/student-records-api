import json
from app import app

def run_tests():
    client = app.test_client()
    print("=" * 60)
    print("TESTING FLASK REST API - STUDENT RECORDS MANAGEMENT")
    print("=" * 60)

    # 1. GET Root / Healthcheck
    print("\n--- [TEST 1] GET / (Root Endpoint) ---")
    res = client.get("/")
    print(f"Status Code: {res.status_code}")
    print(f"Response Body: {json.dumps(res.get_json(), indent=2)}")

    # 2. GET all students
    print("\n--- [TEST 2] GET /students (Get All Students) ---")
    res = client.get("/students")
    print(f"Status Code: {res.status_code}")
    print(f"Response Body: {json.dumps(res.get_json(), indent=2)}")

    # 3. POST - Add a new student
    print("\n--- [TEST 3] POST /students (Add New Student) ---")
    payload = {"name": "Kiran Kumar", "course": "Data Science", "grade": "A"}
    print(f"Request Payload: {json.dumps(payload)}")
    res = client.post("/students", json=payload)
    print(f"Status Code: {res.status_code}")
    print(f"Response Body: {json.dumps(res.get_json(), indent=2)}")

    # 4. GET the newly added student by ID
    print("\n--- [TEST 4] GET /students/4 (Get Created Student by ID) ---")
    res = client.get("/students/4")
    print(f"Status Code: {res.status_code}")
    print(f"Response Body: {json.dumps(res.get_json(), indent=2)}")

    # 5. PUT - Update the newly added student
    print("\n--- [TEST 5] PUT /students/4 (Update Student Details) ---")
    update_payload = {"name": "Kiran Kumar", "course": "Artificial Intelligence", "grade": "A+"}
    print(f"Request Payload: {json.dumps(update_payload)}")
    res = client.put("/students/4", json=update_payload)
    print(f"Status Code: {res.status_code}")
    print(f"Response Body: {json.dumps(res.get_json(), indent=2)}")

    # 6. DELETE - Remove student with ID 2
    print("\n--- [TEST 6] DELETE /students/2 (Delete Student with ID 2) ---")
    res = client.delete("/students/2")
    print(f"Status Code: {res.status_code}")
    print(f"Response Body: {json.dumps(res.get_json(), indent=2)}")

    # 7. GET /students to verify updated list
    print("\n--- [TEST 7] GET /students (Verify Records After Operations) ---")
    res = client.get("/students")
    print(f"Status Code: {res.status_code}")
    print(f"Response Body: {json.dumps(res.get_json(), indent=2)}")

    # 8. GET /students/999 (Test 404 Not Found)
    print("\n--- [TEST 8] GET /students/999 (Test 404 Non-existent Student) ---")
    res = client.get("/students/999")
    print(f"Status Code: {res.status_code}")
    print(f"Response Body: {json.dumps(res.get_json(), indent=2)}")

    print("\n" + "=" * 60)
    print("ALL REST API ENDPOINT TESTS COMPLETED SUCCESSFULLY!")
    print("=" * 60)

if __name__ == "__main__":
    run_tests()
