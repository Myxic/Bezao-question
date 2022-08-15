def int_to_text(num):
    d = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
         6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
         11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
         15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
         19: 'nineteen', 20: 'twenty',
         30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
         70: 'seventy', 80: 'eighty', 90: 'ninety'}

    # k is thousand m is million and so on

    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000

    if num < 20:
        return d[num]

    if num < 100:
        if num % 10 == 0:
            return d[num]
        else:
            return d[num // 10 * 10] + '-' + d[num % 10]

    if num < k:
        if num % 100 == 0:
            return d[num // 100] + ' hundred'
        else:
            return d[num // 100] + ' hundred and ' + int_to_text(num % 100)

    if num < m:
        if num % k == 0:
            return int_to_text(num // k) + ' thousand'
        else:
            return int_to_text(num // k) + ' thousand, ' + int_to_text(num % k)

    if num < b:
        if (num % m) == 0:
            return int_to_text(num // m) + ' million'
        else:
            return int_to_text(num // m) + ' million, ' + int_to_text(num % m)

    if num < t:
        if (num % b) == 0:
            return int_to_text(num // b) + ' billion'
        else:
            return int_to_text(num // b) + ' billion, ' + int_to_text(num % b)

    if num % t == 0:
        return int_to_text(num // t) + ' trillion'
    else:
        return int_to_text(num // t) + ' trillion, ' + int_to_text(num % t)


def text2int(textnum, numwords=None):
    if numwords is None:
        numwords = {}
    if not numwords:
        units = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen",
        ]

        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        scales = ["hundred", "thousand", "million", "billion", "trillion"]

        numwords["and"] = (1, 0)
        for idx, word in enumerate(units):
            numwords[word] = (1, idx)
        for idx, word in enumerate(tens):
            numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales):
            numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
            raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current


input1 = input("What conversion do you want to perform (num_2_text or text_2_num):  ")
input2 = input("Enter input >  ")

if input1 == "text_2_num":
    h = ""
    for words in input2:
        if words == '-':
            words = " "
            h += words
        elif words == ",":
            pass
        else:
            h += words
    num = text2int(h)

    num = str(num)
    m = 3
    emt_str = ""
    list1 = []
    for n in num:
        list1.append(n)

    len1 = len(list1)
    while m < len1:
        list1.insert(len1 - m, ",")
        m += 3
    for number in list1:
        emt_str += number
    print(emt_str)
elif input1 == "num_2_text":
    if input2 == int:
        print(int_to_text(input2))
    #     in the else we will remove "," or "-" if present (eg:7,100,031,337,000) or (eg:7-000-000)
    else:
        input2 = str(input2)
        number1 = ""
        for elements in input2:
            if elements.isnumeric():
                number1 += elements
        number2 = int(number1)
        print(int_to_text(number2))






