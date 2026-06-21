import json

data = {}

def dict_into_json(data):
    with open("data.json", "w") as file:
        json.dump(data, file)

def json_into_dict():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def account_creation(data):
    data = json_into_dict()
    username = input("Pls enter a username: ")
    if username in data:
        print("Username already exists")
        return
    data[username] = {"Tasks": []}
    dict_into_json(data)
    print("All done:)")

def account_check(data, username):
    data = json_into_dict()
    if username in data:
        return True

def add_task(data, username, task, progress):
    data = json_into_dict()
    for all_task in data[username]["Tasks"]:
        key1 = list(all_task.keys())[0]
        if key1 == task:
            return True
    data[username]["Tasks"].append({task: progress})
    dict_into_json(data)
    print("Added a new task")
    return "b"

def update_task_progress(data, username, task, progress):
    data = json_into_dict()
    if not data[username]["Tasks"]:
        return "b"
    for all_task in data[username]["Tasks"]:
        key1 = list(all_task.keys())[0]
        if key1 == task:
            all_task[key1] = progress
            dict_into_json(data)
            return True

def cheack_progress(progress):
    if progress in ["Done", "Not done", "In progress"]:
        return True
    return False

def delete_task(data, username, task):
    data = json_into_dict()
    if not data[username]["Tasks"]:
        print("The tasks list is empty")
        return
    for all_task in data[username]["Tasks"]:
        key1 = list(all_task.keys())[0]
        if key1 == task:
            data[username]["Tasks"].remove(all_task)
            dict_into_json(data)
            return True
    print("Pls try again there is no task like this")

def list_all_tasks(data, username):
    data = json_into_dict()
    if not data[username]["Tasks"]:
        print("The tasks list is empty")
        return
    for task in data[username]["Tasks"]:
        for key, value in task.items():
            print(f"{key}: {value}")

def list_all_done(data, username):
    data = json_into_dict()
    if not data[username]["Tasks"]:
        print("The tasks list is empty")
        return
    for task in data[username]["Tasks"]:
        for key, value in task.items():
            if value == "Done":
                print(f"{key}: {value}")

def list_all_not_done(data, username):
    data = json_into_dict()
    if not data[username]["Tasks"]:
        print("The tasks list is empty")
        return
    for task in data[username]["Tasks"]:
        for key, value in task.items():
            if value == "Not done":
                print(f"{key}: {value}")

def list_all_in_progress(data, username):
    data = json_into_dict()
    if not data[username]["Tasks"]:
        print("The tasks list is empty")
        return
    for task in data[username]["Tasks"]:
        for key, value in task.items():
            if value == "In progress":
                print(f"{key}: {value}")


while True:
    c = input("Do you want to create an account? y/n: ")
    if c == "y":
        account_creation(data)
        break
    elif c == "n":
        break
    else:
        print("Invalid choose")

while True:
    username = input("Pls enter a username (or type 'quit' to exit): ")
    if username.lower() == "quit":
        exit()
    if account_check(data, username):
        print("All done")
        break
    else:
        print("Username not in the database")

while True:
        
    print("---TASK TRACKER---")
    print("Pls pick from the following options:)")
    print("1. Add a new task")
    print("2. Update task progress")
    print("3. Delete a task")
    print("4. list all tasks")
    print("5. List all tasks that are done")
    print("6. List all tasks that are not done")
    print("7. List all tasks that are in progress")
    print("8. Exit")
    while True:
        try:
            choosen = int(input("Pls choose from the option(pick the numbers): "))
            break
        except ValueError:
            print("Pls pick from the numbers")
            
    if choosen == 1:
        while True:
            task = input("Pls enter a new task: ")
            while True:
                progress = input("Pls enter the task progress(Done, Not done, In progress): ")
                if cheack_progress(progress):
                    break
                else:
                    print("Pls try again you have to do the following options: Done, Not done, In progress")
            
            result = add_task(data, username, task, progress)
            if result is True: 
                print("Task Alraedy exists")
            elif result == "b":
                break
                
    if choosen == 2:
        while True:
            progress = input("Pls enter the task progress(Done, Not done, In progress): ")
            if cheack_progress(progress):
                break
            else:
                print("Pls try again you have to do the following options: Done, Not done, In progress")
        while True:
            task = input("Pls enter a new task: ")
            result = update_task_progress(data, username, task, progress)
            if result == "b":
                print("The tasks list is empty")
                break 
            elif result:
                print("Progress updated")
                break
            else:
                print("Pls try again there is no task like this")
                
    if choosen == 3:
        task = input("Pls enter a new task: ")
        delete_task(data, username, task)
    if choosen == 4:
        list_all_tasks(data, username)
    if choosen == 5:
        list_all_done(data, username)
    if choosen == 6:
        list_all_not_done(data, username)
    if choosen == 7:
        list_all_in_progress(data, username)
    if choosen == 8:
        print("Exiting")
        break
