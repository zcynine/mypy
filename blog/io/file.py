#coding=utf-8

def open_file(file_name):
	f = open(file_name)
	content = f.read()
	f.close()

	return content

f = open("test.txt")
content = f.read()
f.close()

print content

#逐行读取
f = open("test.txt")
while True:
    lines = f.readlines(10000)
    if not lines:
        break
    for line in lines:
        print line.strip()

#重写文件
# f = open("test.txt", "w")
# f.writelines(["hhhhhh", "lllll"])
# f.write("hhhhhhlllll")
# f.close()

# print open_file("test.txt")

#追加内容
f = open("test.txt", "a")
f.writelines(["oooooo", "kkkkk"])
f.close()

print open_file("test.txt")
