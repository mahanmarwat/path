import re, os, sys
import stat
import shutil
import urllib.parse

__version__ = '0.1.0'

# Properties constants.
SIZE  = 6 # stat.ST_SIZE
ATIME = 7 # stat.ST_ATIME
MTIME = 8 # stat.ST_MTIME
CTIME = 9 # stat.ST_CTIME

# Access constants.
EXIST      = 0 # os.F_OK
EXECUTABLE = 1 # os.X_OK
WRITABLE   = 2 # os.W_OK
READABLE   = 4 # os.R_OK

# Separators constants.
CURDIR  = os.curdir
PARDIR  = os.pardir
PATHSEP = os.pathsep
DIRSEP  = os.sep
EXTSEP  = os.extsep

class PathError(Exception): pass

# General functions.
cwd = os.getcwd
chd = os.chdir

# Properties as functions.
size  = lambda path: stat(path)[SIZE]
atime = lambda path: stat(path)[ATIME]
mtime = lambda path: stat(path)[MTIME]
ctime = lambda path: stat(path)[CTIME]

# Path Components as functions.
full     = lambda path: os.path.abspath(path)                   # Full path (Absolute path)
#path    = lambda path: path                                    # Given path
drive    = lambda path: os.path.splitdrive(path)[0]             # Drive part
dir      = lambda path: os.path.dirname(path)                   # Path without filename
filedir  = lambda path: os.path.basename(os.path.dirname(path)) # File parent dir
file     = lambda path: os.path.basename(path)                  # Name with extension
name     = lambda path: os.path.splitext(file(path))[0]         # Name without extension
ext      = lambda path: os.path.splitext(path)[1]               # Extension

# General path functions.
join   = os.path.join
stat   = lambda path: _stat()(path)
list   = lambda path, pattern='': [item for item in os.listdir(path) if re.match(pattern, item)]
dirs   = lambda path, pattern='': [dir  for dir  in list(path, pattern) if isdir(join(path, dir))]
files  = lambda path, pattern='': [file for file in list(path, pattern) if isfile(join(path, file))]

# Todo: Add ownership argument.
def chprop(path, mode=None, times=None):
    if mode:  os.chmod(path, mode)
    if times: os.utime(path, times)

# Todo: Complete it.
def walk(): return NotImplemented

# Conditional path functions.
ispath  = lambda path, access: os.access(path, access)
isdir   = os.path.isdir
isfile  = os.path.isfile
islink  = os.path.islink
ismount = os.path.ismount

def isempty(path):
    if isdir(path):
        return os.listdir(path) == []
    elif isfile(path):
        return size(path) == 0
    else:
        raise PathError()

# High Level path functions.
move   = lambda oldpath, newpath: shutil.move(oldpath, newpath)

# Todo: Add renames like functionality also.
rename = lambda oldpath, newpath: os.rename(oldpath, newpath)

def copy(oldpath, newpath):
    if isdir(oldpath):
        if isempty(oldpath):
            shutil.copy2(oldpath, newpath)
        else:
            shutil.copytree(oldpath, newpath)
    elif isfile(oldpath):
        shutil.copy2(oldpath, newpath)
    else:
        raise PathError()

# Todo: Add mkdirs like functionality also.
def create(path, type='dir', mode=0o777):
    type = type.lower()
    if type == 'dir':
        os.mkdir(path, mode)
    elif type == 'file':
        with open(path, 'w') as file:
            os.chmod(file, mode)
    else:
        raise PathError()

# Todo: Add rmdirs like functionality also.    
def delete(path):
    if isdir(path):
        if isempty(path):
            os.rmdir(path)
        else:
            shutil.rmtree(path)
    elif isfile(path):
        os.remove(path)
    elif islink(path):
        os.unlink(path)
    else:
        raise PathError()

class Properties:
    """Properties of a path."""
    def __init__(self, path):
        self.size  = size(path)
        self.atime = atime(path)
        self.mtime = mtime(path)
        self.ctime = ctime(path)


class Components:
    """Components of a path."""
    def __init__(self, path):
        self.full    = full(path)
        self.path    = path
        self.drive   = drive(path)
        self.dir     = dir(path)
        self.filedir = filedir(path)
        self.file    = file(path)
        self.name    = name(path)
        self.ext     = ext(path)


class Path:
    """Path object, represent a path to OS file or dir."""

    def __init__(self, path):
        # Path Components.
        self.full    = full(path)
        self.path    = path
        self.drive   = drive(path)
        self.dir     = dir(path)
        self.filedir = filedir(path)
        self.file    = file(path)
        self.name    = name(path)
        self.ext     = ext(path)
        # Path Properties.
        try:
            self.size  = size(path)
        except OSError:
            self.size  = None
        try:
            self.atime = atime(path)
        except OSError:
            self.atime = None
        try:
            self.mtime = mtime(path)
        except OSError:
            self.mtime = None
        try:
            self.ctime = ctime(path)
        except OSError:
            self.ctime = None

    def __str__(self):
        return self.path

    # Todo: Complete it.
    def __add__(self, path):
        return join(self.path, path)

    # General path methods.
    def join(self, *path):
        return join(self.path, path)

    def stat(self):
        return stat(self.path)

    def list(self, pattern=''):
        return list(self.path, pattern)

    def dirs(self, pattern=''):
        return dirs(self.path, pattern)

    def files(self, pattern=''):
        return files(self.path, pattern)

    def chprop(self, mode=None, times=None):
        chprop(self.path, mode, times)
        return self
    
    # Todo: Complete it.
    def walk():
        return walk()

    # Conditional path methods.
    def ispath(self, access):
        return ispath(self.path, access)

    def isdir(self):
        return isdir(self.path)

    def isfile(self):
        return isfile(self.path)
    
    def islink(self):
        return islink(self.path)

    def ismount(self):
        return ismount(self.path)

    def isempty(self):
        return isempty(self.path)

    # High Level path methods.
    def move(self, newpath):
        move(self.path, newpath)
        return self

    def rename(self, newpath):
        rename(self.path, newpath)
        return self

    def copy(self, newpath):
        copy(self.path, newpath)
        return self

    def create(self, type='dir', mode=0o777):
        create(self.path, type, mode)
        return self

    def delete(self):
        delete(self.path)
        return self


class HttpPath(Path):
    """Path object, represent a path to URL"""
    def __init__(self, url):
        super(HttpPath, self).__init__(urllib.parse.urlparse(url).path)

# Helper functions for this module internal use.
def _stat():
    """Helper function for stat function."""
    if   hasattr(os, 'stat'): return os.stat
    elif hasattr(os, 'lstat'): return os.lstat
