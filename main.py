import os
a = int(open("b", "r").read())
b = 0
while b < 2000:
        os.remove("README.md")
	open("b", "w").write(str(a))
	open("README.md", "w").write(str(open("b", "r").read()))
	os.system("git add . &&  git commit -m 'Hello world' &")
	b += 1
	a += 1
os.system("git push &")
