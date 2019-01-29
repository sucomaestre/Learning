# Program description and command prompt#

menu_prog = ("In memory To-do List \nThe next program allows you to create, delete,and manage tasks.\n"
             "List of commands: \n1.New (Create a new Task)\n2.List_all (List all tasks)\n3.List_open (List open tasks)\n"
             "4.Complete (Complete a task) \n5.Reopen (Reopen a task)\n6.Quit")
print(menu_prog)

# Tuples#
Task_commands = ("New", "List_all", "List_open", "Complete", "Reopen", "Quit")

# Lists#

Task_status = []
Task_list = []

# Variables#
Command = 0

# Functions#

def New_task(task_description):
    Task_list[len(Task_list):] = [task_description]
    Task_status[len(Task_status):] = ["Open"]
    print("the task has been added to your list ")


def complete_task(task_completed):
    Task_status.insert(task_completed,"Completed")

# User Input#
while Command != "6":
    Command = (raw_input("Introduce the number of your next action (Should be one of the previous commands).:"))
    Command = Command.strip(" ")
    if Command == "1":
        Task = (raw_input("Introduce your task: "))
        New_task(Task)
    elif Command == "2":
        i = 0
        EndList = len(Task_list)
        print(i)
        print (EndList)
        while i < EndList:
            print("The task ID {}. {} has the status {} ".format(i, Task_list[i], Task_status[i]))
            i += 1
    elif Command == "3":
        i = 0
        EndList = len(Task_list)
        while i < EndList:
            if Task_status[i] == "Open":
                print("The task ID {}. {} still in open status".format(i, Task_list[i]))
                i += 1
    elif Command == "4":
        task_id = (raw_input("Introduce the ID of the task that you want complete: "))
        EndList = len(Task_list)
        print (Task_status)
        print (task_id)
        print (EndList)
        if task_id < EndList:
            complete_task(task_id)
            print("the task ID {}. {} has been marked as completed ".format(task_id, Task_list[task_id]))
        else:
            print("The ID doesn't exist. List all task in order to know current tasks and their ID's")
    elif Command == "6":
        exit()
    else:
        print("The command it's not valid. Use one of the valid ones")
exit()
