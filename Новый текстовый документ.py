figure = str(input ( ))
if figure == "треугольник" :
    a = int(input ())
    b = int(input ())
    c = int(input ())
    p = (a + b + c)/2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print (s)
elif figure == "прямоугольник" :
    a = int(input ())
    b = int(input ())
    print (a * b)
elif figure == "круг" :
    r = int(input ())
    print (3.14 * (r ** 2))
else:
    print ()
