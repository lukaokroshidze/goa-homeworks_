age = int(input("რამდენი წლის ხართ? "))
for i in range(age):
    print("თქვენი ასაკი: {i + 1}")
=========================================================

celsius = float(input("შეიტანეთ ტემპერატურა ცელსიუსში: "))
fahrenheit = (celsius * 9/5) + 32
print(f"ტემპერატურა ფარენჰეიტში: {fahrenheit}°F")

============================================================

a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False

============================================================

x = 10
y = 20

print(x < y)   # True
print(x > y)   # False
print(x == y)  # False

======================================================

height = 5
for i in range(1, height + 1):
    print("*" * i)
 
======================================================

age = int(input("რამდენი წლის ხართ? "))
if age == 20:
    print("თქვენი ასაკი არის 20.")
else:
    print("თქვენი ასაკი არ არის 20.")

====================================================

