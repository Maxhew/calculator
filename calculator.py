import threading
import time
import os
from time import sleep
from forex_python.converter import CurrencyRates
import random
from googletrans import Translator, constants
from pprint import pprint
import math
import sympy
import sympy as sym
from sympy import *
from sympy import init_printing
from mpmath import cot
import json
import requests

language = input("Language / dil? (en/tr) :  ")

if language == 'en':
    print("""
Select the calculate you want to do.
Press 'q' if you want to quit.
_______________________________________________
1- Addition (x+y)
2- Subtraction (x-y)
3- Multiplication (x.y)
4- Division (x/y)
5- Exponentiation (xʸ)
6- Square root (√x)
7- Factorization (x+1)(x-1)
8- Factorial (x!)
9- Equation simplification
10- Equation solver (x1,x2)
11- Logarithm (log1(10)
12- Trigonometry (sin.cos.tan.cot)
13- Area and Perimeter Solver
14- Remainder Calculator (17/3 = 2)
15- Simple Translator
16- Heads & Tails
17- Crypto Informations
18- Currency Converter
19- Guess the Number
20- LCM and GCD finder
=> Type info if you want to learn more <3
=> Maxy Coding...
""")
    time.sleep(3)
    while True:
        # ? Kullanıcıdan istediği işlemi isteme.
        process = input(
        "Select the number of calculate you want to do (press q if you want to exit!) : ")
        if process == 'info':
            print("=> En : Hello, everyone reading this note, I hope you like my programme. This calculator is multifunctional and has many uses. Just start the program to see what operations it can do. You can play games in it and do high-level math and even some money operations.")
            time.sleep(2)
            print("=> Tr : Merhabalar, bu notu okuyan herkes umarım programımı beğenmiştir. Bu hesap makinesi çok fonksiyonludur ve pek çok işe yarar. Hangi işlemleri yapabildiğini görmek için programı başlatmanız yeterlidir. İçinde oyunlar oynayıp üst düzey matematik işlemleri hatta bazı para işlemlerini bile yapabilirsiniz.")
            time.sleep(2)
            print("=> Ru : Привет всем, кто читает эту заметку, надеюсь вам понравится моя программа. Этот калькулятор многофункционален и имеет множество применений. Просто запустите программу, чтобы увидеть, какие операции она может выполнять. Вы можете играть в игры и заниматься математикой высокого уровня и даже совершать некоторые денежные операции.")
            time.sleep(4)
            process = input(
            "Select the number of calculate you want to do (press q if you want to exit!) : ")

        if process == 'q':
            print("5 seconds left until exiting..")
            print('5..')
            time.sleep(1)
            print('4..')
            time.sleep(1)
            print('3..')
            time.sleep(1)
            print('2..')
            time.sleep(1)
            print('1..')
            time.sleep(1)
            quit()  # ? Çıkmak istiyorsa q tuşuna basmalı.
        msj = "Correct answer => {}"  # ? Temel mesaj formatımız.

        if process == '1':
            print("=> If you type a letter in input, you might get some errors!")
            x = input("Enter the first number: ")
            x = x.lower()
            y = input("Enter the second number: ")
            y = y.lower()
            eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w' and x != '' and x != ' ' y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w' and y != '' and y != ' '

            if eleman is True:
                print(msj.format(float(x)+float(y)))  # ? Toplama

            else:
                print("Noneffective input.. 5 seconds left until exiting..")
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

        elif process == '2':
            x = input("Enter the first number: ")
            x = x.lower()
            y = input("Enter the second number: ")
            y = y.lower()
            eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w' and y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w'

            if eleman is True:

                print(msj.format(float(x)-float(y)))  # ? Çıkarma
            else:
                print("Noneffective input.. 5 seconds left until exiting..")
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

        elif process == '3':
            x = input("Enter the first number: ")
            x = x.lower()
            y = input("Enter the second number: ")
            y = y.lower()
            eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w' and y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w'

            if eleman is True:

                print(msj.format(float(x)*float(y)))  # ? Çarpma
            else:
                print("Noneffective input.. 5 seconds left until exiting..")
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

        elif process == '4':
            x = input("Enter the first number: ")
            x = x.lower()
            y = input("Enter the second number: ")
            y = y.lower()
            eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w' and y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w'

            if eleman is True:

                print(msj.format(float(x)/float(y)))  # ? Bölme
            else:
                print("Noneffective input.. 5 seconds left until exiting..")
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

        elif process == '5':
            x = input("Enter the first number: ")
            x = x.lower()
            y = input("Enter the second number: ")
            y = y.lower()
            eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w' and y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w'

            if eleman is True:

                print(msj.format(float(x)**float(y)))  # ? Üs Alma

            elif x == y:
                print("Noneffective input.. 5 seconds left until exiting..")
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

            else:
                print("Noneffective input.. 5 seconds left until exiting..")
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

        elif process == '6':
            x = input("Enter the number: ")
            x = x.lower()
            eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w'
            if eleman is True:
                print(msj.format(math.sqrt(float(x))))  # Karekök Alma

            else:
                print("Noneffective input.. 5 seconds left until exiting..")
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

        elif process == '7':
            equation1 = input("Enter the equation: ")
            x = sympy.factor(equation1)  # Çarpanlara Ayırma
            print(msj.format(x))

        elif process == '8':
            x = input("Enter the number: ")
            x = x.lower()
            eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w'

            if eleman is True:
                q = sympy.factorial(int(x))  # Faktöriyel
                print(msj.format(q))
            else:
                print("Noneffective input.. 5 seconds left until exiting..")
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

        elif process == '9':
            f = input(
                "Enter the equation that you want to simplify (You have to use parentheses!) : ")
            print(msj.format(simplify(f)))  # Denklem Sadeleştirme

        elif process == '10':
            x = input("Enter the a value: ")
            x = x.lower()
            y = input("Enter the b value: ")
            y = y.lower()
            z = input("Enter the c value: ")
            z = z.lower()
            eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w' and y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w' and z != 'a' and z != 'b' and z != 'c' and z != 'ç' and z != 'd' and z != 'e' and z != 'f' and z != 'g' and z != 'ğ' and z != 'h' and z != 'i' and z != 'j' and z != 'k' and z != 'l' and z != 'm' and z != 'n' and z != 'o' and z != 'ö' and z != 'p' and z != 'r' and z != 's' and z != 'ş' and z != 't' and z != 'u' and z != 'ü' and z != 'v' and z != 'y' and z != 'z' and z != 'x' and z != 'q' and z != 'w'
            if eleman is True:
                delta = float(y)**2-4*float(x)*float(z)
                x1 = (-float(y)-delta**0.5)/(2*float(x))
                x2 = (-float(y)+delta**0.5)/(2*float(x))
                print("First Root : {}\nSecond Root : {}".format(
                    x1, x2))  # Denklem Kök Bulma
            else:
                print("Noneffective input.. 5 seconds left until exiting..")
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

        elif process == '11':
            x = input("Enter the number: ")
            x = x.lower()
            y = input("Enter the base of logarithm: ")
            y = y.lower()
            eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w' and y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w'
            if eleman is True:
                print(msj.format(math.log(float(x), float(y))))  # ? Logaritma
            else:
                print("Noneffective input.. 5 seconds left until exiting..")
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

        elif process == '12':
            x = input("Select the trigonometric function: ")
            y = float(input("Enter the degree: "))  # Trigonometri

            if x == 'sin':
                if y == 0 or y == 180 or y == 360:
                    print(msj.format('0'))
                elif y == 90:
                    print(msj.format('1'))
                elif y == 270:
                    print(msj.format('-1'))
                else:
                    siny = math.sin(math.radians(y))
                    print(siny)

            elif x == 'cos':
                if y == 0 or y == 360:
                    print(msj.format('1'))
                elif y == 90 or y == 270:
                    print(msj.format('0'))
                elif y == 180:
                    print(msj.format('-1'))

                else:
                    cosy = math.cos(math.radians(y))
                    print(msj.format(cosy))

            elif x == 'tan':
                if y == 0 or y == 180 or y == 360:
                    print(msj.format('0'))

                elif y == 90 or y == 270:
                    print(msj.format('∞'))

                else:
                    tany = math.tan(math.radians(y))
                    print(msj.format(tany))

            elif x == 'cot':
                if y == 90 or y == 270:
                    print(msj.format('0'))

                elif y == 0 or y == 180 or y == 360:
                    print(msj.format('∞'))

                else:
                    siny = math.sin(math.radians(y))
                    cosy = math.cos(math.radians(y))
                    coty = cosy/siny
                    print(msj.format(coty))
            else:
                print("Noneffective input.. 5 seconds left until exiting..")
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

        elif process == '13':
            print("=> Just use english characters. Otherwise you might get some errors.")
            time.sleep(1)
            x = input("Choose area, perimeter or volume: ")
            print("=> If you chose volume, you have to select cube, sphere or cylinder.")
            time.sleep(3)

            y = input(
                "Choose the shape(square,triangle,rectangle,circle, cube, sphere, cylinder): ")

            a = x.lower()
            b = y.lower()
            if a == 'area' and b == 'square':
                x = input("Enter the side length: ")
                x = x.lower()
                eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w'
                if eleman is True:
                    area1 = float(x)**2
                    print(msj.format(area1))
                else:
                    print("Noneffective input.. 5 seconds left until exiting..")
                    print('5..')
                    time.sleep(1)
                    print('4..')
                    time.sleep(1)
                    print('3..')
                    time.sleep(1)
                    print('2..')
                    time.sleep(1)
                    print('1..')
                    time.sleep(1)
                    quit()

            elif a == 'area' and b == 'triangle':
                x = input("Enter the base length: ")
                x = x.lower()
                y = input("Enter the height: ")
                y = y.lower()
                eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w' and y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w'
                if eleman is True:
                    area2 = float(x)*float(y)/2
                    print(msj.format(area2))
                else:
                    print("Noneffective input.. 5 seconds left until exiting..")
                    print('5..')
                    time.sleep(1)
                    print('4..')
                    time.sleep(1)
                    print('3..')
                    time.sleep(1)
                    print('2..')
                    time.sleep(1)
                    print('1..')
                    time.sleep(1)
                    quit()

            elif a == 'area' and b == 'rectangle':
                x = input("Enter the length of long side: ")
                x = x.lower()
                y = input("Enter the length of short side: ")
                y = y.lower()
                eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w' and y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w'
                if eleman is True:
                    area3 = float(x)*float(y)
                    print(msj.format(area3))
                else:
                    print("Noneffective input.. 5 seconds left until exiting..")
                    print('5..')
                    time.sleep(1)
                    print('4..')
                    time.sleep(1)
                    print('3..')
                    time.sleep(1)
                    print('2..')
                    time.sleep(1)
                    print('1..')
                    time.sleep(1)
                    quit()

            elif a == 'area' and b == 'circle':
                x = input("Enter the radius: ")
                x = x.lower()
                eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w'
                if eleman is True:

                    area4 = math.pi*float(x)*float(x)
                    print(msj.format(area4))
                else:
                    print("Noneffective input.. 5 seconds left until exiting..")
                    print('5..')
                    time.sleep(1)
                    print('4..')
                    time.sleep(1)
                    print('3..')
                    time.sleep(1)
                    print('2..')
                    time.sleep(1)
                    print('1..')
                    time.sleep(1)
                    quit()

            elif a == 'perimeter' and b == 'square':
                x = input("Enter the side length: ")
                x = x.lower()
                eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w'
                if eleman is True:
                    perimeter1 = 4*float(x)
                    print(msj.format(perimeter1))
                else:
                    print("Noneffective input.. 5 seconds left until exiting..")
                    print('5..')
                    time.sleep(1)
                    print('4..')
                    time.sleep(1)
                    print('3..')
                    time.sleep(1)
                    print('2..')
                    time.sleep(1)
                    print('1..')
                    time.sleep(1)
                    quit()

            elif a == 'perimeter' and b == 'triangle':
                x = input("Enter the length of first side: ")
                x = x.lower()
                y = input("Enter the length of second side: ")
                y = y.lower()
                z = input("Enter the length of third side: ")
                z = z.lower()
                eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w' and y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w' and z != 'a' and z != 'b' and z != 'c' and z != 'ç' and z != 'd' and z != 'e' and z != 'f' and z != 'g' and z != 'ğ' and z != 'h' and z != 'i' and z != 'j' and z != 'k' and z != 'l' and z != 'm' and z != 'n' and z != 'o' and z != 'ö' and z != 'p' and z != 'r' and z != 's' and z != 'ş' and z != 't' and z != 'u' and z != 'ü' and z != 'v' and z != 'y' and z != 'z' and z != 'x' and z != 'q' and z != 'w'
                if eleman is True:

                    perimeter2 = float(x)+float(y)+float(z)
                    print(msj.format(perimeter2))
                else:
                    print("Noneffective input.. 5 seconds left until exiting..")
                    print('5..')
                    time.sleep(1)
                    print('4..')
                    time.sleep(1)
                    print('3..')
                    time.sleep(1)
                    print('2..')
                    time.sleep(1)
                    print('1..')
                    time.sleep(1)
                    quit()

            elif a == 'perimeter' and b == 'rectangle':
                x = input("Enter the length of long side: ")
                x = x.lower()
                y = input("Enter the length of short side: ")
                y = y.lower()
                eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w' and y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w'
                if eleman is True:
                    perimeter3 = 2*(float(x)+float(y))
                    print(msj.format(perimeter3))
                else:
                    print("Noneffective input.. 5 seconds left until exiting..")
                    print('5..')
                    time.sleep(1)
                    print('4..')
                    time.sleep(1)
                    print('3..')
                    time.sleep(1)
                    print('2..')
                    time.sleep(1)
                    print('1..')
                    time.sleep(1)
                    quit()

            elif a == 'perimeter' and b == 'circle':
                x = input("Enter the radius: ")
                x = x.lower()
                eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w'
                if eleman is True:
                    perimeter4 = 2*math.pi*float(x)
                    print(msj.format(perimeter4))
                else:
                    print("Noneffective input.. 5 seconds left until exiting..")
                    print('5..')
                    time.sleep(1)
                    print('4..')
                    time.sleep(1)
                    print('3..')
                    time.sleep(1)
                    print('2..')
                    time.sleep(1)
                    print('1..')
                    time.sleep(1)
                    quit()

            elif a == 'volume' and b == 'cube':
                x = input("Enter the length of side: ")
                x = x.lower()
                eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w'
                if eleman is True:
                    volume1 = float(x)**3
                    print(msj.format(volume1))
                else:
                    print("Noneffective input.. 5 seconds left until exiting..")
                    print('5..')
                    time.sleep(1)
                    print('4..')
                    time.sleep(1)
                    print('3..')
                    time.sleep(1)
                    print('2..')
                    time.sleep(1)
                    print('1..')
                    time.sleep(1)
                    quit()

            elif a == 'volume' and b == 'sphere':
                x = input("Enter the radius: ")
                x = x.lower()
                eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w'
                if eleman is True:
                    volume2 = 4/3*math.pi*float(x)**3
                    print(msj.format(volume2))
                else:
                    print("Noneffective input.. 5 seconds left until exiting..")
                    print('5..')
                    time.sleep(1)
                    print('4..')
                    time.sleep(1)
                    print('3..')
                    time.sleep(1)
                    print('2..')
                    time.sleep(1)
                    print('1..')
                    time.sleep(1)
                    quit()

            elif a == 'volume' and b == 'cylinder':
                x = input("Enter the radius: ")
                y = input("Enter the height: ")
                x = x.lower()
                y = y.lower()
                eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w' and y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w'
                if eleman is True:
                    volume3 = math.pi*float(x)**2*float(y)
                    print(msj.format(volume3))
                else:
                    print("Noneffective input.. 5 seconds left until exiting..")
                    print('5..')
                    time.sleep(1)
                    print('4..')
                    time.sleep(1)
                    print('3..')
                    time.sleep(1)
                    print('2..')
                    time.sleep(1)
                    print('1..')
                    time.sleep(1)
                    quit()

            elif a == 'area' and b == 'cube':
                x = input("Enter the length of side: ")
                eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w'
                if eleman is True:
                    area5 = 6*float(x)**2
                    print(msj.format(area5))
                else:
                    print("Noneffective input.. 5 seconds left until exiting..")
                    print('5..')
                    time.sleep(1)
                    print('4..')
                    time.sleep(1)
                    print('3..')
                    time.sleep(1)
                    print('2..')
                    time.sleep(1)
                    print('1..')
                    time.sleep(1)
                    quit()

            elif a == 'area' and b == 'sphere':
                x = input("Enter the radius: ")
                eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w'
                if eleman is True:
                    area6 = 4*float(x)**2*math.pi
                    print(msj.format(area6))
                else:
                    print("Noneffective input.. 5 seconds left until exiting..")
                    print('5..')
                    time.sleep(1)
                    print('4..')
                    time.sleep(1)
                    print('3..')
                    time.sleep(1)
                    print('2..')
                    time.sleep(1)
                    print('1..')
                    time.sleep(1)
                    quit()

            elif a == 'area' and b == 'cylinder':
                x = input("Enter the radius: ")
                y = input("Enter the height: ")
                x = x.lower()
                y = y.lower()
                eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w' and x != '-' and y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w' and y != '-'
                if eleman is True:
                    area7 = 2*math.pi*float(x)*(float(x)+float(y))
                    print(msj.format(area7))

                else:
                    print("Noneffective input.. 5 seconds left until exiting..")
                    print('5..')
                    time.sleep(1)
                    print('4..')
                    time.sleep(1)
                    print('3..')
                    time.sleep(1)
                    print('2..')
                    time.sleep(1)
                    print('1..')
                    time.sleep(1)
                    quit()

            else:
                print("Noneffective input.. 5 seconds left until exiting..")
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

        elif process == '14':
            x = input("Enter the dividend: ")
            x = x.lower()
            y = input("Enter the divisor:  ")
            y = y.lower()
            eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w' and y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w'
            if eleman is True:
                remainder = float(x) % float(y)
                print(msj.format(remainder))
            else:
                print("Noneffective input.. 5 seconds left until exiting..")
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

        elif process == '15':
            translator = Translator()
            print('=> Enter the text to be translated as a single line.')
            time.sleep(2)
            a = input("Enter the text you want to translate: ")
            print('=> Only some languages are available. ')
            time.sleep(1.5)
            print("""
            Some language codes for you;
            pt => Portuguese, zh-cn => Chinese, de => German, es => Spanish, en => English, ru => Russian, fr => French, tr => Turkish, ko => Korean, ja => Japanese, it => Italian, ar => Arabic 
            """)
            time.sleep(1.5)
            b = input("Select the language you want to translate the text into: ")
            if b == 'pt' or b == 'cn' or b == 'de' or b == 'es' or b == 'gb' or b == 'en' or b == 'ru' or b == 'fr' or b == 'tr' or b == 'ko' or b == 'ja' or b == 'it' or b == 'ar':

                translation = translator.translate(a, dest=b)
                print(f"{translation.text} ({translation.dest})")
            else:
                print('Noneffective input.. 5 seconds left until exiting..')
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

        elif process == '16':
            a = random.randint(0, 100)
            msg30 = "I AM FLIPPING..."
            if a <= 50:
                print(msg30 + 'HEADS WON')

            elif a >= 51:
                print(msg30 + 'TAILS WON')

            else:
                print("Noneffective input.. 5 seconds left until exiting..")
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

        elif process == '17':
            key = "https://api.binance.com/api/v3/ticker/price?symbol="
            currencies = ["BTCUSDT", "DOGEUSDT", "LTCUSDT"]
            j = 0
            for i in currencies:
                url = key+currencies[j]
                data = requests.get(url)
                data = data.json()
                j = j+1
                print(f"{data['symbol']} price is {data['price']}")

        elif process == '18':
            print("=> You have to enter currencies correct. If you don't, you might get some errors!")
            initial_currency = input("Enter the initial currency: ")
            target_currency = input("Enter the target currency: ")
            while True:
                try:
                    amount = float(input("Enter the amount: "))
                except:
                    print("The amount must be a numeric value!")
                    continue
                if not amount > 0:
                    print("The amount must be greater than 0")
                    continue
                else:
                    break
            url = "https://api.apilayer.com/fixer/convert?to=" + target_currency + \
                "&from=" + initial_currency + "&amount=" + str(amount)

            payload = {}
            headers = {
                "apikey": "o6SGccKw9pmrnyipI4m6yf71VhQKkl1z"
            }

            response = requests.request("GET", url, headers=headers, data=payload)

            status_code = response.status_code

            if status_code != 200:
                print("Uh oh, there was a problem. Please try again later")
                quit()

            result = response.json()
            print("Conversion result => " + str(result["result"]))

        elif process == '19':
            x = random.randint(0, 100)
            timer = 0
            time.sleep(1)
            y = input("Enter your guess (You can guess 7 times..) => ")
            y = y.lower()
            eleman = y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w'
            if eleman is True:

                while True:
                    if int(y) == int(x):
                        print("=> You win the game. Congratulations..")
                        print("=> You guessed {} times.".format(timer+1))
                        break

                    if timer == 6:
                        print("=> You lost the game. Try again!")
                        break

                    elif int(y) > int(x):
                        print("You have to say LOWER!..")
                        y = input("Enter your guess again => ")
                        y = y.lower()
                        eleman = y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w'
                        if eleman is True:
                            timer = timer+1
                        else:
                            print("Noneffective input.. 5 seconds left until exiting..")
                            print('5..')
                            time.sleep(1)
                            print('4..')
                            time.sleep(1)
                            print('3..')
                            time.sleep(1)
                            print('2..')
                            time.sleep(1)
                            print('1..')
                            time.sleep(1)
                            quit()

                    elif int(y) < int(x):
                        print("You have to say HIGHER!..")
                        y = input("Enter your guess again => ")
                        y = y.lower()
                        eleman = y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w'
                        if eleman is True:
                            timer = timer+1
                        else:
                            print("Noneffective input.. 5 seconds left until exiting..")
                            print('5..')
                            time.sleep(1)
                            print('4..')
                            time.sleep(1)
                            print('3..')
                            time.sleep(1)
                            print('2..')
                            time.sleep(1)
                            print('1..')
                            time.sleep(1)
                            quit()

        elif process == '20':
            print("=> LCM means least common multiple. GCD means greatest common divisor.")
            time.sleep(2)
            x = input("Enter the first number: ")
            x = x.lower()
            time.sleep(1)
            y = input("Enter the second number: ")
            y = y.lower()
            eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w' and y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w' and x != "" and y != ""

            if eleman is True:
                print("The correct answer for LCM => {}".format(
                    math.lcm(int(x), int(y))))
                time.sleep(1)
                print("The correct answer for GCD => {}".format(
                    math.gcd(int(x), int(y))))
            else:
                print("Noneffective input.. 5 seconds left until exiting...")
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

        else:
            print("Noneffective input.. 5 seconds left until exiting...")
            print('5..')
            time.sleep(1)
            print('4..')
            time.sleep(1)
            print('3..')
            time.sleep(1)
            print('2..')
            time.sleep(1)
            print('1..')
            time.sleep(1)
            quit()

elif language == 'tr':
    print("""
Select the calculate you want to do.
Press 'q' if you want to quit.
_______________________________________________
1- Toplama (x+y)
2- Çıkarma (x-y)
3- Çarpma (x.y)
4- Bölme (x/y)
5- Üslü İfade (xʸ)
6- Köklü İfade (√x)
7- Çarpanlarına Ayırma (x+1)(x-1)
8- Faktöriyel (x!)
9- Denklem Sadeleştirme
10- Denklem Çözücü (x1,x2)
11- Logaritma (log1(10)
12- Trigonometri (sin.cos.tan.cot)
13- Alan, Çevre, Hacim Hesaplayıcı
14- Kalan Bulma (17/3 = 2)
15- Basit Çeviri Makinesi
16- Yazı & Tura
17- Kripto Para Değerleri
18- Para Birimi Dönüştürücü
19- Sayıyı tahmin et!
20- EBOB ve EKOK Hesaplayıcı
=> Daha fazla bilgi için 'info' yazınız.
=> Maxy Coding...
""")
    time.sleep(3)
    while True:
        # ? Kullanıcıdan istediği işlemi isteme.
        process = input(
        "Yapmak istediğiniz işlemi seçiniz. (çıkmak için q tuşuna basın!) : ")
        if process == 'info':
            print("=> En : Hello, everyone reading this note, I hope you like my programme. This calculator is multifunctional and has many uses. Just start the program to see what operations it can do. You can play games in it and do high-level math and even some money operations.")
            time.sleep(2)
            print("=> Tr : Merhabalar, bu notu okuyan herkes umarım programımı beğenmiştir. Bu hesap makinesi çok fonksiyonludur ve pek çok işe yarar. Hangi işlemleri yapabildiğini görmek için programı başlatmanız yeterlidir. İçinde oyunlar oynayıp üst düzey matematik işlemleri hatta bazı para işlemlerini bile yapabilirsiniz.")
            time.sleep(2)
            print("=> Ru : Привет всем, кто читает эту заметку, надеюсь вам понравится моя программа. Этот калькулятор многофункционален и имеет множество применений. Просто запустите программу, чтобы увидеть, какие операции она может выполнять. Вы можете играть в игры и заниматься математикой высокого уровня и даже совершать некоторые денежные операции.")
            time.sleep(4)
            process = input(
            "Yapmak istediğiniz işlemi seçiniz. (çıkmak için q tuşuna basın!) : ")

        if process == 'q':
            print("5 saniye içinde kapanacak..")
            print('5..')
            time.sleep(1)
            print('4..')
            time.sleep(1)
            print('3..')
            time.sleep(1)
            print('2..')
            time.sleep(1)
            print('1..')
            time.sleep(1)
            quit()  # ? Çıkmak istiyorsa q tuşuna basmalı.
        msj = "Doğru cevap => {}"  # ? Temel mesaj formatımız.

        if process == '1':
            print("=> Eğer harf girerseniz bazı hatalar ile karşılaşabilirsiniz!")
            x = input("İlk sayıyı giriniz: ")
            x = x.lower()
            y = input("İkinci sayıyı giriniz: ")
            y = y.lower()
            eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w' and y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w'

            if eleman is True:
                print(msj.format(float(x)+float(y)))  # ? Toplama

            else:
                print("Geçersiz giriş.. 5 saniye içinde kapanacak..")
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

        elif process == '2':
            x = input("İlk sayıyı giriniz: ")
            x = x.lower()
            y = input("İkinci sayıyı giriniz: ")
            y = y.lower()
            eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w' and y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w'

            if eleman is True:

                print(msj.format(float(x)-float(y)))  # ? Çıkarma
            else:
                print("Geçersiz giriş.. 5 saniye içinde kapanacak..")
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

        elif process == '3':
            x = input("İlk sayıyı giriniz: ")
            x = x.lower()
            y = input("İkinci sayıyı giriniz: ")
            y = y.lower()
            eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w' and y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w'

            if eleman is True:

                print(msj.format(float(x)*float(y)))  # ? Çarpma
            else:
                print("Geçersiz giriş.. 5 saniye içinde kapanacak..")
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

        elif process == '4':
            x = input("İlk sayıyı giriniz: ")
            x = x.lower()
            y = input("İkinci sayıyı giriniz: ")
            y = y.lower()
            eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w' and y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w'

            if eleman is True:

                print(msj.format(float(x)/float(y)))  # ? Bölme
            else:
                print("Geçersiz giriş.. 5 saniye içinde kapanacak..")
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

        elif process == '5':
            x = input("İlk sayıyı giriniz: ")
            x = x.lower()
            y = input("İkinci sayıyı giriniz: ")
            y = y.lower()
            eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w' and y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w'

            if eleman is True:

                print(msj.format(float(x)**float(y)))  # ? Üs Alma

            elif x == y:
                print("Geçersiz giriş.. 5 saniye içinde kapanacak..")
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

            else:
                print("Geçersiz giriş.. 5 saniye içinde kapanacak..")
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

        elif process == '6':
            x = input("Sayıyı giriniz: ")
            x = x.lower()
            eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w'
            if eleman is True:
                print(msj.format(math.sqrt(float(x))))  # Karekök Alma

            else:
                print("Geçersiz giriş.. 5 saniye sonra kapanacak..")
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

        elif process == '7':
            equation1 = input("Denklemi giriniz: ")
            x = sympy.factor(equation1)  # Çarpanlara Ayırma
            print(msj.format(x))

        elif process == '8':
            x = input("Sayıyı giriniz: ")
            x = x.lower()
            eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w'

            if eleman is True:
                q = sympy.factorial(int(x))  # Faktöriyel
                print(msj.format(q))
            else:
                print("Geçersiz giriş.. 5 saniye içinde kapanacak..")
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

        elif process == '9':
            f = input(
                "Sadeleştirmek istediğiniz denklemi giriniz (Parantez kullanmalısınız!) : ")
            print("=> Örneğin; (x**2+2*x+1)/(x+1) şeklinde.")
            time.sleep(1.5)
            print(msj.format(simplify(f)))  # Denklem Sadeleştirme

        elif process == '10':
            x = input("a değerini giriniz: ")
            x = x.lower()
            y = input("b değerini giriniz: ")
            y = y.lower()
            z = input("c değerini giriniz: ")
            z = z.lower()
            eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w' and y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w' and z != 'a' and z != 'b' and z != 'c' and z != 'ç' and z != 'd' and z != 'e' and z != 'f' and z != 'g' and z != 'ğ' and z != 'h' and z != 'i' and z != 'j' and z != 'k' and z != 'l' and z != 'm' and z != 'n' and z != 'o' and z != 'ö' and z != 'p' and z != 'r' and z != 's' and z != 'ş' and z != 't' and z != 'u' and z != 'ü' and z != 'v' and z != 'y' and z != 'z' and z != 'x' and z != 'q' and z != 'w'
            if eleman is True:
                delta = float(y)**2-4*float(x)*float(z)
                x1 = (-float(y)-delta**0.5)/(2*float(x))
                x2 = (-float(y)+delta**0.5)/(2*float(x))
                print("İlk kök : {}\nİkinci kök : {}".format(
                    x1, x2))  # Denklem Kök Bulma
            else:
                print("Geçersiz giriş.. 5 saniye içinde kapanacak..")
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

        elif process == '11':
            x = input("Sayıyı giriniz: ")
            x = x.lower()
            y = input("Logaritma tabanını giriniz: ")
            y = y.lower()
            eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w' and y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w'
            if eleman is True:
                print(msj.format(math.log(float(x), float(y))))  # ? Logaritma
            else:
                print("Geçersiz giriş.. 5 saniye içinde kapanacak..")
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

        elif process == '12':
            x = input("Trigonometrik fonksiyonu giriniz: ")
            y = float(input("Dereceyi giriniz: "))  # Trigonometri

            if x == 'sin':
                if y == 0 or y == 180 or y == 360:
                    print(msj.format('0'))
                elif y == 90:
                    print(msj.format('1'))
                elif y == 270:
                    print(msj.format('-1'))
                else:
                    siny = math.sin(math.radians(y))
                    print(siny)

            elif x == 'cos':
                if y == 0 or y == 360:
                    print(msj.format('1'))
                elif y == 90 or y == 270:
                    print(msj.format('0'))
                elif y == 180:
                    print(msj.format('-1'))

                else:
                    cosy = math.cos(math.radians(y))
                    print(msj.format(cosy))

            elif x == 'tan':
                if y == 0 or y == 180 or y == 360:
                    print(msj.format('0'))

                elif y == 90 or y == 270:
                    print(msj.format('∞'))

                else:
                    tany = math.tan(math.radians(y))
                    print(msj.format(tany))

            elif x == 'cot':
                if y == 90 or y == 270:
                    print(msj.format('0'))

                elif y == 0 or y == 180 or y == 360:
                    print(msj.format('∞'))

                else:
                    siny = math.sin(math.radians(y))
                    cosy = math.cos(math.radians(y))
                    coty = cosy/siny
                    print(msj.format(coty))
            else:
                print("Geçersiz giriş.. 5 saniye içinde kapanacak..")
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

        elif process == '13':
            print("=> Sadece ingilizce karakterler kullanınız. Aksi halde hatalarla karşılaşabilirsiniz.")
            time.sleep(1)
            x = input("Hacim, alan veya çevre bulma seçiniz: ")
            print("=> Eğer hacim seçtiysen, küp,küre veya silindir seçmelisin.")
            time.sleep(3)

            y = input(
                "Şekli seçiniz(kare,üçgen,dikdörtgen,çember, küp, küre, silindir): ")

            a = x.lower()
            b = y.lower()
            if a == 'alan' and b == 'kare':
                x = input("Bir kenar uzunluğunu giriniz: ")
                x = x.lower()
                eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w'
                if eleman is True:
                    area1 = float(x)**2
                    print(msj.format(area1))
                else:
                    print("Geçersiz giriş.. 5 saniye içinde kapanacak..")
                    print('5..')
                    time.sleep(1)
                    print('4..')
                    time.sleep(1)
                    print('3..')
                    time.sleep(1)
                    print('2..')
                    time.sleep(1)
                    print('1..')
                    time.sleep(1)
                    quit()

            elif a == 'alan' and b == 'üçgen':
                x = input("Taban uzunluğunu giriniz: ")
                x = x.lower()
                y = input("Yüksekliğini giriniz: ")
                y = y.lower()
                eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w' and y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w'
                if eleman is True:
                    area2 = float(x)*float(y)/2
                    print(msj.format(area2))
                else:
                    print("Geçersiz giriş.. 5 saniye içinde kapanacak..")
                    print('5..')
                    time.sleep(1)
                    print('4..')
                    time.sleep(1)
                    print('3..')
                    time.sleep(1)
                    print('2..')
                    time.sleep(1)
                    print('1..')
                    time.sleep(1)
                    quit()

            elif a == 'alan' and b == 'dikdörtgen':
                x = input("Uzun kenarı giriniz: ")
                x = x.lower()
                y = input("Kısa kenarı giriniz: ")
                y = y.lower()
                eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w' and y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w'
                if eleman is True:
                    area3 = float(x)*float(y)
                    print(msj.format(area3))
                else:
                    print("Geçersiz giriş.. 5 saniye içinde kapanacak..")
                    print('5..')
                    time.sleep(1)
                    print('4..')
                    time.sleep(1)
                    print('3..')
                    time.sleep(1)
                    print('2..')
                    time.sleep(1)
                    print('1..')
                    time.sleep(1)
                    quit()

            elif a == 'alan' and b == 'çember':
                x = input("Yarıçap değerini giriniz: ")
                x = x.lower()
                eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w'
                if eleman is True:

                    area4 = math.pi*float(x)*float(x)
                    print(msj.format(area4))
                else:
                    print("Geçersiz giriş.. 5 saniye içinde kapanacak..")
                    print('5..')
                    time.sleep(1)
                    print('4..')
                    time.sleep(1)
                    print('3..')
                    time.sleep(1)
                    print('2..')
                    time.sleep(1)
                    print('1..')
                    time.sleep(1)
                    quit()

            elif a == 'çevre' and b == 'kare':
                x = input("Bir kenar uzunluğunu giriniz: ")
                x = x.lower()
                eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w'
                if eleman is True:
                    perimeter1 = 4*float(x)
                    print(msj.format(perimeter1))
                else:
                    print("Geçersiz giriş.. 5 saniye içinde kapanacak..")
                    print('5..')
                    time.sleep(1)
                    print('4..')
                    time.sleep(1)
                    print('3..')
                    time.sleep(1)
                    print('2..')
                    time.sleep(1)
                    print('1..')
                    time.sleep(1)
                    quit()

            elif a == 'çevre' and b == 'üçgen':
                x = input("1.kenar uzunluğunu giriniz: ")
                x = x.lower()
                y = input("2.kenar uzunluğunu giriniz: ")
                y = y.lower()
                z = input("3.kenar uzunluğunu giriniz: ")
                z = z.lower()
                eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w' and y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w' and z != 'a' and z != 'b' and z != 'c' and z != 'ç' and z != 'd' and z != 'e' and z != 'f' and z != 'g' and z != 'ğ' and z != 'h' and z != 'i' and z != 'j' and z != 'k' and z != 'l' and z != 'm' and z != 'n' and z != 'o' and z != 'ö' and z != 'p' and z != 'r' and z != 's' and z != 'ş' and z != 't' and z != 'u' and z != 'ü' and z != 'v' and z != 'y' and z != 'z' and z != 'x' and z != 'q' and z != 'w'
                if eleman is True:

                    perimeter2 = float(x)+float(y)+float(z)
                    print(msj.format(perimeter2))
                else:
                    print("Geçersiz giriş.. 5 saniye içinde kapanacak..")
                    print('5..')
                    time.sleep(1)
                    print('4..')
                    time.sleep(1)
                    print('3..')
                    time.sleep(1)
                    print('2..')
                    time.sleep(1)
                    print('1..')
                    time.sleep(1)
                    quit()

            elif a == 'çevre' and b == 'dikdörtgen':
                x = input("Uzun kenarı giriniz: ")
                x = x.lower()
                y = input("Kısa kenarı giriniz: ")
                y = y.lower()
                eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w' and y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w'
                if eleman is True:
                    perimeter3 = 2*(float(x)+float(y))
                    print(msj.format(perimeter3))
                else:
                    print("Geçersiz giriş.. 5 saniye içinde kapanacak..")
                    print('5..')
                    time.sleep(1)
                    print('4..')
                    time.sleep(1)
                    print('3..')
                    time.sleep(1)
                    print('2..')
                    time.sleep(1)
                    print('1..')
                    time.sleep(1)
                    quit()

            elif a == 'çevre' and b == 'çember':
                x = input("Yarıçap değerini giriniz: ")
                x = x.lower()
                eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w'
                if eleman is True:
                    perimeter4 = 2*math.pi*float(x)
                    print(msj.format(perimeter4))
                else:
                    print("Geçersiz giriş.. 5 saniye içinde kapanacak..")
                    print('5..')
                    time.sleep(1)
                    print('4..')
                    time.sleep(1)
                    print('3..')
                    time.sleep(1)
                    print('2..')
                    time.sleep(1)
                    print('1..')
                    time.sleep(1)
                    quit()

            elif a == 'hacim' and b == 'küp':
                x = input("Bir kenar uzunluğunu giriniz: ")
                x = x.lower()
                eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w'
                if eleman is True:
                    volume1 = float(x)**3
                    print(msj.format(volume1))
                else:
                    print("Geçersiz giriş.. 5 saniye içinde kapanacak..")
                    print('5..')
                    time.sleep(1)
                    print('4..')
                    time.sleep(1)
                    print('3..')
                    time.sleep(1)
                    print('2..')
                    time.sleep(1)
                    print('1..')
                    time.sleep(1)
                    quit()

            elif a == 'hacim' and b == 'küre':
                x = input("Yarıçap uzunluğunu giriniz: ")
                x = x.lower()
                eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w'
                if eleman is True:
                    volume2 = 4/3*math.pi*float(x)**3
                    print(msj.format(volume2))
                else:
                    print("Geçersiz giriş.. 5 saniye içinde kapanacak..")
                    print('5..')
                    time.sleep(1)
                    print('4..')
                    time.sleep(1)
                    print('3..')
                    time.sleep(1)
                    print('2..')
                    time.sleep(1)
                    print('1..')
                    time.sleep(1)
                    quit()

            elif a == 'hacim' and b == 'silindir':
                x = input("Yarıçap uzunluğunu giriniz: ")
                y = input("Yüksekliği giriniz: ")
                x = x.lower()
                y = y.lower()
                eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w' and y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w'
                if eleman is True:
                    volume3 = math.pi*float(x)**2*float(y)
                    print(msj.format(volume3))
                else:
                    print("Geçersiz giriş.. 5 saniye içinde kapanacak..")
                    print('5..')
                    time.sleep(1)
                    print('4..')
                    time.sleep(1)
                    print('3..')
                    time.sleep(1)
                    print('2..')
                    time.sleep(1)
                    print('1..')
                    time.sleep(1)
                    quit()

            elif a == 'alan' and b == 'küp':
                x = input("Bir kenar uzunluğunu giriniz: ")
                eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w'
                if eleman is True:
                    area5 = 6*float(x)**2
                    print(msj.format(area5))
                else:
                    print("Geçersiz giriş.. 5 saniye içinde kapanacak..")
                    print('5..')
                    time.sleep(1)
                    print('4..')
                    time.sleep(1)
                    print('3..')
                    time.sleep(1)
                    print('2..')
                    time.sleep(1)
                    print('1..')
                    time.sleep(1)
                    quit()

            elif a == 'alan' and b == 'küre':
                x = input("Yarıçap değerini giriniz: ")
                eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w'
                if eleman is True:
                    area6 = 4*float(x)**2*math.pi
                    print(msj.format(area6))
                else:
                    print("Geçersiz giriş.. 5 saniye içinde kapanacak..")
                    print('5..')
                    time.sleep(1)
                    print('4..')
                    time.sleep(1)
                    print('3..')
                    time.sleep(1)
                    print('2..')
                    time.sleep(1)
                    print('1..')
                    time.sleep(1)
                    quit()

            elif a == 'alan' and b == 'silindir':
                x = input("Yarıçap değerini giriniz: ")
                y = input("Yüksekliği giriniz: ")
                x = x.lower()
                y = y.lower()
                eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w' and x != '-' and y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w' and y != '-'
                if eleman is True:
                    area7 = 2*math.pi*float(x)*(float(x)+float(y))
                    print(msj.format(area7))

                else:
                    print("Geçersiz giriş.. 5 saniye içinde kapanacak..")
                    print('5..')
                    time.sleep(1)
                    print('4..')
                    time.sleep(1)
                    print('3..')
                    time.sleep(1)
                    print('2..')
                    time.sleep(1)
                    print('1..')
                    time.sleep(1)
                    quit()

            else:
                print("Geçersiz giriş.. 5 saniye içinde kapanacak..")
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

        elif process == '14':
            x = input("Bölünen sayıyı giriniz: ")
            x = x.lower()
            y = input("Bölen sayıyı giriniz:  ")
            y = y.lower()
            eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w' and y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w'
            if eleman is True:
                remainder = float(x) % float(y)
                print(msj.format(remainder))
            else:
                print("Geçersiz giriş.. 5 saniye içinde kapanacak..")
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

        elif process == '15':
            translator = Translator()
            print('=> Çevirmek istediğiniz metni tek satır halinde giriniz.')
            time.sleep(2)
            a = input("Çevirmek istediğiniz metni giriniz: ")
            print('=> Sadece bazı diller aktif çalışıyor. ')
            time.sleep(1.5)
            print("""
            Aşağıda dil kodlarını görebilirsiniz;
            pt => Portekizce, zh-cn => Çince, de => Almanca, es => İspanyolca, en => İngilizce, ru => Rusça, fr => Fransızca, tr => Türkçe, ko => Korece, ja => Japonca, it => İtalyanca, ar => Arapça 
            """)
            time.sleep(1.5)
            b = input("Metninizi hangi dile çevirmek istediğinizi seçiniz: ")
            if b == 'pt' or b == 'zh-cn' or b == 'de' or b == 'es' or b == 'en' or b == 'ru' or b == 'fr' or b == 'tr' or b == 'ko' or b == 'ja' or b == 'it' or b == 'ar':

                translation = translator.translate(a, dest=b)
                print(f"{translation.text} ({translation.dest})")
            else:
                print('Bu dil aktif değil.. 5 saniye içinde kapanacak..')
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

        elif process == '16':
            a = random.randint(0, 100)
            msg30 = "PARA DÖNÜYORR..."
            if a <= 50:
                print(msg30 + 'TURA KAZANDI.')

            elif a >= 51:
                print(msg30 + 'YAZI KAZANDI.')

            else:
                print("Geçersiz giriş.. 5 saniye içinde kapanacak..")
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

        elif process == '17':
            key = "https://api.binance.com/api/v3/ticker/price?symbol="
            currencies = ["BTCUSDT", "DOGEUSDT", "LTCUSDT"]
            j = 0
            for i in currencies:
                url = key+currencies[j]
                data = requests.get(url)
                data = data.json()
                j = j+1
                print(f"{data['symbol']} fiyatı: {data['price']}")

        elif process == '18':
            print("=> Para birimlerini doğru girmelisiniz. Aksi takdirde bazı hatalarla karşılaşabilirsiniz!")
            initial_currency = input("Çevirmek istediğiniz para birimini giriniz: ")
            target_currency = input("Hedef para birimini giriniz: ")
            while True:
                try:
                    amount = float(input("Miktarı giriniz: "))
                except:
                    print("Miktar bir sayı olmalıdır!")
                    continue
                if not amount > 0:
                    print("Miktar 0'dan büyük olmalıdır..")
                    continue
                else:
                    break
            url = "https://api.apilayer.com/fixer/convert?to=" + target_currency + \
                "&from=" + initial_currency + "&amount=" + str(amount)

            payload = {}
            headers = {
                "apikey": "o6SGccKw9pmrnyipI4m6yf71VhQKkl1z"
            }

            response = requests.request("GET", url, headers=headers, data=payload)

            status_code = response.status_code

            if status_code != 200:
                print("Bir problem oluştu. Lütfen tekrar deneyin..")
                quit()

            result = response.json()
            print("Çevirme Sonucu => " + str(result["result"]))

        elif process == '19':
            x = random.randint(0, 100)
            timer = 0
            time.sleep(1)
            y = input("Tahmin ettiğiniz sayıyı giriniz (7 hakkınız var..) => ")
            y = y.lower()
            eleman = y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w'
            if eleman is True:

                while True:
                    if int(y) == int(x):
                        print("=> Oyunu kazandınız. Tebrikler..")
                        print("=> {} kez tahmin ettiniz.".format(timer+1))
                        break

                    if timer == 6:
                        print("=> Oyunu kaybettiniz. Tekrar deneyin!")
                        break

                    elif int(y) > int(x):
                        print("Daha DÜŞÜK bir sayı söylemelisiniz!..")
                        y = input("Tahmin ettiğiniz sayıyı tekrar giriniz => ")
                        y = y.lower()
                        eleman = y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w'
                        if eleman is True:
                            timer = timer+1
                        else:
                            print("Geçersiz giriş.. 5 saniye içinde kapanacak..")
                            print('5..')
                            time.sleep(1)
                            print('4..')
                            time.sleep(1)
                            print('3..')
                            time.sleep(1)
                            print('2..')
                            time.sleep(1)
                            print('1..')
                            time.sleep(1)
                            quit()

                    elif int(y) < int(x):
                        print("Daha YÜKSEK bir sayı söylemelisiniz!..")
                        y = input("Tahmin ettiğiniz sayıyı tekrar giriniz => ")
                        y = y.lower()
                        eleman = y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w'
                        if eleman is True:
                            timer = timer+1
                        else:
                            print("Geçersiz giriş.. 5 saniye içinde kapanacak..")
                            print('5..')
                            time.sleep(1)
                            print('4..')
                            time.sleep(1)
                            print('3..')
                            time.sleep(1)
                            print('2..')
                            time.sleep(1)
                            print('1..')
                            time.sleep(1)
                            quit()

        elif process == '20':
            print("=> EKOK en küçük ortak kat anlamına gelir. EBOB en büyük ortak bölen anlamına gelir.")
            time.sleep(2)
            x = input("İlk sayıyı giriniz: ")
            x = x.lower()
            time.sleep(1)
            y = input("İkinci sayıyı giriniz: ")
            y = y.lower()
            eleman = x != 'a' and x != 'b' and x != 'c' and x != 'ç' and x != 'd' and x != 'e' and x != 'f' and x != 'g' and x != 'ğ' and x != 'h' and x != 'i' and x != 'j' and x != 'k' and x != 'l' and x != 'm' and x != 'n' and x != 'o' and x != 'ö' and x != 'p' and x != 'r' and x != 's' and x != 'ş' and x != 't' and x != 'u' and x != 'ü' and x != 'v' and x != 'y' and x != 'z' and x != 'q' and x != 'x' and x != 'w' and y != 'a' and y != 'b' and y != 'c' and y != 'ç' and y != 'd' and y != 'e' and y != 'f' and y != 'g' and y != 'ğ' and y != 'h' and y != 'i' and y != 'j' and y != 'k' and y != 'l' and y != 'm' and y != 'n' and y != 'o' and y != 'ö' and y != 'p' and y != 'r' and y != 's' and y != 'ş' and y != 't' and y != 'u' and y != 'ü' and y != 'v' and y != 'y' and y != 'z' and y != 'x' and y != 'q' and y != 'w'

            if eleman is True:
                print("EKOK değeri => {}".format(
                    math.lcm(int(x), int(y))))
                time.sleep(1)
                print("EBOB değeri => {}".format(
                    math.gcd(int(x), int(y))))
            else:
                print("Geçersiz giriş.. 5 saniye içinde kapanacak...")
                print('5..')
                time.sleep(1)
                print('4..')
                time.sleep(1)
                print('3..')
                time.sleep(1)
                print('2..')
                time.sleep(1)
                print('1..')
                time.sleep(1)
                quit()

        else:
            print("Geçersiz giriş.. 5 saniye içinde kapanacak...")
            print('5..')
            time.sleep(1)
            print('4..')
            time.sleep(1)
            print('3..')
            time.sleep(1)
            print('2..')
            time.sleep(1)
            print('1..')
            time.sleep(1)
            quit()    

else:
        print("Geçersiz giriş.. 5 saniye içinde kapanacak...")
        print('5..')
        time.sleep(1)
        print('4..')
        time.sleep(1)
        print('3..')
        time.sleep(1)
        print('2..')
        time.sleep(1)
        print('1..')
        time.sleep(1)
        quit()
