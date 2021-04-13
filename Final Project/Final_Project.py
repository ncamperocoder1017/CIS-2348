# Nicolas Campero
# 1856853

import csv


class Inventory:

    def __init__(self):
        pass
        # you need to have a class in the code


with open("ManufacturerList.csv", 'r') as main_file:
    csv_file = csv.reader(main_file, delimiter=',')
    for x in csv_file:
        # you need to get the id from x[0] and look
        # it up in the Price list and Service Date list
        # if you put eveything in a list you can sort
        # you need to use a dictionary in the code
        print(x)
