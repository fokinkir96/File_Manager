from config import ROOT
import Commands

cmd = ''
cmds = Commands.Commands(ROOT)

while cmd != 'exit':
    cmd = input('Введите команду: ').split()

    args = tuple(cmd[1:])
    cmd = cmd[0]


    cmd = cmds._call(cmd)
    if cmd is False:
        print('Команды не существует')
        continue

    # print(cmd(*args))
    try:
        cmd(*args)
    except Exception as e:
        print(e)
