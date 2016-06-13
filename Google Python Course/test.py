# Function for testing out some stuff

# I'm going to make the Cat() function, which prints out the contents of files
import sys

def Cat(filename): 
   f = open(filename, 'rU')
   for line in f:
       print line,
       
       
def main():
    Cat(sys.argv[1])
    

# Specify to run the main() function if the module is called
if __name__ == '__main__':
    main()