"""Development file

When I think about a new feature of path module. I first add the
feature to this file. Then if the new feature sound good. I add it to
the path module. if it didn't I discard it.

"""

is_space(path, size) = has_space(path, size) # Check if there is a space on disk.
stat = usage = statistics = space

islink
ismount
#add chown to chprop function.

#create aliases for the high level functions like move, delete, copy, create etc
#the aliases are mv, del, cp, cr etc

# Now we use.
path.zip
# Not it is better to use.
path.file.zip

path.parts # parts of a path i.e c:\\hello\\world.py ['c:\\', 'hello', 'world.py']
# may be name it path.comp but it is not good.

path('c:\\') + 'hello' + 'world.py'

print(path(r'c:\hello\world.py'))
c:\\hello\\world.py

path.parent # do not use it.

path.exists # do not use it.

# Add support to copy, move, rename etc of makedirs, renames etc like functionality.

root # \x\s\d\f.py in this x is the root dir.

# add humanize to ctime, atime etc

isvalid # check validity of a path

chprop = chprops = chmod + chstat

walk # walk like functionality.

remove = delete # alias
fullpath = full # alias
filename = file # alias

props = Properties(path)
props.size
...
comps = Components(path)
comps.full
...

# no nothing.
root, pathname, base, filepath, paths
