# -*- coding: utf-8 -*-
import sys

def rectangles(f,a,b,n):
#Méthode des rectangles:
	S=0
	for i in xrange (0,n):
		xi=a+(b-a)*i/float (n)
		xj=a+(b-a)*(i+1)/float (n)
		S+=f((xi+xj)/2.0)*(xj-xi)
	return S


def trapezes(f,a,b,n):
#Methode des trapezes
	S=0
	for i in xrange(0,n):
		xi=a+(b-a)*i/float (n)
		xj=a+(b-a)*(i+1)/float (n)
		S+=(f(xi)+f(xj))/2.0*(xj-xi)
	return S

def simpson(f,a,b,n):
#Methode de simpson
	S=0
	for i in xrange(0,n):
		xi=a+(b-a)*i/float (n)
		xj=a+(b-a)*(i+1)/float (n)
		S+= (xj-xi) * (f(xi)+4*f((xi+xj)/2.0)+f(xj)) /6.0
	return S

def fn(x):
#fonction a integrer
	action = sys.argv[1]
	return action


def main(): 
	if len(sys.argv) < 2:
    		print("Précisez une action en paramètre")
		sys.exit(1)
	print "par rectangles: ", rectangles(fn,0.,5.,100);
	print "par trapèzes: ", trapezes(fn,0.,5.,100);
	print "par Simpson: ", simpson(fn,0.,5.,100);

main() 
