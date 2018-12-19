#!/usr/bin/env python3
# -*- coding: utf-8 -*-

Continue = "y"
while Continue == "y" :
    list = [float(input("input your height(m) :\n")),float(input("input your weight(kg) :\n"))]
    BMI=list[1]/list[0]**2
    print("your BMI is ",BMI)
    print(" you are ",end = "" )
    if BMI < 18.5 :
        print(" thin")
    elif 18.5 <= BMI < 25 :
        print("health")
    elif 25 <= BMI < 28 :
        print("fat")
    elif 28<= BMI <32 :
        print("very fat")
    elif 32< BMI :
        print("too fat")
    Continue = input("continue ? : (y"+r"\n)"+"\n")