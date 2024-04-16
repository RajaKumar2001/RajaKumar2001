def add():
    print("Adding...")

def modify():
    print("Modifying...")

def delete():
    print("Deleting...")

choice = int(input("Enter a number (1: add, 2: modify, 3: delete): "))
match choice:
    case 1:
        add()
    case 2:
        modify()
    case 3:
        delete()
