print [x * x for x in range(1, 11)]

print [x * x for x in range(1, 11) if x % 2 == 0]

print [m + n for m in 'ABC' for n in 'XYZ']

import os
print [d for d in os.listdir('.')]

d = {
	'x': 'A', 
	'y': 'B', 
	'z': 'C'
}

for k, v in d.iteritems():
	print k, '=', v

print [k + '=' + v for k, v in d.iteritems()]

print [s.lower() for s in ['Hello', 'World', 'IBM', 'Apple']]
