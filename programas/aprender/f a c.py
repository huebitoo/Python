# # formula para transformar los celsius a fa: (0 °F − 32) × 5/9 
# fa = []
# celsius = [1, 2, 3, 4, 5, 6 , 32]
# for x in celsius:
#     fa.append(round((x-32)*5/9)) # append = agregar datos a lista fa, round = redondear
# print(fa)

u = "1234"
u = u[::-1]
u.replace(u[0], str(int(u[0])+1)) 
u = u[::-1]
print(u)