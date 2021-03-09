input = []
with open('input.txt','r') as fr:
  input = fr.read()

lst_tickets = input.split("\n")

lst_ids = []

def get_id(row, column):
    id = (row*8) + column
    return id

def process_ticket(ticket):
    binary_row = ticket[:7]
    binary_column = ticket[7:]
    row = find_row(binary_row)
    column = find_column(binary_column)
    return row, column

def find_row(br):
    rows = list(range(128))
    for item in br:
        if item == "B":
            rows = rows[int(len(rows)/2):]
        else:
            rows = rows[:int(len(rows)/2)]
    return rows

def find_column(bc):
    columns = list(range(8))
    for item in bc:
        if item == "R":
            columns = columns[int(len(columns)/2):]
        else:
            columns = columns[:int(len(columns)/2)]
    return columns

for ticket in lst_tickets:
    row, column = process_ticket(ticket)
    id = get_id(row[0], column[0])
    lst_ids.append(id)

print(max(lst_ids))

lst_ids.sort()
counter = 0
for x in range(89,989):
    if lst_ids[counter]== x:
        counter+=1
    else:
        print(x)
