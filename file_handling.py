import datetime
import os
# Create a file
fil=open("demofile.txt","w+")
# Check if a file exists or not
print(os.path.isfile('D:\\eShop\\amado\\amado\\cartx.html'))
# get attributes of a file - size, date created, date last modified
print(os.stat("D:\\eShop\\amado\\amado\\shop.html"))
dm=os.stat("D:\\eShop\\amado\\amado\\shop.html").st_ctime
print(datetime.datetime.fromtimestamp(dm))
# read from a file
# write into a file
fil.write("Contents of demo file\n")
fil.write(("More contents\n"))
mylist=["line one\n", "line two\n", "line three\n"]
fil.writelines(mylist)