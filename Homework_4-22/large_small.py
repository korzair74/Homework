"""
List Challenge

    Write a Python program to get the largest number from a list.
    Write a Python program to get the smallest number from a list.
    Extra Credit:
    Combine the two functions and add an argument that determines if
     the function will return the largest or smallest,

"""
from random import sample


def min_max(numbs):
  while numbs <= 99:
    numb = sample(range(1, 100), numbs)
    if min(numb) >= 36 and max(numb) <= 45:
      print("Its in the Middle")
    elif min(numb) <=35:
      print(min(numb))
    else:
      print(max(numb))
    break 
  else:
    print("pick number less than 100")
min_max(25)
