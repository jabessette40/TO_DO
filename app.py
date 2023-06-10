# Simple ToDo App made in Python.
def add_task(task_list, task):
    '''Add TASK to TASK_LIST'''
    return task_list.append(task)

def view_list(task_list):
    '''Print TASK_LIST to stdout'''
    return print(task_list)


def main():

    continue_flag = True
    todo_list = []

    while continue_flag:  # Event loop
        print("ToDo List: V)iew List. A)dd Task.  D)elete Task.  E)xit.\n")
        event = input("What would you like to do? ")

        if event == "E" or "e":
            continue_flag = False
        elif event == "A" or "a":
            task = input("Enter task: ")
            add_task(todo_list, task)
        elif event == "V" or "v":
            if todo_list:
                view_list(todo_list)
            else:
                print("Todo list is empty! Add a task!")

if __name__ == "__main__":
    main()
