
import math

class vec:
	def __init__(self, *coords):
		self.coords = coords
	def __neg__(self):
		return (-1)*self
	def __add__(self, other): # Addition
		return vec(*[self.coords[i]+other.coords[i] for i in range(len(self.coords))])
	def __radd__(self, other): # Addition
		return vec(*[self.coords[i]+other.coords[i] for i in range(len(self.coords))])
	def __sub__(self, other): # Subtraction
		return vec(*[self.coords[i]-other.coords[i] for i in range(len(self.coords))])
	def __rsub__(self, other): # Subtraction
		return vec(*[self.coords[i]-other.coords[i] for i in range(len(self.coords))])
	def __mul__(self, other):
		if type(other) == type(self): # Dot product
			return sum([self.coords[i]*other.coords[i] for i in range(len(self.coords))])
		else: # Scalar multiplication
			return vec(*[self.coords[i]*other for i in range(len(self.coords))])
	def __rmul__(self, other):
		if type(other) == type(self): # Dot product
			return sum([self.coords[i]*other.coords[i] for i in range(len(self.coords))])
		else: # Scalar multiplication
			return vec(*[self.coords[i]*other for i in range(len(self.coords))])
	def __xor__(self, other): # Cross product
		return vec(self.coords[1]*other.coords[2]-self.coords[2]*other.coords[1],
			   self.coords[2]*other.coords[0]-self.coords[0]*other.coords[2],
			   self.coords[0]*other.coords[1]-self.coords[1]*other.coords[0])
	def __truediv__(self, other): # Scalar division
		return vec(*[self.coords[i]/other for i in range(len(self.coords))])
	def __getitem__(self, index): # Support indexing
		return self.coords[index]
	def __abs__(self): # Length
		return math.sqrt(self*self)
	def normalize(self):
		return self/abs(self)
