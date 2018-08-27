import random

from User import User


def generate_random_phone():
    phone = ["09150394133", "09124395193","09151704648", "09109059572","09153710636"]
    return phone[random.randint( 0, len(phone)-1)]




def generate_random_bank_account_number():
    numbers = ["5859831024820176", "6037997190727140", "5892101022660290","5859831050058964"]
    return numbers[random.randint(0,len(numbers)-1)]

def generate_random_name():
    letters = ["a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l","m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    name = ""
    name_len = random.randint(3, 7)
    for i in range(name_len):
        name = name + letters[random.randint(0, 25)]
    return name


def generate_random_pass():

    letters = ["a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l","m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1"
               , "2", "3", "4", "5", "6", "7", "8", "9", "@", "#", "%", "$"]
    password = ""
    password_len = random.randint(6, 15)
    for i in range(password_len):
        password = password + letters[random.randint(0, len(letters)-1)]
    return password


def generate_random_email():
    domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
    letters = ["a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l","m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    email_name = ""
    for i in range(7):
        email_name = email_name + letters[random.randint(0, 25)]
    domain = domains[random.randint( 0, len(domains)-1)]
    return email_name + "@" + domain


def make_random_user():
    return User(generate_random_name(), generate_random_email(), generate_random_bank_account_number(), generate_random_phone(), generate_random_pass())



