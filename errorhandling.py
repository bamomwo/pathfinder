import os

path = "C:\\Windows\\CSC\\v2.0.6"
try:
	print(os.listdir(path))
except PermissionError:
	pass