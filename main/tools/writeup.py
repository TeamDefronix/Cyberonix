from main.tools import run_on_browser,colors,banner
import os
import threading
def writeup(writeup_dist,name):
    while True:
        os.system("clear")
        banner.main()
        banner.attack(name.title())
        #convert dict keys in list(type casting)
        key=list(writeup_dist.keys())
        key.append("Go Back")
        for i in range(len(key)):
            print(colors.options,f"{i}) {key[i]}".title(),colors.reset)
        option = input(f"\n {colors.select}Select An Option -> {colors.reset} ")
        #1-9=int kdsjfhgkjds=int X to type cast safely 
        try:
            threading.Thread(target=run_on_browser.main, args=(writeup_dist[key[int(option)]],)).start()
            #a={"a":1,"b":2}
            # print(2)
        except:
            return
