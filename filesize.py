import os
import math
import sys
import colorama as color
millnames = [color.Fore.WHITE+'B'+color.Fore.RESET,color.Fore.CYAN+'kB'+color.Fore.RESET,color.Fore.BLUE+'MB'+color.Fore.RESET,color.Fore.GREEN+'GB'+color.Fore.RESET,color.Fore.YELLOW+'TB'+color.Fore.RESET,color.Fore.LIGHTMAGENTA_EX+'PB'+color.Fore.RESET,color.Fore.MAGENTA+'EB'+color.Fore.RESET,color.Fore.LIGHTRED_EX+'ZB'+color.Fore.RESET,color.Fore.RED+'YB'+color.Fore.RESET]
def millify(n:int):
	n = float(n)
	millidx = max(0,min(len(millnames)-1,int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))
	return '{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx])

argsfr = ""
for i in sys.argv[1::]:
	argsfr += i
	if i != sys.argv[len(sys.argv)-1]:
		argsfr += " "

if not "/" in argsfr and not "\\" in argsfr:
	if sys.platform == "win32":
		argsfr = os.getcwd() + "\\" + argsfr
	else:
		argsfr = os.getcwd() + "/" + argsfr

print(millify(os.stat(argsfr).st_size))
