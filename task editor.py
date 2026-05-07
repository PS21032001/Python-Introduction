import os
task = []
def show_menu():
    print ("A. View B. Add C. Delete D. Exit")
while True:
    show_menu()
    choose = input("Pick an option.")
    if choose == "A":
        print (task)
    elif choose == "B":
        task.append(input("Add task."))
    elif choose == "C":
        idx = int(input("Which one?")) - 1
        if 0 <= idx <= len(task):
            task.pop(idx)
    elif choose == 'D':
        break
    else:
        print ("Wrong choice suckers")