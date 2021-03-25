input = []

with open('input.txt','r') as fr:
  input = fr.read()

lst_input = input.split("\n")

def no_occu_adjacent(i, i2):
    count_occu = 0
    for i3 in range(-1,2):
        for i4 in range(-1, 2):
            try:
                if i3== 0 and i4 == 0:
                    continue
                if new_list[i + i3][i2 + i4] == "#":
                    count_occu +=1
            except IndexError:
                continue
    if count_occu == 0:
        return True
    else:
        return False


def four_adjacent_occupied(i, i2):
    count_occu = 0
    for i3 in range(-1,2):
        for i4 in range(-1, 2):
            try:
                #print(new_list[i + i3][i2 + i4], "here")
                if i3== 0 and i4 == 0:
                    continue
                if new_list[i + i3][i2 + i4] == "#":
                    count_occu +=1
            except IndexError:
                continue

    if count_occu >= 4:
        return True
    else:
        return False

def rules(lst_input):
    new_list = []
    changes = 0
    for i in range(len(lst_input)):
        rw = ""
        new_seat = ""
        for i2 in range(len(lst_input[i])):
            seat = lst_input[i][i2]
            #print(seat)
            if seat == "L" and no_occu_adjacent(i, i2):
                new_seat = "#"
                changes +=1
            elif seat == "#" and four_adjacent_occupied(i, i2):
                new_seat = "L"
                changes +=1
            else:
                new_seat = seat
            rw += new_seat
        new_list.append(rw)   
    return new_list, changes

new_list = lst_input
changes = 1
count = 0
while changes !=0:
    new_list, changes = rules(new_list)
    #print(new_list)
    count += 1

count_occupied = 0
for item in new_list:
    for seat in item:
        if seat == "#":
            count_occupied +=1

print(count_occupied)
