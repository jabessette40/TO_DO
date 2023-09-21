# Simple ToDo App made in Python.

from to_do_mod import *

def main():

    continue_flag = True
    todo_list = {}

    while continue_flag:  # Event loope
        draw_gui("-", todo_list)
        event = input("What would you like to do? ").strip()

        if event in ("A", "a"):
            task = input("Enter task: ")
            add_task(todo_list, task)
        elif event in ("M", "m"):
            mark_task(todo_list)
        elif event in ("D", "d"):
            if todo_list:
                del_task(todo_list)
            else:
                print("\nError: Your TO DO list is empty. Congratulations!")
        elif event in ("S", "s"):
            export_list(todo_list, "my_list.json")
        elif event in ("L", "l"):
            todo_list = import_list("my_list.json")
    
        elif event in ("E", "e"):
            continue_flag = False


if __name__ == "__main__":
    main()
