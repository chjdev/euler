# Number letter counts
# Problem 17
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
# letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one
# hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British
# usage.


def spell_out(num, cont='', spell_zero=False):
    if num == 0:
        if spell_zero:
            return 'zero'
        else:
            return ''

    if num >= 1000:
        return "one thousand" + spell_out(num % 1000, ' and ')
    if num >= 100:
        return (spell_out(num / 100) + ' hundred' + spell_out(num % 100, ' and ')).rstrip()

    tens = ('twenty',
            'thirty',
            'forty',
            'fifty',
            'sixty',
            'seventy',
            'eighty',
            'ninety')
    if num >= 20:
        return cont + tens[int(num / 10) - 2] + spell_out(num % 10, ' ')

    singles = ('one',
               'two',
               'three',
               'four',
               'five',
               'six',
               'seven',
               'eight',
               'nine',
               'ten',
               'eleven',
               'twelve',
               'thirteen',
               'fourteen',
               'fifteen',
               'sixteen',
               'seventeen',
               'eighteen',
               'nineteen')
    return cont + singles[int(num) - 1]


spelled_numbers = map(spell_out, range(1, 1001))
no_spaces = map(lambda number: number.replace(' ', ''), spelled_numbers)
num_characters = sum(map(len, no_spaces))
print(num_characters)
