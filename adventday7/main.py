input = []

with open('input.txt','r') as fr:
  input = fr.read()

lst_input = input.split("\n")


def contains_gold(bag):
    if bag.contains("shiny gold"):
        return 1
    elif bag.contains("no other bags"):
        return 0
    else: 
        return contains_gold(bag)
        
dict_bags = {}
count_gold = 0
for item in lst_input:
    temp_list = item.split(" bags contain ")
    dict_bags[temp_list[0]]=temp_list[1]
    count_gold += contains_gold(bag)


print(count_gold)
