import subprocess
import os

perm = input('please input permission in numbers with 0 begining: ')
filepath = str(input('please input full file path,enter no if you would want to give a directory path: '))
folderpath = input('please input folder path,enter no if you have already entered a file path: ')


# subprocess.call('ifconfig wlan0 down',shell=True)
# subprocess.call('ifconfig wlan0 hw ether 00:11:22:33:44:55',shell=True)
# subprocess.call('ifconfig wlan0 up',shell=True)



def get_filepaths(directory,permission):
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root,filename)
            file_paths.append(filepath)  # Add it to the list.
            for i in file_paths:
                print('changing permissions')
                subprocess.call(['chmod', permission, i])
    # return subprocess.call('ls -l',shell=True)
        return file_paths

    

    
    


if folderpath == 'no':
    subprocess.call['chmod',perm,filepath]
    subprocess.call('ls -l',shell=True)
else:
    get_filepaths(folderpath,permission=perm)
    print(folderpath)
    subprocess.call('ls -l',shell=True)


    
    

    # return file_paths  # Self-explanatory.

# Run the above function and store its results in a variable.   
# full_file_paths = get_filepaths("/home/crash/Documents/kalkulus")
# print(full_file_paths)