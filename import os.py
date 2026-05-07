import os
tasks = []
def show_menu():
    print ("\nA. View \nB. Add \nC. Remove \nD. Exit")
while True:
    show_menu()
    choice = input ("Select = ")
    if choice == 'A':
        print (tasks)
    elif choice == 'B':
        tasks.append(input("Task - "))
    elif choice == 'C':
        idx = int(input("Which one?"))
        if 0 <= idx < len(tasks): tasks.pop(idx)
    elif choice == 'D':
        break
    else:
        print ("Invalid Choice suckers")
