age = int(input("თქვენი წლოვანება შეიყვანეთ: "))
if age > 13 and age < 19:
    print("თქვენი წლოვანება 13 ზე დიდი და 19 ზე ნაკლებია.")
else:
    print("თქვენი წლოვანება არ შეესაბამება ამ კრიტერიუმს.")

===========================================================

score = int(input("ნუგზარის მიღებული ნიშანი (1-10): "))

is_A = score >= 9
is_B = 8 <= score < 9
is_C = 7 <= score < 8
is_D = 6 <= score < 7
is_F = score < 6

print("is_A:", is_A)
print("is_B:", is_B)
print("is_C:", is_C)
print("is_D:", is_D)
print("is_F:", is_F)

=================================================================

a = True
b = False

print("a and b:", a and b)
print("a or b:", a or b)
print("not a:", not a)
print("not b:", not b)
print("a != b:", a != b)

================================================================

num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))

print("num1 == num2:", num1 == num2)
print("num1 < num2:", num1 < num2)
print("num1 > num2:", num1 > num2)
print("num1 <= num2:", num1 <= num2)
print("num1 >= num2:", num1 >= num2)
print("num1 != num2:", num1 != num2)



