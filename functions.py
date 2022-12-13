def get_todos(filepath='tds.txt'):
    try:
        with open(filepath, 'r') as f:
            return [line[:-1] for line in f.readlines()]
    except IOError:
        with open('tds.txt', 'w') as f:
            return []


def write_todos(todos, filepath='tds.txt'):
    with open(filepath, 'w') as f:
        todos = [todo + '\n' for todo in todos]
        f.writelines(todos)


if __name__ == '__main__':
    print('When you run the function directly you get: ')
    print(get_todos())
