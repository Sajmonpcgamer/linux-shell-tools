import os
import colorama as color

id = os.popen("/usr/bin/id").read().replace("\n","")

id = id.replace("root",color.Fore.WHITE + color.Back.RED + "root" + color.Fore.RESET + color.Back.RESET)
id = id.replace("sudo",color.Back.YELLOW+color.Fore.BLACK+"sudo"+color.Fore.RESET+color.Back.RESET)
id = id.replace(" ","\n")
id = id.replace(",","\n\t")
id = id.replace("euid", color.Fore.RED+"euid"+color.Fore.RESET)
id = id.replace("uid",color.Fore.GREEN+"uid"+color.Fore.RESET)
id = id.replace("gid",color.Fore.GREEN+"uid"+color.Fore.RESET)
id = id.replace("groups",color.Fore.GREEN+"groups"+color.Fore.RESET)
id = id.replace("lxc",color.Back.YELLOW+color.Fore.BLACK+"lxc"+color.Fore.RESET+color.Back.RESET)

print(id, end="")
