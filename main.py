from tasks import load_tasks, save_tasks
from datetime import datetime
import sys

def main():
    tasks = load_tasks()
    print('='*50)
    print('Todos:', tasks)
    print('='*50)

    args = sys.argv

    if len(args) < 2:
        print('python main.py dan keyin: "add" kiriting')
        return
    
    command = args[1]

    if command == 'add':
        if len(args) < 3:
            print('Task matnini kiriting')
            return

        desctiption = args[2]
        # new task
        now = datetime.now().isoformat(timespec='seconds')
        new_task = {
                'id': 1 if not tasks else max(task['id'] for task in tasks) + 1,
                'description': desctiption,
                'status': 'todo',
                'createdAt': now,
                'updatedAt': now
            }
        tasks.append(new_task)
        save_tasks(tasks)
        print(f'Task added: {new_task} {desctiption}')




if __name__ == "__main__":
    main()