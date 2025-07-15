# modules
import os
import random

# ensuring pip is up to date and installing colorama
os.system("python -m pip install --upgrade pip")
os.system("pip install colorama")

# obtaining Fore from the colorama library
from colorama import Fore

# password list
pas_list=["123456","password","12345678","qwerty","123456789","12345","1234","111111","1234567","dragon","123123","baseball","abc123","football","monkey","letmein","shadow","master","qwertyuiop","123321","1234567890","michael","654321","superman","1qaz2wsx","7777777","121212","000000","qazwsx","123qwe","trustno1","jordan","jennifer","zxcvbnm","asdfgh","hunter","buster","soccer","harley","batman","andrew","tigger","sunshine","iloveyou","2000","charlie","robert","thomas","hockey","ranger","daniel","starwars","klaster","112233","george","computer","michelle","jessica","pepper","1111","zxcvbn","555555","11111111","131313","freedom","777777","pass","maggie","aaaaaa","ginger","princess","joshua","cheese","amanda","summer","love","ashley","nicole","chelsea","matthew","access","yankees","987654321","dallas","austin","thunder","taylor","matrix","william","corvette","hello","martin","heather","secret","merlin","diamond"]

# user input
os.system("clear")
pas=input("password: ")

# attempt mechanism
attempts = 0

# program
while True:
    
    # chose password
    a=random.choice(pas_list)
    
    # password matched
    if a == pas:
        attempts += 1
        print(f"{Fore.GREEN}Password matched: {a} (attempts: {attempts}){Fore.RESET}")
        break
    
    # password failed to match
    else:
        attempts += 1
        print(f"{Fore.RED}Password failed to match: {a}{Fore.RESET}")