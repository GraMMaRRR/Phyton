import os
put = input()

if put == 'shut down':
    os.system("shutdown /s /t 0")
elif put == 'restart':
    os.system("shutdown/r /t 0")
