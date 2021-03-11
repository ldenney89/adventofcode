input = []

with open('input.txt','r') as fr:
  input = fr.read()

lst_input = input.split("\n")
lst_input = [int(i) for i in lst_input]

counter = 0
start = 0 
end = 25
next= lst_input[end]
while (end + 1) < len(lst_input):
    current_subset = lst_input[start:end]
    for num in current_subset:
        for i in range(25):
            if current_subset[i]==num:
                #print("nums equal")
                continue
            summation = current_subset[i] + num
            if next == summation:
                #print("increased counter")
                counter += 1
    if counter < 1:
        print("got here")
        print(next)
    counter = 0
    start+= 1
    end+=1
    next = lst_input[end]

num = 90433990


for start in range(len(lst_input)):
    for end in range(len(lst_input), 0, -1):
        if len(lst_input[start:end])==1:
            continue
        #print(start,end)
        if sum(lst_input[start:end]) == num:
            print("got here")
            print(lst_input[start:end])
    if len(lst_input[start:end])==1:
        continue
    if sum(lst_input[start:end]) == num:
        print("got here")
        print(lst_input[start:end])

new_lst = [3289338, 5179176, 4759952, 5413470, 8402308, 4463250, 5358204, 5385482, 4715571
, 5141223, 4879861, 5096842, 5206454, 6345865, 5288410, 5946272, 5562312]

print(min(new_lst)+ max(new_lst))