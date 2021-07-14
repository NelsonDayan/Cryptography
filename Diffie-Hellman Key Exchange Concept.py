if __name__ == '__main__':
	P = 23
	G = 9
	a = 4
	x = int(pow(G,a,P))
	b = 3
	y = int(pow(G,b,P))
	ka = int(pow(y,a,P))
	kb = int(pow(x,b,P))
	print('Secret key for A is : %d'%(ka))
	print('Secret Key for B is : %d'%(kb))
