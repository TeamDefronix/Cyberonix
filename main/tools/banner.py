def main():
    print('''
    \u001b[31m
     ██████ ██    ██ ██████  ███████ ██████   ██████  ███    ██ ██ ██   ██ 
    ██       ██  ██  ██   ██ ██      ██   ██ ██    ██ ████   ██ ██  ██ ██  
    ██        ████   ██████  █████   ██████  ██    ██ ██ ██  ██ ██   ███   
    ██         ██    ██   ██ ██      ██   ██ ██    ██ ██  ██ ██ ██  ██ ██  
     ██████    ██    ██████  ███████ ██   ██  ██████  ██   ████ ██ ██   ██ 
                                                                           v1.0
                \033[38;5;81mBy Team Metaxone Solution And Technical Navigator

    ''')
    print("\u001b[37m--------------------------------------------------------------------------------")
    print("\t\t\033[38;5;226mA Complete Recource Hub For Cyber Securty Community")
    print("\u001b[37m--------------------------------------------------------------------------------")
def attack(name):
    print(f"\u001b[32m\t\t\t\t{name}")
    print("\u001b[37m--------------------------------------------------------------------------------")
def wrap_text(text, width=80):
    wrapped_text = []
    lines = text.split(" ")
    line = ""
    for word in lines:
        if len(line) + len(word) <= width:
            line += word + " "
        else:
            wrapped_text.append(line)
            line = word + " "
    wrapped_text.append(line)
    return "\n".join(wrapped_text)
def description(Description):
    print("\u001b[34mDescription:")
    print(wrap_text(Description))
    print("\u001b[37m--------------------------------------------------------------------------------")
