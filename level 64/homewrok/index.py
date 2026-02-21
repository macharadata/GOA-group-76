# 1)
def greeting(name):
    return "გამარჯობა, {name}!"

print(greeting("Giorgi"))
print(greeting("Nino"))
print(greeting("David"))






# 2)
def sum_numbers(num1, num2):
    return num1 + num2

print(sum_numbers(5, 7))
print(sum_numbers(10, 20))
print(sum_numbers(-3, 9))





# 3)
def square(num):
    return num * num

print(square(4))
print(square(0))
print(square(-6))





# 4)
def is_adult(age):
    if age >= 18:
        return "you are legaly allowed here"
    else:
        return "you are legaly not allowed here"

print(is_adult(18))
print(is_adult(15))
print(is_adult(30))





# 5) 
def print_length(string):
    print(len(string))

print_length("hello")
print_length("nigger")
print_length("python is cool")





# 6) 
def multiply_numbers(num1, num2):
    return num1 * num2

print(multiply_numbers(3, 4))
print(multiply_numbers(10, 0))
print(multiply_numbers(-2, 8))





# 7)
def score_grade(score):
    if score >= 90:
        return "good boy"
    elif score >= 70 and score <= 89:
        return "great boy"
    elif score >= 50 and score <= 69:
        return "meh boy"
    else:
        return "you no longer dragon warrior"

print(score_grade(95))
print(score_grade(80))
print(score_grade(60))
print(score_grade(20))





# 8) 
def even_or_odd(number):
    if number % 2 == 0:
        return "ts is even"
    else:
        return "ts is odd"

print(even_or_odd(10))
print(even_or_odd(7))
print(even_or_odd(0))





# 9)
def first_letter(name):
    return name[0]

print(first_letter("Giorgi"))
print(first_letter("Nino"))
print(first_letter("David"))





# 10) 
def average_of_three(num1, num2, num3):
    return (num1 + num2 + num3) / 3

print(average_of_three(3, 6, 9))
print(average_of_three(10, 20, 30))
print(average_of_three(5, 5, 8))





#11) 
def check_password(password):
    if password == "python123":
        return "yes dragon warrior pasword"
    else:
        return "no dragon warrior pasword"


print(check_password("python123"))
print(check_password("Python123"))
print(check_password("12345"))





#12)
def to_uppercase(text):
    return text.upper()


print(to_uppercase("hello"))
print(to_uppercase("nigger"))
print(to_uppercase("Python is cool"))
