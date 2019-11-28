hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter Rate:")
r = float(rate)

if h >= 40:
	pay = r * 40 + (r * 1.5) * (h - 40)
print(pay)

    
