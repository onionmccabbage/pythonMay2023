import sys

print( sys.path ) # shows a list of all the places Python will look for imports
sys.path.append('path to anotehr location')

# we can see the platform and version
print( sys.platform ) # even on 64 bit Windows it says win32
print( sys.version )
print( sys.version_info )