f = open("about_me.txt")
#print (f.read())
#print (f.read(50)) #It printed 5 lines but on the 5th line only 6 characters were displayed so I am unsure if 50 characters total were printed
#print (f.readline()) #Only printed out the first line
#print (f.readline(10)) #Only printed out ten characters

#for i in range(1,24):
#    print(f.readline())

for i in range(1,24):
#    print(f.readlines()) # The execution was in [] and it included the string portions and breaks I added to my text separated by '' and ,
    #print(f.readlines(1)) # Every line is in [] and within '' divided by , and includes any breaks
    #print(f.readlines(1)) # Duplicates the rows executed 
    print(f.readlines(10)) #14.c