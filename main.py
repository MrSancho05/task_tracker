from tasks import load_tasks, save_tasks
from datetime import datetime

def main():
    tasks = load_tasks()
    print('='*50)
    print('Todos:', tasks)
    print('='*50)

    # new task
    # now = datetime.now().isoformat(timespec='second')
    now = datetime.now().isoformat(timespec='seconds')
    new_task = {
        'id': 1 if not tasks else max(task['id'] for task in tasks) + 1,
        'description': 'Test new task',
        'status': 'todo',
        'createdAt': now,
        'updatedAt': now
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print('New task added & saved!')



if __name__ == "__main__":
    main()