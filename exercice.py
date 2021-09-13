#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math


def average(a: float, b: float, c: float) -> float:
    return (a+b+c)/3


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    angle_rads = angle_degs*math.pi/180 + angle_mins*math.pi/180/60 + angle_secs*math.pi/180/3600
    return angle_rads


def to_degrees(angle_rads: float) -> tuple:
    angle_degs = math.floor(angle_rads*180/math.pi)
    angle_rads -= angle_degs*math.pi/180
    angle_mins = math.floor(angle_rads*180/math.pi*60)
    angle_rads -= angle_mins*math.pi/180/60
    angle_secs = angle_rads*180/math.pi*3600
    angle_rads -= angle_secs*math.pi/180/3600    
    return angle_degs,angle_mins,angle_secs


def to_celsius(temperature: float) -> float:
    return (temperature-32)/1.8


def to_farenheit(temperature: float) -> float:
    return temperature*1.8+32


def main() -> None:
    print(f"Moyenne des nombres 2, 4, 6: {average(2.1, 4.3, 6.5)}")

    print(f"Conversion de 180 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
