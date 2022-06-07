#codewars 'Highest and Lowest' Python

def high_and_low(numbers):
    numbers = numbers.split()
    numbers = [int(i) for i in numbers]
    return str(max(numbers)) + " " + str(min(numbers))

  
"""
Not my solution. But it works very well and if u think about it its logical.

I`ve tried something like this:
***
1   def high_and_low(numbers):
2       b = []
3       c = numbers.split(" ")
4          for g in c:
5               b.append(int(i))
6          b.sort()
7       return (f"{b[len(b)-1]} {b[0]}")
    
 but it returns unexpected indent in line 4. I didnt understood the problem and couldnt find a solution.
    
  
