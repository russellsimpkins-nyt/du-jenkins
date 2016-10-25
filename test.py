import sys
f = open('/tmp/test.log', 'w')
o = sys.stdout
sys.stdout = f
sys.stderr = f

# something bad happened
message = "Something bad happened"
print message
sys.stdout = o
print message
exit(1)
