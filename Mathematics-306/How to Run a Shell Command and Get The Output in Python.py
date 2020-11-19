import subprocess
return_text = subprocess.check_output("dir",shell=True,universal_newlines=True)
print("dir command to list file and directory.")
print(return_text)