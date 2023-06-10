# Simple ToDo App made in Python.
def add_task(task_list, task):
    '''Add TASK to TASK_LIST'''
    return task_list.append(task)


def main():

    continue_flag = True

    while continue_flag:  # Event loop
        print("ToDo List: A)dd Task.  D)elete Task.  E)xit.\n")

        event = input("What would you like to do? ")
        if event == "E":
            continue_flag = False


if __name__ == "__main__":
    main()
