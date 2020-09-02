import sys
def c_chipher(name,key): 
	result = "" 
	for i in range(len(name)): 
		c = name[i] 		
		if (c.isupper()): 
			result += chr((ord(c) + key-65) % 26 + 65) 	
		else: 
			result += chr((ord(c) + key - 97) % 26 + 97) 
	return result
    
if __name__== '__main__':
    if len(sys.argv) != 4 :
        print('Usage: python3 ' +sys.argv[0]+ ' <option> <text> <shift key>')
        print('Example: python3 ' +sys.argv[0]+ ' d ThIsIsCipherTeXt 23\n         python3 ' +sys.argv[0]+ 'e ThIsIsPlainTexT 4')
    else:
        if sys.argv[1]=='e':
            print ("Cipher: \n" + c_chipher(sys.argv[2],sys.argv[3]))
        if sys.argv[1] =='d':
            print ("Cipher: \n" + c_chipher(sys.argv[2],26 - sys.argv[3]))
        else:
            print('Usage: python3 ' +sys.argv[0]+ ' <option> <text> <shift key>')
            print('Example: \n python3 ' +sys.argv[0]+ ' d ThIsIsCipherTeXt 23\n python3 ' +sys.argv[0]+ 'e ThIsIsPlainTexT 4')
