import json 
from rich import print as rprint
from rich.console import Console
console = Console()

def add_task(task_list, task):
    '''Add TASK to TASK_LIST'''
    if task:
        task_list.update({task: "[ ]"})
    else:
        print("Didn't detect input!")


def del_task(task_list):
    '''Delete a task from TASK_LIST'''
    choice = input("Delete which task? ")

    if choice in task_list.keys():
        del task_list[choice]
        print(f"Deleted {choice}")
    else:
        print("Couldn't find task!")


def draw_gui(border_char, task_list):
    ''' Draw the menu'''
    # Print The Checklist.
    index = 1

    #print("\nMy Todo List:")
    console.rule("[bold blue]\nMy Todo List:[bold blue/]")
    #print("-" * 13)

    if task_list:
        for task in task_list:
            print(str(index) + " " + str(task_list[task]), str(task))
            index += 1
    else:
        rprint("[blue]Nothing to do! Yay![blue/]")

    # Draw the Menu
    rprint("[magenta]\nA)dd Task.  D)elete Task. M)ark Finished. S)ave. L)oad.  E)xit.[magenta/]")
    console.rule()
    #print(border_char * 63)


def mark_task(task_list):
    ''' Marks a Task Finished.'''
    choice = input("Which task? ")

    if choice in task_list.keys():
        task_list[choice] = "[X]"
    else:
        print("Couldn't find task!")
        
def export_list(task_list, savefile):
    '''Exports the Todo list using JSON'''
    if savefile:
        with open(savefile, "w") as json_file:
            json.dump(task_list, json_file)
            rprint(f"[bold yellow]Saving file {savefile}[bold yellow/]")
        json_file.close()
    else:
        print("No file selected!")
    return

def import_list(load_file):
    '''Imports a Todo list using JSON'''
    if load_file:
        with open(load_file, 'r') as json_file:
            data = json.load(json_file)
        json_file.close()
    else:
        print("No file to load.")

    return data
