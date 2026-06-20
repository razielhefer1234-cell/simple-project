Task Tracker CLI
A simple, terminal-based task management application written in Python. It allows users to create individual accounts and manage their to-do lists, saving everything locally in a JSON database.

Features
Account Management: Create a unique username or log in to an existing profile.

Task Creation: Add new tasks to your personal list.

Progress Tracking: Assign and update task statuses using specific categories (Done, Not done, In progress).

Task Deletion: Remove tasks you no longer need.

List Filtering: View all tasks at once, or filter them specifically by their current status.

Local Storage: Automatically reads and writes all data to a local JSON file.

Prerequisites & Setup
To run this script successfully, you will need Python 3 installed on your machine and a starter JSON file in the same directory.

Important Note: Based on the script's design, it immediately attempts to read the database file. To prevent a "File Not Found" error on your very first run, ensure you have created a file named data.json in the same folder as your Python script.

Initialize the database: Create the data.json file. Inside this file, type a single opening curly brace followed immediately by a closing curly brace to represent an empty database. Save the file.

Run the script: Open your terminal or command prompt, navigate to the folder containing your files, and execute the Python script using standard terminal commands for running Python files.

How to Use
Upon launching, the program will guide you through a series of prompts:

Welcome Screen: It will first ask if you want to create an account. If you don't have an account yet, type y to register a new username. Type n if you already have one.

Login: Enter your registered username to access your specific task database.

Main Menu: Once logged in, choose an action by typing the corresponding number (1-8):

1: Add a new task (prompts for the task name and its current status).

2: Update task progress (prompts for the new status first, and then asks for the exact task name to update).

3: Delete a task.

4: View all tasks currently on your list.

5-7: View tasks filtered specifically by Done, Not done, or In progress.

8: Save and exit the application.

Tip: When entering a progress status, make sure to type it exactly as prompted (i.e., Done, Not done, or In progress). The application is case-sensitive for these statuses.

Data Structure Overview
The application organizes your data logically within the data.json file. Each registered username serves as a primary profile. Within that profile, there is a dedicated tasks section that holds individual entries. Each entry pairs the exact name of your task with its current progress status.
