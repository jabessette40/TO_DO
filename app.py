# Simple ToDo App made in Python.

# To Do - 
# Prevent delete function from running if the list is empty
# If there is a space in the input, ie "A_" input is neglected. Strip whitespace.
# Add checklist toggle
# Add save/load feature.

def add_task(task_list, task):
    '''Add TASK to TASK_LIST'''
    return task_list.append(task)


def view_list(task_list, border_char):
    '''Print TASK_LIST to stdout'''
    index = 0
    for task in task_list:
        print(border_char * 25)
        print("| " + str(index) + " | " + task)

        index += 1


def del_task(task_list):
    '''Delete a task from TASK_LIST'''
    index = 0
    for task in task_list:
        print(str(index) + " " + task)
        index += 1
    choice = input("Delete which task? ")

    return int(choice)
def draw_gui(border_char):
    ''' Draw the menu'''
    print() # For newline
    print("ToDo List: V)iew List. A)dd Task.  D)elete Task.  E)xit.")
    print(border_char * 55)
    print() # For newline

def main():

    continue_flag = True
    todo_list = []

    while continue_flag:  # Event loop
        draw_gui("-")
        event = input("What would you like to do? ")

        if event in ("A", "a"):
            task = input("Enter task: ")
            add_task(todo_list, task)
        elif event in ("V", "v"):
            if todo_list:
                view_list(todo_list, "-")
            else:
                print("Todo list is empty! Add a task!")
        elif event in ("D", "d"):
            choice = del_task(todo_list)
            if choice in range(0, len(todo_list)):
                del todo_list[choice]
            else:
                print("Error: Task not in list!")
        elif event in ("E", "e"):
            continue_flag = False


if __name__ == "__main__":
    main()
