def number_to_words(n):
    # Dictionaries for single digits, tens, and thousands
    ones = ["", "one ","two ","three ","four ", "five ", "six ","seven ","eight ","nine "]

    tens = ["ten ","eleven ","twelve ","thirteen ", "fourteen ", "fifteen ","sixteen ","seventeen ","eighteen ","nineteen "]

    twenties = ["","","twenty ","thirty ","forty ", "fifty ","sixty ","seventy ","eighty ","ninety "]

    thousands = ["","thousand ","million ", "billion ", "trillion ",
        "quadrillion ", "quintillion ", "sextillion ", "septillion ","octillion ",
        "nonillion ", "decillion ", "undecillion ", "duodecillion ", "tredecillion ",
        "quattuordecillion ", "quindecillion", "sexdecillion ", "septendecillion ", 
	    "octodecillion ", "novemdecillion ", "vigintillion "]

    def helper(n):
        if n == 0:
            return ""
        elif n < 10:
            return ones[n]
        elif n < 20:
            return tens[n % 10]
        elif n < 100:
            return twenties[n // 10] + ones[n % 10]
        elif n < 1000:
            return ones[n // 100] + "hundred " + helper(n % 100)
        else:
            return helper(n // 1000) + " " + thousands[0] + " " + helper(n % 1000)

    return helper(n).strip()

print(number_to_words(1000))