#!/usr/bin/env python
"""
This module contains class that can find the square root of a given number
using newtons method.

This module also contains some test function to test the convergence of the
given number.

:date: 26 Mar, 2015
"""
from __future__ import division

__version__ = "0.1.0"
__author__ = "Srikanth Narayanan"

#import necessary libraries


class Newton(object):
    """
    This class creates an object that solves the square root of a given number
    using newtons method
    """
    def __init__(self, initial_guess=1, itr=20, tol=1e-14, debug=False, 
                 val=None, ext_func=False, fx=None, fxprime=None):
        """
        This is a constructor to load the object with a given number.

        :param val: The val whose square to be calculated.
        :param itr: number of iterations, Default value can be overidden.
        :param tol: Tolerance value to be met by the solver
        """
        self.itr = itr
        self.tol = tol
        self.debug = debug
        self.ini_gus = initial_guess
        self.ext_func = ext_func
        if self.ext_func:
            if fx and fxprime is not None:
                self.fx_user = fx
                self.fx_prime_user = fxprime
            else:
            	print "fx and fxprime definition cannot be none when ext_func is True"
        else:
        	self.val = val
                
    
    def find_root(self):
        """
        This method uses newtons method to find roots
        """
        # set initial guess
        x = self.ini_gus
        
        if self.debug:
            print "Initial guess: x = %22.15E" % x
        
        if self.ext_func:
        	my_fx = self.fx_user
        	my_fxprime = self.fx_prime_user
        else:
        	my_fx = self.f_sqrt
        	my_fxprime = self.fprime_sqrt
        
        # Newton iteration to find a zero of f(x) 
        for ii in range(self.itr):
            # evaluate func and derivative
            fx = my_fx(x)
            fxprime = my_fxprime(x)
            if abs(fx) < self.tol:
                self.sqrt = x
                self.iter_consumed = ii + 1
                return x, self.iter_consumed
                break

            # compute Newton increment x
            deltax = fx/fxprime
            # update x
            x = x - deltax
            
            if self.debug:
                print "After %d iterations, x = %22.15E" %(ii+1, x)
        
        # check for convergence
        if ii == self.itr:
            fx = my_fx(x)
            if abs(fx) > self.tol:
                print "*** Warning: has not yet converged"
        
        self.iter_consumed = ii + 1
        return x, self.iter_consumed
    
    def f_sqrt(self, x):
        """
        This method defines the square root function
        """
        return x**2 - self.val
    
    def fprime_sqrt(self, x):
        """
        This method defines the derivative of the f_sqrt function
        """
        return 2*x

    def test1(self):
        """
        Test Newton iteration for the square root with different initial
        conditions.
        """
        self.val = 4
        self.debug = True
        for x0 in [1., 2., 100.]:
            print " "  # blank line
            self.ini_gus = x0
            x,iters = self.find_root()
            print "solve returns x = %22.15e after %i iterations " % (x,iters)
            fx = self.f_sqrt(x)
            fpx = self.fprime_sqrt(x)
            print "the value of f(x) is %22.15e" % fx
            assert abs(x-2.) < 1e-14, "*** Unexpected result: x = %22.15e"  % x
