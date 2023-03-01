import config, Commands

cmd = ''
cmds = Commands.Commands(config.ROOT)

while cmd != 'exit':
    cmd = input('Введите команду: ').split()

    args = tuple(cmd[1:])
    cmd = cmd[0]


    cmd = cmds._call(cmd)
    if cmd is False:
        print('Команды не существует')
        continue

    print(cmd(*args))
