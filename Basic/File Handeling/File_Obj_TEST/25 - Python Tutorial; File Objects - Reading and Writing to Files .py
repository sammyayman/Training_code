f =open("7-app.log","r")
print(f.name)
print(f.mode)
print(f.closed)
f.close()
print(f.closed)

with open("7-app.log","r") as f:
    size_to_read = 79
    f_content = f.read(size_to_read)
    print(f_content)
    print(f.tell())
 
    # f_content = f.read()
    # print(f_content)
    # f_content = f.read(50)
    # print(f_content)
    # f_content = f.read(40)
    # print(f_content)
    # # for line in f:
    # #     print(line,end="")
        
        
    # f_content = f.readline()
    # print(f_content)
    # f_content = f.readline()
    # print(f_content)
    # print(f.closed)
print(f.closed)



