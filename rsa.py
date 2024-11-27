from colorama import Fore, Style, init
import pyfiglet
import math
def prime(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0 :
            return False
    return True

#phi p = p-1 if p is prime, phi(p^k)=p^k-p^(k-1) or just count the co-primes O(n)
def euler(n):
    cnt=0
    for i in range(1,n):
        if math.gcd(i,n)==1:
            cnt+=1
    return cnt

#C=m^e mod N (Public Key)
def encryption(m, e, n):
    return pow(m,e,n)
#pow(base,exponential,mod)

#ax cong 1 mod n => (a.b) x cong b mod n => x cong ab mod n  
def inverse(e,n):
    if math.gcd(e,n)!=1:
        raise ValueError("INVALID :>>")
    return pow(e,-1,n)

def decryption(c,d,n):
    return pow(c,d,n)
    
    
banner = pyfiglet.figlet_format("GodaPWN")
print(Fore.BLUE + banner)
print(Fore.YELLOW + "=" * 60)
print(Fore.CYAN + "GodaPWN's RSA")
print(Fore.YELLOW + "=" * 60)
p = int(input(Fore.CYAN + Style.BRIGHT + "Enter a prime number : "))
if not(prime(p)):
    raise ValueError("Put a prime here")
q = int(input(Fore.MAGENTA + Style.BRIGHT + "Enter another prime number: "))
if not(prime(q)):
    raise ValueError("Put a prime here")
e = int(input(Fore.GREEN + Style.BRIGHT + "Enter the public key exponent : "))
n = p * q
phiin = euler(n)
d = inverse(e, phiin)
print(Fore.YELLOW + "Generating your RSA keys...")
print(Fore.GREEN + f"Public Key: (e={e}, n={n})")
print(Fore.RED + f"Private Key: (d={d}, n={n})")
banner = pyfiglet.figlet_format("SHHH!! Secret")
print(Fore.RED + banner)
print(Fore.YELLOW + "=" * 30)
print(Fore.CYAN + "Don't tell anybody ;)")
print(Fore.YELLOW + "=" * 60)
m = int(input(Fore.CYAN + "Enter a message to encrypt: "))
c = encryption(m, e, n)
print(Fore.MAGENTA + f"Chipher : {c}")
decrypted = decryption(c, d, n)
print(Fore.GREEN + f"Decryption: {decrypted}")
