import json


def load_tasks():
    try: 
        with open('tasks.json') as file:
            data = json.load(file)
            return data

    except FileNotFoundError:
        print('Error: The file tasks.json was not found.')
        return []
    except json.JSONDecodeError as e:
        print(f'Error: Failed to decode JSON. Check file format {e}')
        return []
    

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent = 4)


def add_tasks():
    return 'add_tasks'  


def update_taks():
    return 'update_tasks'


def delete_tasks():
    return 'delete tasks'


def mark_tasks():
    return 'mark tasks'

