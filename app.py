# Simple ToDo App made in Python.
def add_task(task_list, task):
    '''Add TASK to TASK_LIST'''
    return task_list.append(task)
    
def main():
    
    todo_list = []
    
    add_task(todo_list, "Finish Project")
    
    print(todo_list)


if __name__ == "__main__":
    main()
