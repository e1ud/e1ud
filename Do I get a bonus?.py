#codewars 'Do I get a bonus?' Python

def bonus_time(salary, bonus):
    if bonus == True:
        a = salary * 10
        return f"${a}"
    else:
        return f"${salary}"
   
