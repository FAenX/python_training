def calculate():
    principle = input('Enter principle: ')

    days = input('Enter days: ')

    principle = int(principle)
    days = int(days)
    rate = 0.91
    

    # for day in range(days):
    final = principle * (pow((1 + rate / 100), days))
        # principle += interest

    return final


    

total = calculate()

print(total)

