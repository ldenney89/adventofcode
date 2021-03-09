input = []

with open('input.txt','r') as fr:
  input = fr.read()

lst_group = input.split("\n\n")
total_sum = 0

for group in lst_group:
    responses = group.split("\n")
    dic_answer = {}
    for answer in responses:
        for letter in answer:

            dic_answer[letter] = dic_answer.get(letter, 0) + 1
    # print(len(dic_answer))
    # total_sum += len(dic_answer)

    for value in dic_answer.values():
        if value == len(responses):
            total_sum += 1



print(total_sum)
