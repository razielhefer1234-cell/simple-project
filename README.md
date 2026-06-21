# Task Tracker

Task Tracker is a simple program that helps you keep track of things you need to do. You can create your own account, add tasks, and update their progress as you work on them. Your tasks are saved automatically, so they will still be there the next time you run the program.

## Features

* Create your own account.
* Add new tasks.
* Change the status of tasks.
* Remove tasks you no longer need.
* View all your tasks.
* See only completed tasks.
* See tasks that are still unfinished.
* See tasks that are currently in progress.
* Save all data automatically.

## Task Statuses

Every task has one of the following statuses:

* **Done** – The task has been completed.
* **Not done** – The task has not been completed yet.
* **In progress** – You are currently working on the task.

## Files

### `tracker.py`

The main program. It handles creating accounts and managing tasks.

### `data.json`

Stores all users and their tasks so that information is not lost when the program is closed.

## How to Use

1. Start the program.
2. Create an account or log in with an existing username.
3. Choose an option from the menu.
4. Add tasks and give them a status.
5. Update or delete tasks whenever needed.
6. View all tasks or filter them by their status.
7. Exit the program when you are finished.

## Menu Options

The program provides the following options:

1. Add a new task.
2. Update the status of a task.
3. Delete a task.
4. View all tasks.
5. View completed tasks.
6. View unfinished tasks.
7. View tasks that are currently in progress.
8. Exit the program.

## Data Storage

All information is stored locally in a JSON file. This means that your accounts and tasks are saved automatically and will still be available the next time you open the program.
