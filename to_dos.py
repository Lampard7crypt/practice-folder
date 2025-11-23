instruction = input("Type 'add' to add, 'remove' to remove, and 'view' to view")
task_dict = {}

if instruction.lower() == 'add':
    def add():
        while True:
            key = input("Task:(Enter Q to quit) ")
            if key.lower() == 'q':
                break
            value = input("Priority: ")
            add_task(key, value)
        print(task_dict)
    def add_task(task_name, priority):
        task_dict[task_name] = priority
        print(f"added {task_name}")

if instruction.lower() == 'remove':
    def remove_task(key):
        task_dict.pop(key)

if instruction.lower() == 'view':
    def view_task():
        return task_dict





