import sys, getopt

args=sys.argv
argnum=len(args)
#print(type(args))



def main(argv):
    #print(f"{argnum} arguments")
    
    age=''
    name=''

    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    
    for opt, arg in opts:
      if opt == '-h':
         print ('arg.py -a <age> -n <name>')
         sys.exit()
      elif opt in ("-a", "--age"):
         age = arg
      elif opt in ("-n", "--name"):
         name = arg

    print("Bravo, tu sais faire du velo")
    print(opts)
    print(args)


if __name__ == "__main__":
    
    #if argnum==1:
    #    print("usage: arg.py prenom [age]")
    #    exit(0)
    
    main(sys.argv[1:])

