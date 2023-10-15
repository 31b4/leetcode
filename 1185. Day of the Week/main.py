class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
	    return date(year, month, day).strftime("%A")
