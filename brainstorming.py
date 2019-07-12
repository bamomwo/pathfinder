import os

path = "D:\\"
slash = "\\"

def pathscanner(path):
	try:
		res = os.listdir(path)
		reswithpath = [path+slash+i for i in res]
		print(reswithpath)
		handle = open("scantext.txt",'a+')
		handle.writelines("%s\n" %text for text in reswithpath)
		handle.close()
		for i in reswithpath:
			if os.path.isdir(i):
				pathscanner(i)
	except Exception:
		pass			

pathscanner(path)