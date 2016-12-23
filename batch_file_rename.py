#batch file rename.py
#created: 2016-12-23

'''
This script change file extention of a given directory
rename one extension to another
file extension like .sh, .sql, .txt
'''

__author__ = 'l00280784'
__version__ = '0.0'

import os
import sys

def batch_rename_extension(directory, old_ext, new_ext):
    #go through all file and do that job
    for file in os.listdir(directory):
        #print "file:", file
        #get file extension
        file_ext = os.path.splitext(file)[1]
        #print "file extension:", file_ext
        #print "old extension:", old_ext
        #target extension
        if file_ext == old_ext:
            new_file = replaceExt(file, new_ext)
            #print "new file:", new_file
            os.rename(os.path.join(directory, file), os.path.join(directory, new_file))
    return


def replaceExt(file, new_ext):
    return os.path.splitext(file)[0] + new_ext


def main():
    directory = sys.argv[1]
    old_ext = sys.argv[2]
    new_ext = sys.argv[3]
    
    print "%s %s %s" %(directory, old_ext, new_ext)
    
    batch_rename_extension(directory, old_ext, new_ext)
    
    
    
if __name__ == '__main__':
    main()
    