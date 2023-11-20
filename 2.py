def area(side:float):
    return (3*(3**0.5)*side**2)/2
length=float(input("Enter side length of hexagon: "))
print("Area of hexagon is ",round(area(length),2)," square units.")
