# 📝 To-Do List Application (Console-Based)

A **simple Python console-based To-Do List app** that lets you add, view, and remove tasks, with data stored in a text file so your list stays saved even after you close the program.  
This is beginner-friendly and perfect for internship or learning projects.

---

## 📌 Features
- **Add Tasks** — Add new tasks easily.
- **View Tasks** — Display all your saved tasks.
- **Remove Tasks** — Delete tasks by selecting their number.
- **Persistent Storage** — Tasks are saved in `Task.txt` and loaded automatically.
- **Beginner-Friendly Code** — Easy to read, simple logic, minimal functions.

---

## 📂 Project Structure
📁 ToDoListApp
├── todo.py # Main application code
├── Task.txt # Data file for tasks (auto-created)
└── README.md # Project documentation


**📖 How It Works**
-- Loads Tasks from Task.txt when the program starts.

-- Menu Options let you view, add, or remove tasks.

-- File Handling ensures tasks are saved instantly after changes.

-- Persistent Data — even after closing, tasks remain saved.


**Example Run/ Output**

1. View Task
2. Add Task
3. Remove Task
4. Exit
Choose: 2
Enter Task: Complete Python Internship Report
Task Added.

Choose: 2
Enter Task: Buy Groceries
Task Added.

Choose: 2
Enter Task: Study for Data Science Exam
Task Added.

Choose: 1
1. Complete Python Internship Report
2. Buy Groceries
3. Study for Data Science Exam

Choose: 3
1. Complete Python Internship Report
2. Buy Groceries
3. Study for Data Science Exam
Enter Task Number to Remove: 2
Task Removed.

Choose: 1
1. Complete Python Internship Report
2. Study for Data Science Exam

