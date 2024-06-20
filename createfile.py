'''
open()
Create()
Read()
ReadLine()
Write()
WeiteLine()
Fseek()
FTell()
Close()
'''
fp=open("Cse.text","w")
if fp:
    print("file is created successfully")
fp.write("Hi students welcome to cmrec\n today is Friday")
fp.writelines("Hi students welcome to cmrec\n today is Friday\n hello world")

fp.close()
