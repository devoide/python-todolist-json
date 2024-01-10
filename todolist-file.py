import os
import json
import time


def main():
    print('TO-DO LIST')
    print('-------------------------------')
    print('WELCOME TO YOUR TO-DO LIST\n')
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
            load()
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
            try:
                with open('todos.json', 'r') as file:
                    data = json.load(file)
                    print('\n\nTO-DO LIST')
                    print('-------------------------------')
                    for i in data:
                        print('- ' + i["content"])
                    input('\n\n[ENTER] TO STOP WATCHING')
                    break
            except json.JSONDecodeError:
                print('ERROR WHILE READING DATA')
                print('EXITING FUNCTION')
                break
        else:
            print('FILE NOT FOUND. CREATING A NEW FILE...')
            create()
    questions()


def create():
    tasks = []
    with open('todos.json', 'w') as file:
        json.dump(tasks, file)


def add():
    task = input('NEW TASK: ')
    if task == '':
        print('YOU MUST ATLEAST WRITE ONE CHARACTER')
        return

    if os.path.exists('todos.json'):
        with open('todos.json', 'r') as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                tasks = []
    else:
        tasks = []
    item = {"id": str(time.time()), "content": str(task)}
    tasks.append(item)
    with open('todos.json', 'w') as file:
        json.dump(tasks, file)
    print('NEW TASK ADDED')
    load()


def delete():
    while True:
        if os.path.exists('todos.json'):
            print('LOADING DATA...')
            try:
                with open('todos.json', 'r') as file:
                    data = json.load(file)
                    print('\n\nTO-DO LIST')
                    print('-------------------------------')
                    todolist = []
                    for i in data:
                        todolist.append(i["content"])
                    input('\n\n[ENTER] TO STOP WATCHING')
                    break
            except json.JSONDecodeError:
                print('ERROR WHILE READING DATA')
                print('EXITING FUNCTION')
                break
        else:
            print('FILE NOT FOUND. CREATING A NEW FILE...')
            create()
    questions()


if __name__ == '__main__':
    main()
