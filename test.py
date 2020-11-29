import random


list_of_lists = []

for i in range(0, 50):
    list_of_lists.append([])
    for j in range(0, 20):
        list_of_lists[i].append(random.randint(0, 100))
