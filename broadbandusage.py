t = int(input("enter the total time in minutes in which the data is used:"))
d = float(input("enter total data used in MB:"))
Tk = int (input ("enter the time in minutes in which data used for free:"))
if t > Tk:
    dk = float(input("entter the amount of data used in free usage period:"))
    cost = d - dk
    print(cost,"rs")
else:
    print("this data was used for free according to plan.")
