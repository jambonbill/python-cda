import sys
from verif import verif

USAGE = f"usage: python3 test.py age(int)"

if len(sys.argv) != 2:
    print(USAGE)
    exit(127)

def main():
    '''
    documenation de la fonction
    '''    
    try:
        age=int(sys.argv[1])        
    
    except TypeError:
        sys.exit(USAGE)
    
    else:
        verif(age)





if __name__ == "__main__":    
    main()