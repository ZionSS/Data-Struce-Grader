h,w = input("Enter your High and Weight : ").split()
h = float(h)
w = float(w)
if w/(h*h)>=30:
    print("Fat")
elif w/(h*h)>=25 and w/(h*h)<30:
    print("Getting Fat")
elif w/(h*h)>=23 and w/(h*h)<25:
    print("More than Normal Weight")
elif w/(h*h)>=18.5 and w/(h*h)<23:
    print("Normal Weight")
else:
    print("Less Weight")