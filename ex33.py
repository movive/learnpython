numbers=[]

def my_loops(max, inc):
    i = 0
    while i < max:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + inc
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    return numbers
my_numbers = my_loops(6, 1)
print("The numbers: ")

for num in my_numbers:
    print(num)
