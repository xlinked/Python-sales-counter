# A sales person makes sales every day for five days.
# Write a program that keeps a running total of the number
# of sales made during the five days. The loop should
# ask for the number of sales made for each day, and
# when the loop is finished, the program should display
# the total number of sales made.

def sales_counter():
    num_of_sales = 0

    for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
        question = "How many sales did you make on " + day + ": "
        num_of_sales += int(input(question))

    print("\nThis week you made", num_of_sales, "sales!")


sales_counter()

