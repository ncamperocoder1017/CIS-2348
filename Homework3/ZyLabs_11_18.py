# Nicolas Campero
# 1856853

num_list = []
num_of_elements = int(input())

for i in range(0, num_of_elements):
    item = input(int())
    if item > 0:
        num_list.append(item)

num_list.sort()
print(num_list)