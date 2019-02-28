import math
from vector import vec

class quat:
	def __init__(self, s, v):
		self.s = s
		self.v = v
	def __neg__(self, other):
		return (-1)*self
	def __invert__(self, other):
		return quat(self.s, -self.v)
	def __add__(self, other):
		return quat(self.s+other.s, self.v+other.v)
	def __sub__(self, other):
		return quat(self.s-other.s, self.v-other.v)
	def __mul__(self, other):
		if type(other) == type(self):
			return quat((self.s*other.s)-(self.v*other.v),
						(self.s*other.v)+(self.v*other.s)+(self.v^other.v))
		if type(other) == type(vec(0,0,0)):
			return self*quat(0,other)
		else:
			return quat(other*self.s, other*self.v)
	def __truediv__(self, other):
		return quat(self.s/other, self.v/other)
	def __abs__(self):
		return math.sqrt(self.s+abs(self.v)**2)
	def angle(self):
		return 2*math.acos(self.s)
	def axis(self):
		return self.v.normalize()
	def rotate(self, other):
		if type(other) == type(self):
			return self*other*(~self)
		else:
			return self*other*(~self)
	def normalize(self):
		return self/abs(self)
