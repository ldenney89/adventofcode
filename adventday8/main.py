input = []

with open('input.txt','r') as fr:
  input = fr.read()

lst_input = input.split("\n")

lst_lst = [item.split(" ") for item in lst_input]

accumulator = 0
dic_line = {}
line = 0
notchanged=True


for i in range(len(lst_lst)):
    lst_lst = [item.split(" ") for item in lst_input]
    accumulator = 0
    dic_line = {}
    line = 0
    if lst_lst[i][0] == "nop":
        lst_lst[i][0] = "jmp"
    elif lst_lst[i][0] == "jmp":
        lst_lst[i][0] = "nop"
    while line < len(lst_lst):
        #print(line)
        #print(lst_lst[line])
        if line in dic_line.keys():
            #print(accumulator)
            #print(line)
            #print(lst_lst[line])
            break
        if lst_lst[line][0]=="nop":
            dic_line[line] = 1
            line += 1
        if lst_lst[line][0]=="acc":
            dic_line[line] = 1
            accumulator += int(lst_lst[line][1])
            line +=1
        if lst_lst[line][0] == "jmp":
            dic_line[line] = 1
            line += int(lst_lst[line][1])
        if accumulator > 30000:
            break
        if line == len(lst_lst):
            print("got here")
    print("accumulator: ", accumulator)

    