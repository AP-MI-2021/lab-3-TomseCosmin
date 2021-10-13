import math
def verificare_perfect_square(x):
    y = math.sqrt(x)
    int(y)
    y=y//1
    
    if y*y==x:
        return True
    return False
def test_vertificare_perfect_square():
    '''
    test verificare_perfect_square
    '''
    assert verificare_perfect_square(16) == True
    assert verificare_perfect_square(17) == False
def get_longest_all_perfect_squares(lst: list[int]) -> list[int]:

    '''
    numar maxim patrate perfecte consecutive
    '''
    mx = 0
    nr = 0
    for x in lst:
        if verificare_perfect_square(x):
            nr = nr + 1
            if nr > mx:
                mx = nr
        else:
            nr = 0
    return mx

def afiseaza_get_longest_all_perfect_square(listat):
    print(get_longest_all_perfect_squares(listat))

def is_prime(n):
    '''
    returneaza true daca nr e prim si false in caz contrar
    '''
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def test_is_prime():
    '''
    Test pentru is_prime
    '''
    assert is_prime(7) == True
    assert is_prime(10) == False
    assert is_prime(1) == False
    assert is_prime(29) == True


test_is_prime()


def get_longest_all_primes(lst):
    '''
    verifica cate numere sunt prime.
    '''
    mx = 0
    nr = 0
    for x in lst:
        if is_prime(x):
            nr = nr + 1
            if nr > mx:
                mx = nr
        else:
            nr = 0
    return mx


def test_get_longest_all_primes():
    '''
    Test pentru get_longest_all_primes
    '''
    lista1 = [12, 7, 11, 4, 7, 7, 7, 8]
    lista2 = [12, 7, 11, 4, 7, 7, 7, 11, 8]
    lista3 = [12, 7, 11, 4, 7, 7, 6, 8]
    assert get_longest_all_primes(lista1) == 3
    assert get_longest_all_primes(lista2) == 4
    assert get_longest_all_primes(lista3) == 2


test_get_longest_all_primes()


def afiseaza_get_longest_all_primes(listay):
    '''
    se introduce o lista de nr intregi
    :return: lungimea celui mai lung subsir care contine doar nr prime
    '''
    print(get_longest_all_primes(listay))


def all_prime_digits(numar2):
    '''
    verifica daca toate cifrele unui nr sunt prime
    '''
    while (0 - numar2) < 0:
        if is_prime(numar2 % 10):
            numar2 = numar2 // 10
        else:
            return False
    return True


def test_all_prime_digits():
    '''verifica functia all_prime_digits
    '''
    assert all_prime_digits(32) == True
    assert all_prime_digits(124) == False


test_all_prime_digits()


def get_longest_prime_digits(lst: list[int]) -> list[int]:
    mx = 0
    nr = 0
    for x in lst:
        if all_prime_digits(x):
            nr = nr + 1
            if nr > mx:
                mx = nr
        else:
            nr = 0
    return mx


def test_get_longest_primes_digits():
    list1 = [222, 2323, 44, 22, 2, 22, 2222]
    assert get_longest_prime_digits(list1) == 4


test_get_longest_all_primes()


def afiseaza_get_longes_prime_digits(listaz):
    '''
    :return: lungimea celui mai lung subsir cu toate nr cu cifre prime
    '''
    a = get_longest_prime_digits(listaz)
    print(a)


def main():

    listax = []
    print("1. introducere lista")
    print("2. afiseaza lungimea celei mai lungi subsecvente cu proprietatea ca toate nr sunt prime")
    print("3. afiseaza lungimea celeimai mai lungi subsecvente cu proprietatea ca toate nr au cifre prime")
    print("4. afiseaza lungimea celeimai mai lungi subsecvente cu proprietatea ca toate nr sunt patrate perfecte")
    print("5. iesire")
    while True:
        optiune = int(input("dati optiune:"))
        if optiune == 1:

            n = int(input("introduceti nr de elemente pe care doriti sa il introduceti:"))
            for i in range(0, n):
                element = int(input("introduceti element al listei:"))
                listax.append(element)

        elif optiune == 2:
            afiseaza_get_longest_all_primes(listax)
        elif optiune == 3:
            afiseaza_get_longes_prime_digits(listax)
        elif optiune == 4:
            afiseaza_get_longest_all_perfect_square(listax)
        elif optiune == 5:
            print("ati iesit din meniu")
            return
        else:
            print("optiunea aleasa nu exista")
            return


main()

