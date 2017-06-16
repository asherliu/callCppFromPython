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
#	f = Foo();
#	f.bar()
	import sys
	for fname in sys.argv[1:]:
		with open(fname, "rb") as f:
			(r, s, M, M_r_row, M_s_row, M_r_col, M_s_col, d_out, d_in, d_out_new, d_in_new) = pickle.load(f)
			print r;

if __name__ == '__main__': main()
