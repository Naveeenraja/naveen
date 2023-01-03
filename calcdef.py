def add(a,b):
    return(a+b)

def sub(a,b):
    return(a-b)

def mul(a,b):
    return(a*b)

def div(a,b):
    return(a/b)

def si(p,n,r):
    si = (p*n*r)/100
    amt = si + p
    return amt,si

def ci(p,n,r):
    ci = p*((1 +(0.01 * r)) **n)
    amt = ci - p
    return ci,amt

def fahrenhit_to_celsius(f):
    cel = (f -32)/1.8
    return cel

def celsius_farhrenhit(c):
    fahrenhit = (c*1.8) + 32
    return fahrenhit

def fahrenhit_to_kelvin(f):
    kelvin = (f +459.67) * 5/9
    return kelvin

def celsius_to_kelvin(c):
    kelvin = c + 273.15
    return kelvin

def square_root(a):
    square_root = pow(a,2)
    return square_root

def cubic_root(a):
    cubic_root_of = pow(a,3)
    return cubic_root_of

def volume_of_square(a):
    volume_of_square = (pow,2)
    return volume_of_square

def volume_of_rectangle(l,b):
    volume_of_rectangle = l*b
    return volume_of_rectangle

def volume_of_circle(r):
    volume_of_circle = 3.14 *pow(r,2)
    return volume_of_circle

def volume_of_right_angle_triangle(b,h):
    volume_of_right_angle_triangle = 1/2 *b*h
    return volume_of_right_angle_triangle

def volume_of_rhombus(d1,d2):
    volume_of_rhombus = 1/2 * d1*d2
    return volume_of_rhombus

def volume_of_parallelogra(b,h):
    volume_of_parallelogra = b*h
    return volume_of_parallelogra

def volume_of_trapezium(h,a,b):
    volume_of_trapezium = (1/2)*h*(a+b)
    return volume_of_trapezium

def perimeter_of_square(a):
    perimeter_of_square = 4*a
    return perimeter_of_square

def perimert_of_rectangle(l,b):
    perimert_of_rectangle = 2*(l+b)
    return perimert_of_rectangle

def perimeter_of_circle(r):
    perimeter_of_circle = 2*3.14*pow(r,2)
    return perimeter_of_circle

def perimeter_of_rhombus(a):
    perimeter_of_rhombus = 4*a
    return perimeter_of_rhombus

def perimeter_of_parallelogra(l,b):
    perimeter_of_parallelogra = 2*(l+b)
    return perimeter_of_parallelogra

def perimeter_of_trapezium(a,b,c,d):
    perimeter_of_trapezium = a+b+c+d
    return perimeter_of_trapezium

def volume_of_cube(a):
    volume_of_cube = pow(a,3)
    return volume_of_cube

def total_surface_area_of_cube(a):
    total_surface_area_of_cube = 6*(pow(a,2))
    return total_surface_area_of_cube

def volume_of_cuboid(l,w,h):
    volume_of_cuboid = l*w*h
    return volume_of_cuboid

def total_surface_area_of_cuboid(l,b,h,):
    total_surface_area_of_cuboid = 2*(l*b + b*h + h*l)
    return total_surface_area_of_cuboid

def volume_of_sphere(r):
    volume_of_sphere = (4/3)* 3.14* pow(r,3)
    return volume_of_sphere

def curved_surface_area_of_sphere(r):
    curved_surface_area_of_sphere = 4* 3.14* pow(r,2)
    return curved_surface_area_of_sphere

def total_surface_area_of_sphere(r):
    total_surface_area_of_sphere = 4* 3.14* pow(r,2)
    return total_surface_area_of_sphere

