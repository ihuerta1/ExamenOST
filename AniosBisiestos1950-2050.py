#!/usr/bin/python
# -*- coding: utf-8 -*-
# By: Nacho
def aniobisiesto(inicio):
	i = inicio
	j = inicio + 101
	while i<j:
	 if i%4 == 0 and i%100 != 0 or i%400 == 0:
		print("El año "+str(i)+" es bisiesto " )
	 i += 1
aniobisiesto(1950)

