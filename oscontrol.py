import os
import pwd
import sys
import shutil
import subprocess as sub

print(os.getlogin())
print(os.getuid())
print(pwd.getpwuid(os.getuid()))

for id in pwd.getpwall():
    print (id[0])


print(sys.platform)
print(os.uname() )
print(os.getpid())
print(os.getcwd()) # directorio actual current work directory
print(len(os.environ))
print(os.environ['HOME'])


print(os.umask(0b111111111))
print(bin(18))
print(os.umask(18))
print(os.name)
print(os.uname())



cols, lines =  shutil.get_terminal_size()
print(cols)
print(lines)


print(os.environ)


sub.call(['ls'])
stdout=open('ls.txt','w')

for line in open('ls.txt'):
    print(line)


sub.Popen(['ls','*.*'], shell=True)
