
pi = 3.141
radio = input("valor del radio: " )
radio = float(radio)
area= pi * radio**2
#print("el area de un circulo de radio:" ,radio, "es:" ,area)
print("el area de un circulo de radio: " +str(radio) +" es: " +str(area))


# otro ejercico

name = input("Nombre: ")
lastname = input("apellido: ")
age = input("edad: ")
age = int(age)
height = input("altura: " )
height = int(height)
sex = input("masc(1) o fem(0): ")
sex = bool(int(sex))
sobre = height - 100

print("tu nombre completo es:" ,name ,lastname)
print("tienes " +str(age) +" años")
print("en 15 años tendrás" ,age+15 )
print("mides" ,height ,"cm")
print ("eres masculino?" ,sex)

print(sobre)

