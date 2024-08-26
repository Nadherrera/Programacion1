#Listas


#Append
lst = [1,2,3]
lst.append(4)
print(f"append(): {lst}")

#Extend
lst = [1,2]
lst.extend([3,4])
print(f"extend(): {lst}")

#Insert
lst = [1,2,3]
lst.insert(1,1.5)
print(f"insert(): {lst}")

#Remove
lst = [1,2,3]
lst.remove(2)
print(f"remove(): {lst}")

#Pop
lst = [1,2,3]
poppedElement = lst.pop()
print(f"pop(): (Elemento: {poppedElement}, Lista: {lst}) ")

#Index
lst = [1,2,3]
indexOfElement = lst.index(2)
print(f"index(): {indexOfElement}")

#Count
lst = [1,2,3]
countOfElement = lst.count(2)
print(f"count(): {countOfElement}")

#Sort
lst = [3,1,2]
lst.sort()
print(f"sort(): {lst}")

#Reverse
lst = [1,2,3]
lst.reverse()
print(f"reverse(): {lst}")


#Acceso y Operaciones


#Acceso por indice
lst = [1,2,3]
print(f"lst[1]: {lst[1]}")

#Slicing
lst = [1,2,3,4]
print(f"lst[1:3]: {lst[1:3]}")

#Concatenacion de listas
lst1 = [1,2]
lst2 = [3,4]
print(f"lst1 + lst2: {lst1 + lst2}")

#Copia de lista
lst = [1,2]
lstCopy = lst.copy()
print(f"lst.copy(): {lstCopy}")

#Desempaquetado
a,b,c = [1,2,3]
print()

#Funciones Comunes

#len()
#sum()
#min()
#max()
#list()