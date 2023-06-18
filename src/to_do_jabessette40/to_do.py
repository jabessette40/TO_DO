# Simple ToDo App made in Python.

from to_do_mod import *

#test_func("Testing...")

def main():

    continue_flag = True
    todo_list = {}

    while continue_flag:  # Event loop
        draw_gui("-", todo_list)
        event = input("What would you like to do? ").strip()
        
        if event in ("A", "a"):
            task = input("Enter task: ")
            add_task(todo_list, task)
        elif event in ("M", "m"):
            continue # Place Holder for check toggle.
        elif event in ("D", "d"):
            if todo_list:
                choice = del_task(todo_list)
                if choice in range(0, len(todo_list)):
                    del todo_list[choice]
                else:
                    print("Error: Task not in list!")
            else:
                print("\nError: Your TO DO list is empty. Congratulations!")
        elif event in ("E", "e"):
            continue_flag = False


if __name__ == "__main__":
    main()
