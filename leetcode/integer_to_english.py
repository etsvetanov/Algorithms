# non-negative integers, i.e. [0, 2^31 - 1)
# largest number is 4 billion and something
# orders - [teens, tens, hundreds, thousands, million, billion]
# find the orders and their weight(size)

# Test Cases
# 0 - Zero
# 5 - Five (single digits)
# 10 - first number of next order (tens)
# 15 -
# num = 3 123 456 713
# num // 10 ** 9 == 3
# num %  10 ** 9 == 123 456 713


class Solution:
    def numberToWords(self, num: int) -> str:
        repr_by_number = {
            0: 'zero',
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
            10: 'ten',
            11: 'eleven',
            12: 'twelve',
            13: 'thirteen',
            14: 'fourteen',
            15: 'fifteen',
            16: 'sixteen',
            17: 'seventeen',
            18: 'eighteen',
            19: 'nineteen',
            20: 'twenty',
            30: 'thirty',
            40: 'fourty',
            50: 'fifty',
            60: 'sixty',
            70: 'seventy',
            80: 'eighty',
            90: 'ninety',
            10 ** 2: 'hundred',
            10 ** 3: 'thousand',
            10 ** 6: 'million',
            10 ** 9: 'billion'
        }

        orders_of_magnitude = (10 ** 9, 10 ** 6, 10 ** 3, 10 ** 2, 10 ** 1, 10 ** 0)
        reminder = num

        results = []
        for o in orders_of_magnitude:
            quotient = reminder // o
            reminder %= o

            if quotient > 0:
                results.append((quotient, o))

            if reminder == 0:
                break

        number_in_english = []

        for weight, order in results:
            if weight == 0:
                continue

            if order == 10 ** 1 and weight == 1:
                last_digit, _ = results[-1]
                teen = 10 + last_digit

                number_in_english.append(repr_by_number[teen])
                break

            number_in_english.append(repr_by_number[weight].capitalize() + ' ' + repr_by_number)


        return ' '.join(number_in_english)




