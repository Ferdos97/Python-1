
## seed data

# Tasks = [
#     {'title': 'call mom', 'status': 'pending'},
#     {'title': 'buy food', 'status': 'deleted'},
#     {'title': 'post pocket', 'status': 'completed'},
#     {'title': 'post pocket2', 'status': 'pending'},
#     {'title': 'post pocket3', 'status': 'pending'}
# ]

Tasks = []

def show_menu():
    print("\n--------------------------")
    print("1. View")
    print("2. Add")
    print("3. Mark Complete")
    print("4. Delete")
    print("5. Exit")
    print("\n")


def view_tasks():
    if len(Tasks) > 0:
        for index, task in enumerate(Tasks, start =1):
            if task.get('status') != 'deleted':
                print(f'({index}) {task.get('title')}', end='')
                if task.get('status') == 'completed':
                    print(' (done)')
                if task.get('status') == 'pending':
                    print('')
    else:
        print('No task to show!')
    

def add_task():
    task = input('Enter a new task: ')
    if len(task) > 2:
        Tasks.append({
        'title': task,
        'status': 'pending'
        })
    else:
        print('Task must be at least 3 letters.')

 
def complete_task():
    view_tasks()
    try:
        task_id = int(input('Which task to be completed: '))
        Tasks[task_id -1]['status'] = 'completed'
    except Exception as e:
        print('error: ', e)


def delete_task():
    view_tasks()
    task_id = int(input('Which task to be deleted: '))
    Tasks[task_id -1]['status'] = 'deleted'


def main():
    while True:
        show_menu()
        choice = input('Select from menu: ')
        match choice:
            case '1':
                view_tasks()
            case '2':
                add_task()
            case '3':
                complete_task()
            case'4':
                delete_task()
            case'5':
                break
            case _:
                print('Invalid! Select only from menu.')


main()