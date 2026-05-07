import os
task = []
def show_menu():
    print ("A.) View B.) Add C.) Delete D.) Exit")
while True:
    show_menu()
    choice = str(input("Pick one."))
    if choice == 'A':
        print (task)
    elif choice == 'B':
        task.append(input("Add the task."))
    elif choice == 'C':
        idx = int(input("Which one?")) - 1
        if 0 <= idx <= len(task):
            task.pop(idx)
    elif choice == 'D':
        break
    else:
        print("no task editor for you, pick a right choice")