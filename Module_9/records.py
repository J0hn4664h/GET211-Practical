import sqlite3

link = sqlite3.connect("database.db")
pointer = link.cursor()

pointer.execute("""
CREATE TABLE IF  NOT EXISTS students(
    id INTEGER  PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    matric TEXT,
    department TEXT
)
""")

def addStudent (name, matric, department) :
    pointer.execute("INSERT INTO students(name, matric, department) VALUES(?, ?, ?)", (name, matric, department))
    link.commit()

def viewStudents() :
    pointer.execute("SELECT * FROM students")
    rows = pointer.fetchall()

    for row in rows :
        print(row)

def updateDepartment(matric, newDepartment) :
    pointer.execute("UPDATE students SET department = ? WHERE matric = ?", (newDepartment, matric))
    link.commit()

def deleteStudent(matric) :
    pointer.execute("DELETE FROM students WHERE matric = ?", (matric,))
    link.commit()

print("\nTable Created")

addStudent("John Abbah", "25/64908/UE", "CiVil Engineering")
addStudent("James Bond", "25/12345/UE", "Computer Engineeering")
addStudent("Mary Jane", "25/67555/UE", "Bio Chemistry")

print("\n===Students Added===")
viewStudents()

updateDepartment("25/12345/UE", "Civil Engineering")

print("\n===Departments changed===")
viewStudents()

deleteStudent("25/67555/UE")
print("\n====Updates Made====")
viewStudents()

print("\n====All Registered Students====")
viewStudents()

link.close()
