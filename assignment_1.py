print("1) Given a list x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , 12, 13, 14, 15, 16]")
print("   Produce an ouput:-  [8, 9, 10, 11, 12]\n\n\n")

x = []
for i in range(1, 17):
    x.append(i)
print("Original list : "+ str(x)+ "\n")     #original list


print("Do this by using slicing from the front (positive)")
print(x[7:12:1])                            #slicing positive


print("\nDo this by using slicing from the back (negative)")
a = []
for i in range(11, 6, -1):
    a.append(x[i])
print(a[-1: :-1])                           #slicing negative


print("\nPrint even number from x using list slicing only.")
print(x[1:17:2])


print("\nPrint every 4th number using list slicing only.")
print(x[0:17:4])