#!/usr/bin/python

# Caesar Cipher
# Following cipher is based on where A = 0, B = 1, ..., Z = 25
# Highly insecure cipher, never use it
# The class works by itself as well

import sys
import argparse

class Caesar:
	def __init__(self, key = 3):
		self.key = key

		if self.key < 0 or self.key > 25:
			sys.exit("[-] Error: key must be between 0 and 25")

		self.alphabet = {
			'A': 0,
			'B': 1,
			'C': 2,
			'D': 3,
			'E': 4,
			'F': 5,
			'G': 6,
			'H': 7,
			'I': 8,
			'J': 9,
			'K': 10,
			'L': 11,
			'M': 12,
			'N': 13,
			'O': 14,
			'P': 15,
			'Q': 16,
			'R': 17,
			'S': 18,
			'T': 19,
			'U': 20,
			'V': 21,
			'W': 22,
			'X': 23,
			'Y': 24,
			'Z': 25
		}

	def encode(self, string):
		try:
			encoded_string = ""

			for letter in string.upper():
				if not letter.isalpha():
					raise Exception("cipher only meant to encode letters")
				
				special_number = (self.alphabet.get(letter) + self.key)
				
				if special_number < 0:
					special_number + 26
				elif special_number > 25:
					special_number - 26
				
				for key, value in self.alphabet.iteritems():
					if value == (special_number % 26):
						encoded_string += key
			
			return encoded_string
		
		except Exception as e:
			sys.exit("[-] Error: " + str(e))

	def decode(self, string):
		try:
			decoded_string = ""
			
			for letter in string.upper():
				if not letter.isalpha():
					raise Exception("cipher only meant to encode letters")
				special_number = (self.alphabet.get(letter) - self.key)
				
				if special_number < 0:
					special_number + 26
				elif special_number > 25:
					special_number - 26
				
				for key, value in self.alphabet.iteritems():
					if value == (special_number % 26):
						decoded_string += key
			
			return decoded_string
		
		except Exception as e:
			sys.exit("[-] Error: " + str(e))

def main():
	usage = '%(prog)s -s <string to encode/decode>'
	description = 'Caesar cipher in Python'
	parser = argparse.ArgumentParser(usage=usage, description=description)
	parser.add_argument('-s', '--string', action="store", dest="string", help="string to encode/decode", required=True)
	parser.add_argument('-k', '--key', action="store", dest="key", help="integer 0-25")
	results = parser.parse_args()

	string = results.string

	if results.key:
		key = int(results.key)
	else:
		key = 3

	caesar = Caesar(key)

	encoded = caesar.encode(string)
	decoded = caesar.decode(encoded)
	
	print "[*] Encoded: %s" % encoded
	print "[*] Decoded: %s" % decoded

if __name__ == '__main__':
	main()
