class Solution:
    units = ["","One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    
    def is_zero(self, number:int, divisor:int) -> int:
        return f" {self.numberToWords(number % divisor)}" if number % divisor != 0 else ""

    def numberToWords(self, number: int) -> str:
        
        if number == 0:
            return "Zero"
        elif 1 <= number < 10:
            return self.units[number]
        elif 10 <= number < 20:
            return self.teens[number - 10]
        elif 20 <= number < 100:
            return self.tens[number // 10] + self.is_zero(number, 10)
        elif number < 1_000:
            return self.numberToWords(number // 100) + " Hundred" + self.is_zero(number, 100)
        elif number < 1_000_000:
            return self.numberToWords(number // 1_000) + " Thousand" + self.is_zero(number, 1_000)
        elif number < 1_000_000_000:
            return self.numberToWords(number // 1_000_000) + " Million" + self.is_zero(number, 1_000_000) 
        elif number < 1_000_000_000_000:
            return self.numberToWords(number // 1_000_000_000) + " Billion" + self.is_zero(number, 1_000_000_000) 
