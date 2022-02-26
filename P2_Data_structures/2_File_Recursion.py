import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    
    results=[]
    for file in os.listdir(path):
        #get all the files and directories under current path
        new_path=os.path.join(path,file)
        #print(new_path)
        # if current file is a file and it has the suffix we want to find, add to the results list
        if os.path.isfile(new_path) and new_path.endswith(suffix):
            results.append(new_path)
        # if current file is a folder, find files under the new folder, then extend the results/
        elif os.path.isdir(new_path):
            files_to_add=find_files(suffix, new_path)
            results.extend(files_to_add)
            #print('files_to_add',new_path,files_to_add)
            
    return results
    
    
path='./testdir'

suffix='.c'
print(find_files(suffix, path))

suffix='.h'
print(find_files(suffix, path))

suffix='.py'
print(find_files(suffix, path))


#print the files in the directory in which you are running this scrip, type: list
#print(os.listdir("."))
# Let us check if this file is indeed a file!
#print (os.path.isfile("./problem_1.py"))
# Does the file end with .py?
#print ("./problem_1.py".endswith(".py"))
    
    
