input = []
with open('input.txt','r') as fr:
  input = fr.readlines()

input = [item.strip() for item in input]
print(input)

def count_trees(num1, num2):
  x, y = 0, 0
  counttrees=0
  while y <= len(input)-1:
    if input[y][x] == "#":
      counttrees+=1
    #print(input[y][x])
    x+= num1
    if x >= len(input[0]):
      x-=len(input[0])
    y+= num2
    #print(x, y)
  return counttrees

lst_num = []
lst_num.append(count_trees(1, 1))
lst_num.append(count_trees(3, 1))
lst_num.append(count_trees(5, 1))
lst_num.append(count_trees(7, 1))
lst_num.append(count_trees(1, 2))

print(lst_num)

multiply = 1
for x in lst_num:
  multiply*=x

print(multiply)
