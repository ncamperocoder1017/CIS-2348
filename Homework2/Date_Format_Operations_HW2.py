# Nicolas Campero
# 1856853

# create a dictionary of dates with numbers associated to each month
date_list = {
    "January": "1",
    "February": "2",
    "March": "3",
    "April": "4",
    "May": "5",
    "June": "6",
    "July": "7",
    "August": "8",
    "September": "9",
    "October": "10",
    "November": "11",
    "December": "12"
}
# get input file from repository, then output a new file called "parsedDates "to repository
in_file = open('inputDates.txt', 'r')
out_file = open('parsedDates.txt', 'w')



out_file.close()  # close the parsedDates.txt file
in_file.close()  # close the inputDates.txt file
