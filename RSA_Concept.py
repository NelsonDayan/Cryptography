from decimal import Decimal 

def main():
	global p,q,n
	p = int(input('Enter a prime number (p) = '))
	chk_prime(p)
	q = int(input('Enter another prime number (q) = ')) 
	chk_prime(q)
	text = input('Enter the message = ')
	n=p*q
	print('Public Key:\n   n =',p*q,'\n   e =',snd_pub())
	print('Private Key:\n   d =',de(snd_pub()))
	ct=en_text(p,q,text)
	print('chipher text:\n   '+str(ct))
	print('decrypted text:\n   '+de_text(p,q,ct))
	return 0

#Checks if x is a prime number
def chk_prime(x):
	for i in (2,x//2):
		if x%i==0:
			print(x,"is not a prime")
			main()
	return 0

#Greatest common divisor (Euclid's Algorithm) 
def gcd(a,b): 
	if b==0: 
		return a 
	else: 
		return gcd(b,a%b) 

#Function to convert string to numbers (when e==1) and converts numbers to string (when e==0) 
def txt_ascii(x,e):
	x=str(x).upper()
	txt_num={'A':'01','B':'02','C':'03','D':'04','E':'05','F':'06','G':'07','H':'08','I':'09','J':'10','K':'11','L':'12','M':'13','N':'14','O':'15','P':'16','Q':'17','R':'18','S':'19','T':'20','U':'21','V':'22','W':'23','X':'24','Y':'25','Z':'26'}
	if e==1:
		return txt_num[x]
	elif e==0:
		if int(x) in range (0,9): 
			return list(txt_num.keys())[list(txt_num.values()).index('0'+str(x))]
		else:
			return list(txt_num.keys())[list(txt_num.values()).index(x)]

#Finds e (part of Public Key)
def snd_pub():
	t = (p-1)*(q-1)
	for e in range(2,t): 
		if gcd(e,t)== 1: 
			break
	return e

#Finds d (Private Key)
def de(e):
	t = (p-1)*(q-1)
	for i in range(1,10): 
		x = 1 + i*t 
		if x % e == 0: 
			d = int(x/e) 
			break
	return d

#Encryption
def encrypt(n,no,e):
	r = Decimal(0) 
	r =pow(no,e) 
	ct = r % n
	return ct

#Decryption
def decrypt(ct,d,n):
	w = Decimal(0) 
	w = pow(ct,d) 
	dt = w % n 
	return dt

def rsa_en(no,n):
	e=snd_pub()
	return encrypt(n,no,e)

def rsa_de(n,ct): 
	e=snd_pub()
	d=de(e)
	return decrypt(ct,d,n)		

def en_text(p,q,text):
	en_txt=[]
	for x in text:
		y=rsa_en(int(txt_ascii(x,1)),p*q)
		en_txt.append(y)
	return en_txt

def de_text(p,q,ct):
	de_txt=''
	for x in ct:
		y=rsa_de(n,int(x))
		z=txt_ascii(y,0)
		de_txt+=str(z)
	return de_txt
	
main()
