contacts = {
    "number": "4",
    "students": [
        {
            "name": "Alice",
            "age": 20,
            "email": "alice@mail.it"},
        {
            "name": "Bob",
            "age": 22,
            "email": "bob@mail.com"},
        {
            "name": "Charlie", 
            "age": 21,
            "email": "chalie@mail.com"}
    ]
}
print("Current students emails:")
for student in contacts["students"]:
    print(student["email"])