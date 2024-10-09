# მომხმარებლისგან ვიღებთ ინფორმაციას
name = input("შეიყვანეთ სახელი: ")
surname = input("შეიყვანეთ გვარი: ")

# კონკატინაცია
full_name = name + " " + surname

# შედეგის გამოსაჩენად
print("სრული სახელი:", full_name)

======================]================================

# მომხმარებლისგან ვიღებთ ციფრებს და ოპერაციას
name1 = float(input("შეიყვანეთ პირველი ციფრი: "))
name2 = float(input("შეიყვანეთ მეორე ციფრი: "))
operation = input("შეიყვანეთ ოპერაცია (+, -, //, /, *, **): ")

# ოპერაციის შესრულება
 operation == "+":
    result = name1 + name2
 operation == "-":
    result = name1 - name2
 operation == "//":
    result = name1 // name2
 operation == "/":
    result = name1 / name2
 operation == "*":
    result = name1 * name2
 operation == "**":
    result = name1 ** name2
else:
    result = "არასწორი ოპერაცია"

# შედეგის გამოსაჩენად
print("შედეგი:", result)
