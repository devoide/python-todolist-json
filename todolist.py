import os
import json
import time


def main():
    print('WELCOME TO YOUR TO-DO LIST')
    questions()


def questions():
    while True:
        print('\nWHAT WOULD YOU LIKE TO DO?')
        print('-------------------------------')
        print('LOOK AT YOUR TO-DO LIST: 1\n'
              'ADD TASK: 2\n'
              'REMOVE TASK: 3\n'
              'EXIT PROGRAM: 4\n')
        userinput = input()
        if userinput == '1':
            show()
            break
        elif userinput == '2':
            add()
            break
        elif userinput == '3':
            delete()
            break
        elif userinput == '4':
            print('EXITING PROGRAM...')
            break
        else:
            print('INVALID INPUT')


def load():
    while True:
        if os.path.exists('todos.json'):
            print('LOADING DATA...')
            with open('todos.json', 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print('ERROR WHILE READING DATA')
                    print('EXITING FUNCTION')
                    return []
        else:
            print('FILE NOT FOUND. CREATING A NEW FILE...')
            create()


def write(tasks):
    with open('todos.json', 'w') as file:
        json.dump(tasks, file)


def show():
    data = load()
    print('\n\nTO-DO LIST')
    print('-------------------------------')
    for i in data:
        print('- ' + i["content"])
    input('\n\n[ENTER] TO STOP WATCHING')
    questions()


def create():
    tasks = []
    write(tasks)


def add():
    while True:
        task = input('NEW TASK: ')
        if task == ' ' * len(task):
            print('YOU MUST ATLEAST WRITE ONE CHARACTER')
        else:
            tasks = load()
            item = {"id": str(time.time()), "content": str(task)}
            tasks.append(item)
            write(tasks)
            print('NEW TASK ADDED')
            show()
            break


def delete():
    data = load()
    while True:
        if len(data) == 0:
            print('NO TASKS FOUND')
            break
        print('\n\nTO-DO LIST')
        print('-------------------------------')
        for index, item in enumerate(data, start=1):
            print(f'{index}. {item["content"]}')
        userinput = input('\nCHOOSE WHICH TASK YOU WANT TO DELETE / [ENTER] TO CANCEL: ')
        #print(data)
        found = False
        for index, item in enumerate(data, start=1):
            if str(index) == userinput:
                found = True
                #print(f'{userinput} {index}')
                #print(item["id"])
                del data[index -1]
                print('TASK DELETED')
        if not found:
            print('NOTHING FOUND TO DELETE RETURNING TO TO-DO LIST')
            break
        write(data)
        break
    show()


if __name__ == '__main__':
    main()
