#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains script to find the roots of the functions 
g1(x)=sin(x) and g2(x)=1−x*2
using newtons method.

This is evaluated by solving sin(x)=1−x2, or equivalently solving for zeros of the 
function f(x)=g1(x)−g2(x). This can be done using Newton’s method. 

:date: 28 Mar, 2015
"""
from __future__ import division

__version__ = "0.1.0"
__author__ = "Srikanth Narayanan"

# import all necessary libs
import numpy as np
import newton
import matplotlib.pyplot as plt

def f(x):
	"""
	This function returns the value of a functions whose intersection has to be found
	"""
	return x * np.cos(np.pi * x) - (1 - (0.6 * x ** 2))

def fprime(x):
	"""
	This function returns the derivative of f(x)
	"""
	return (-x * np.pi) * np.sin(np.pi * x) + np.cos(np.pi * x) + 1.2 * x

def find_intersect(debug=False):
	"""
	This is a sample program to find the intersection of g1(x) and g2(x)
	"""
	# setup initials
	ig = np.array([-2.2, -1.6, -0.8, 1.4])
	xx = np.zeros(np.shape(ig))
	iters = np.zeros(np.shape(ig))
	
	# loop over ig values
	for idx, val in enumerate(ig):
		# create a newton object
		intersect = newton.Newton(initial_guess=val, itr=20, debug=False, ext_func=True, 
								  fx=f, fxprime=fprime)
		roots = intersect.find_root()
		xx[idx] = roots[0]
		iters[idx] = roots[1]
		if debug:
			if roots[1] < 50:
				print "With initial guess x0 = %22.15e," %val
				print "      solve returns x = %22.15e after %d iterations" %(roots)

	# plot g1(x) and g2(x)
	plt.figure(1)
	plt.clf()
	x = np.linspace(-5,5,1000)
	y1 = x * np.cos(np.pi * x)
	y2 = 1 - 0.6 * x ** 2
	plt.plot(x, y1, 'b-', label='g1(x) = xcos(pix)')
	plt.plot(x, y2, 'r-', label='g2(x) = 1 - 0.6x^2')
	plt.plot(xx, 1 - 0.6*xx**2, 'ko', label='intersect')
	plt.legend(loc = 'best')
	plt.savefig('intersect.png')
    
    # Add data points  (polynomial should go through these points!)
