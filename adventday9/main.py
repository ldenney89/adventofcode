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
            sum = current_subset[i] + num
            if next == sum:
                #print("increased counter")
                counter += 1
    if counter < 1:
        print("got here")
        print(next)
    counter = 0
    start+= 1
    end+=1
    next = lst_input[end]