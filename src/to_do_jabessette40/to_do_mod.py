def add_task(task_list, task):
    '''Add TASK to TASK_LIST'''
    return task_list.update({task: "[ ]"})


def view_list(task_list):
    '''Print TASK_LIST to stdout'''
    index = 1

    print("My Todo List:")
    print("-" * 13)
    for task in task_list:
        print(str(index) + " " + str(task_list[task]), str(task))
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
    print()  # For newline
    print("ToDo List: V)iew List. A)dd Task.  D)elete Task.  E)xit.")
    print(border_char * 56)
    print()  # For newline

