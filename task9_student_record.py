students = []

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        branch = input("Enter branch: ")
        marks = input("Enter marks: ")
        students.append({"Name": name, "Branch": branch, "Marks": marks})
        print("Student added!")

    elif choice == "2":
        for s in students:
            print(s)

    elif choice == "3":
        name = input("Enter name to search: ")
        for s in students:
            if s["Name"].lower() == name.lower():
                print("Student found:", s)

    elif choice == "4":
        name = input("Enter name to delete: ")
        for s in students:
            if s["Name"].lower() == name.lower():
                students.remove(s)
                print("Student deleted!")

    elif choice == "5":
        break

    else:
        print("Invalid choice")
