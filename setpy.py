#!/usr/bin/env python -tt
# Description: Python Module to implement many functions related to set and relations.

# Checks is R is a relation on set A and B
# return True if R is a valid relation on A and B
# else return False
def isRelation(R, A, B):
	import itertools as i
	# For R to be a realtion on A and B
	# R must ge a subset of A * B
	AxB = set(i.product(A,B))
	if R.issubset(AxB):
		return True
	else:
		return False

# Return Identity Relation on a given set A
def identity(A):
	I = set();
	for element in A:
		I.add((element,element))
	return I
	
# Checks if a given set is reflexive
def isReflexive(R, A):
	# For R to be a reflexive relation on A,
	# Identity Relation on A must be a subset of R
	I = identity(A)
	if I.issubset(A):
		return True
	else:
		return False
