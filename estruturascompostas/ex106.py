def helping(input_parameter):
    return help(input_parameter)


while True:
    interactive_help = str(input("\033[34mWrite: \033[38m")).lower()
    if interactive_help == "end":
        print("\033[35mWe see you later ")
        break
    else:
        helping(interactive_help)
