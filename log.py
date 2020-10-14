log_file = 'work_log.txt'


def debug(msg: str):
    with open(log_file, 'a') as file:
        file.write(msg+'\n')


def clear():
    open(log_file, 'w').close()
