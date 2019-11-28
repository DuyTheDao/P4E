def computepay(h,r):
    if (h>40) : 
        pay = (40*r)+(h-40)*1.5*r
    else:
        pay = (h*r)     
    return pay
try:
    inp = input("Please enter hours: ")
    hours=float(inp)
    inp = input("Please enter rate: ")
    rate= float(inp)
except:
    print("Please enter a number")
    quit()

print(computepay(hours,rate))
