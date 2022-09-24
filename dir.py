import os
import colorama as color
import stat
from pwd import getpwuid as getpwdid

dir = os.getcwd()
d = os.listdir(dir)

for f in d:
	try:
		# R perm
		if os.access(f, os.R_OK):
			print(color.Fore.LIGHTBLUE_EX + "R", end=color.Fore.RESET)
		else:
			print(color.Fore.WHITE + "-", end=color.Fore.RESET)
		# W perm
		if os.access(f, os.W_OK):
			print(color.Fore.GREEN + "W", end=color.Fore.RESET)
		else:
			print(color.Fore.WHITE + "-", end=color.Fore.RESET)
		# X perm
		if os.access(f, os.X_OK):
			print(color.Fore.RED + "X", end=color.Fore.RESET)
		else:
			print(color.Fore.WHITE + "-", end=color.Fore.RESET)

		print("   ", end="")

		# Owner
		u = getpwdid(os.stat(f).st_uid).pw_name
		if u.lower() == "root":
			# Setuid check
			if os.stat(f).st_mode & stat.S_ISUID != 0:
				print(color.Fore.RED + color.Back.YELLOW + "root", end=color.Fore.RESET + color.Back.RESET)
			else:
				print(color.Fore.WHITE + color.Back.RED + "root", end=color.Fore.RESET + color.Back.RESET)
		else:
			print(color.Fore.GREEN + u, end=color.Fore.RESET)

		print(" " * (12-len(u)), end="")

		# File or folder
		if os.path.isdir(f):
			print(color.Fore.GREEN + f, end=color.Fore.RESET)
			print("/", end="")
		elif os.path.isfile(f):
			print(color.Fore.YELLOW + f, end=color.Fore.RESET)
		print()
	except PermissionError:
		print("\r" + color.Fore.RED + "=== Permission denied ===" + color.Fore.RESET)
	except KeyboardInterrupt:
		exit("\rQuitting...")
	except:
		exit("\rA critical error occured and the program shut down")
