#!/usr/bin/env python -tt
# Description: Python Module to implement many functions related to set and relations.

# Checks is set R is a valid relation on set A and B
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
# return True is set R is reflexive relation on set A
def isReflexive(R, A):
	# if R is not a valid relation on A
	# return False
	if not isRelation(R, A, A):
		return False	
	# Now, For R to be a reflexive relation on set A,
	# Identity Relation on set A must be a subset of R
	I = identity(A)
	if I.issubset(R):
		return True
	else:
		return False
