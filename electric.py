#input value
hours = int(input("Enter hours used \n"))
if hours <= 1000:
    owed = float(hours * 7.633 / 100)
    print("Amount Owed is $", "%.2f" % owed)
else:
    owed = float((7.633 * 1000 / 100) + ((hours - 1000) * 9.259 / 100))
    print("Amount Owed is $", "%.2f" % owed)

