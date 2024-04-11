def Numeroromano(roman_numeral):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    decimal_num = 0
    previous_value = 0

    for symbol in roman_numeral[::-1]:
        value = roman_values[symbol]
        if value < previous_value:
            decimal_num -= value
        else:
            decimal_num += value
            previous_value = value
    return decimal_num

print(Numeroromano(input("Ingrese el número romano: ").upper()))