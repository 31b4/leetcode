class Solution:
	def reverseBits(self, n: int) -> int:
		binary_number = bin(n)[2:]
		binary_number = '0'*(32-len(binary_number))+binary_number
		reverse_binary_number = binary_number[::-1]
		return int(reverse_binary_number, 2)
