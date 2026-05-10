#LAS VARIABLES SIRVEN PARA GUARDAR DATOS EN MEMRORIA, PARA LUEGO USARLOS EN NUESTRO PROGRAMA

my_name = "Ian"

print (my_name)

age = 45
print (age)
age = 56
print (age)

age = "34"
print (age)

#tipado dinámico, no es necesario declarar el tipo de variable, el tipo se asigna automáticamente según el valor que se le asigne a la variable
#tipado fuerte, no se pueden realizar operaciones entre tipos de datos diferentes sin convertirlos explícitamente, por ejemplo, no se puede sumar un número entero con una cadena de texto sin convertir uno de los dos a un tipo compatible.
#print (10 + "23") esto peta debe de ser asi:
print (10 + 10)
print ("20" + "3")

#f string, es una forma de formatear cadenas de texto, se utiliza la letra f antes de las comillas y se pueden incluir variables dentro de la cadena utilizando llaves {}
print (f"Hola yo soy {my_name} ")
print (f"ESte es mi nombre: {my_name} y este es mi edad: {age}")
print (type(age))
age = 23
print (type(age))


is_user_logged_in : bool = True
print (is_user_logged_in)
print (type(is_user_logged_in))
is_user_logged_in = 42
print (is_user_logged_in)
print (type(is_user_logged_in))
