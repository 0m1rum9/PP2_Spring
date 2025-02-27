import os

def task1(path):

    print([name for name in os.listdir(path)]) # lists dirs and files
    print([name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]) # lists dirs
    print([name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name))]) # lists files


def task2(path):

    if os.path.exists(path):
        result = 'Path is '

        result += 'readable, ' if os.access(path, os.R_OK) else 'not readable, '

        result += 'writable, ' if os.access(path, os.W_OK) else 'not writable, '

        result += 'executable' if os.access(path, os.X_OK)else 'not executable.'

        print(f'Path {path} exists\n{result}')

    else:
        print(f'Path {path} does not exists')



def task3(path):
    

    if os.path.exists(path):
        print(f'Path {path} exists')
        directory, filename = os.path.split(path)
        print(f"Directory: {directory}")
        print(f"Filename: {filename}")
    else:
        print(f'Path {path} does not exists')

def task4(path):
    
    with open(path, 'r') as file:
        lines = file.readlines()
        print(f'Numbers of lines = {len(lines)}')

def task5(path, l):
    
    with open(path, 'w') as file:
        file.write(' '.join(l))

def task6():
    
    from string import ascii_uppercase
    for letter in ascii_uppercase:
        with open(f'/./home/user/PP2_Spring/{letter}.txt', 'w'):
            pass

    for letter in ascii_uppercase:
        os.remove(f'/./home/user/PP2_Spring/{letter}.txt')
        


def task7(path1, path2):
    
    with open(path1, 'r') as file1, open(path2, 'a') as file2:
        file2.write(file1.read())

def task8(path):
    
    if os.access(path, os.F_OK):
        os.remove(path)
        print('File exists and has been removed')
    else:
        print(f"Error: File '{path}' does not exist.")
# task8("/./home/user/PP2_Spring/1.txt")
# task1("/./home/user/PP2_Spring/lab6")
# task2("/./home/user")

# task6()