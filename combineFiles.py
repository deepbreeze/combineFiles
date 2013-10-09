import os
import shutil

def dir_list(dir_name, subdir, *args):
    fileList = []
    for file in os.listdir(dir_name):
        dirfile = os.path.join(dir_name, file)
        if os.path.isfile(dirfile):
            fileList.append(dirfile)     
    return fileList

def combine_files(fileList, fn):
    f = open(fn, 'w')
    for file in fileList:
        print 'Writing file %s' % file
        f.write(open(file).read())
    f.close()
 
if __name__ == '__main__':
    search_dir = "C:\directory"
    fn = "output.txt"
    combine_files(dir_list(search_dir, False, 'txt'), fn)
    try:
        f = open('output.txt','r')
        try:
            lines = f.readlines()
            lines.sort()
            f.close()
            f = open('output.txt','w')
            f.writelines(lines)
        finally:
            f.close()
    except IOError:
        pass

def CleanDir( Dir ):
    if os.path.isdir( Dir ):
        paths = os.listdir( Dir )
        for path in paths:
            filePath = os.path.join( Dir, path )
            if os.path.isfile( filePath ):
                try:
                    os.remove( filePath )
                except os.error:
                    autoRun.exception( "remove %s error." %filePath )
            elif os.path.isdir( filePath ):
                if filePath[-4:].lower() == ".svn".lower():
                    continue
                shutil.rmtree(filePath,True)
    return True

Dir = "C:\directory"
CleanDir(Dir)


