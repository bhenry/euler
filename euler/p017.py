def num2words(n):
    """Convert a number to words."""
    if n == 0:
        return 'zero'
    one2twenty = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    hundreds = ["one hundred", "two hundred", "three hundred", "four hundred", "five hundred", "six hundred", "seven hundred", "eight hundred", "nine hundred"]
    if n < 20:
        return one2twenty[n-1]
    elif n < 100:
        if n % 10 == 0:
            return tens[n//10-2]
        else:
            return tens[n//10-2] + "-" + one2twenty[n%10-1]
    elif n < 1000:
        if n % 100 == 0:
            return hundreds[n//100-1]
        else:
            return hundreds[n//100-1] + " and " + num2words(n%100)
    elif n == 1000:
        return "one thousand"

words = []

for i in range(1, 1001):
    words.append(num2words(i))

words = "".join(words).replace(" ", "").replace("-", "")
print(len(words))
