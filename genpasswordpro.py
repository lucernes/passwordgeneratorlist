import itertools
from string import digits, punctuation ,ascii_letters

def genpass():
    try:
        passwordlen = input('enter leng password: \n')
        passwordlen = [int(item) for item in passwordlen.split('-')]
        
  
    except:
        print('eror')
    print('enter 1 if password have numbers: \nenter 2 if password have letters: \nenter 3 if password have numbers and letters: \nenter 4 if password have numbers, letters and punctuation ')
    try:
        choice = int(input(':'))
        if choice == 1:
            possible_symble = digits
        elif choice == 2:
            possible_symble = ascii_letters
        elif choice == 3:
            possible_symble = digits + ascii_letters
        elif choice == 4:
            possible_symble = digits + ascii_letters + punctuation
        else:
            print('eror')
        
        for passwordleng in range(passwordlen[0], passwordlen[1]):
            for password in itertools.product(possible_symble, repeat=passwordleng):
                password = "".join(password)
                file = open('brut.txt', 'a')
                file.write('\n' + password)
                file.close()

 



    except:
        print('eror')


def main():
    genpass()

if __name__ == '__main__':
    main()