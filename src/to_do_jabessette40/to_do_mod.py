def add_task(task_list, task):
    '''Add TASK to TASK_LIST'''
    return task_list.update({task: "[ ]"})



    


def del_task(task_list):
    '''Delete a task from TASK_LIST'''
    index = 0
    for task in task_list:
        print(str(index) + " " + task)
        index += 1
    choice = input("Delete which task? ")

    return int(choice)


def draw_gui(border_char, task_list):
    ''' Draw the menu'''
    # Print The Checklist.
    index = 1

    print("\nMy Todo List:")
    print("-" * 13)
    
    if task_list:
        for task in task_list:
            print(str(index) + " " + str(task_list[task]), str(task))
            index += 1
    else:
        print("Nothing to do!\nYay!")
        
    # Draw the Menu
    print("\nA)dd Task.  D)elete Task. M)ark Finished.  E)xit.")
    print(border_char * 50)
    
    