import ctypes
from ctypes import *
import numpy as np
lib = cdll.LoadLibrary('./libadder.so')

class Foo(object):

	def bar(self):
		count = 10;
		a = np.random.randint(count);
		pointer_arr = [np.ctypeslib.as_ctypes(array) for array in a]
		#pointer_arr = ctypes.ARRAY(ctypes.POINTER(ctypes.c_int), count)
		#a = (c_int * count)(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
		#lib.adder(a, count);
		lib.adder(pointer_arr, count);

def main():
	f = Foo();
	f.bar()

if __name__ == '__main__': main()
