filename= "Task.txt"

def load_task():
    try:
        with open(filename, 'r') as f:
            return[line.strip() for line in f]
    except FileNotFoundError:
        return[]

def save_task(tasks):
    with open(filename,'w') as f:
        f.write("\n".join(tasks))

tasks=load_task()

while True:
    print("\n 1. View Task \n 2. Add Task \n 3. Remove Task \n 4. Exit")
    choice= input("Choose:")
    if choice == '1':
        if tasks:
            for i, task in enumerate(tasks,1):
                print(f"{i}. {task}")
        else:
            print("No Task Yet")
    elif choice == '2':
        task=input("Enter Task:").strip()
        if task:
            tasks.append(task)
            save_task(tasks)
            print("Task Added")

    elif choice == '3':
        if tasks:
            for i, task in  enumerate(tasks,1):
                print(f"{i}. {task}")
            try:
                num=int(input("Enter Task Number to Remove"))
                if 1 <= num <= len(tasks):
                    tasks.pop(num -1)
                    save_task(tasks)
                    print("Task Removed")
            except ValueError:
                print("Invalid Number !")
        else:
            print("No Task Removed.")

    elif choice == '4':
        break
    else:
        print("Invalid Choice")