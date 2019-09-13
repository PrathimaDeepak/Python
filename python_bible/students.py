students = {
            "Alice":["D001", 25, "A"],
            "Bob":["D002", 27, "B"],
            "Claire":["D003", 17, "C"],
            "Dan": ["D004", 21, "D"],
            "Emma": ["D005", 22, "E"]
            }

print(students["Claire"])

print(students["Claire"][0])

print(students["Dan"][1:])


dict_students = {
            "Alice": {"id": "ID001", "age":25, "grade":"A"},
            "Bob":{"id": "ID002", "age":27, "grade":"B"},
            "Claire":{"id": "ID003", "age":17, "grade":"C"},
            "Dan": {"id": "ID004", "age":21, "grade":"D"},
            "Emma": {"id": "ID005", "age":22, "grade":"E"}
            }
print(dict_students["Dan"]["age"])

print(dict_students["Emma"]["id"], dict_students["Emma"]["grade"])

