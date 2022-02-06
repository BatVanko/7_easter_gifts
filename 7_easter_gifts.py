presents = input().split(" ")
commands_line = input()

while not commands_line == "No Money":
    commands = commands_line.split()
    command = commands[0]
    if command == "OutOfStock":
        gift = commands[1]
        for i in range(len(presents)):
            if presents[i] == gift:
                presents[i] = "None"
    elif command == "Required":
        command, gift, index = commands
        index = int(index)
        if 0 < index < len(presents):
            presents[index] = gift
    elif command == "JustInCase":
        gift = commands[1]
        presents[-1] = gift
    commands_line = input()
presents_without_none = [el for el in presents if el != "None"]
print(" ".join(presents_without_none))
