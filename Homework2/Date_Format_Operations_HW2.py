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


for date in in_file:
    if date != "-1":  # if the list element = -1 then do not add to date.split() list
        full_list = date.split()
        if len(full_list) >= 3:  # if length of full_list is 3 or more,  make first element month, 2nd day, 3rd year
            month = full_list[0]
            day = full_list[1]
            year = full_list[2]

            if month in date_list:
                char = day[-1]
                if char == ',':
                    day = day[:len(day)-1]
                    month_num = date_list[month]
                    answer = month_num + '/' + day + '/' + year

                    out_file.write(answer)  # write all output to new file "parsedDates"
                    out_file.write('\n')  # write a new line to the end of parsedDates file

out_file.close()  # close the parsedDates.txt file
in_file.close()  # close the inputDates.txt file
