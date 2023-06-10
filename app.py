# Simple ToDo App made in Python.

def add_task(task_list, task):
    '''Add TASK to TASK_LIST'''
    return task_list.append(task)

def view_list(task_list):
    '''Print TASK_LIST to stdout'''
    return print(task_list)

def del_task(task_list):
    '''Delete a task from TASK_LIST'''
    index = 0
    for task in task_list:
        print(str(index) + " " + task)
        index += 1


def main():

    continue_flag = True
    todo_list = []

    while continue_flag:  # Event loop
        print("\nToDo List: V)iew List. A)dd Task.  D)elete Task.  E)xit.\n")
        event = input("What would you like to do? ")

        if event in ("A", "a"):
            task = input("Enter task: ")
            add_task(todo_list, task)
        elif event in ("V", "v"):
            if todo_list:
                view_list(todo_list )
            else:
                print("Todo list is empty! Add a task!")
        elif event in ("D", "d"):
            del_task(todo_list)
        elif event in ("E", "e"):
            continue_flag = False
if __name__ == "__main__":
    main()
