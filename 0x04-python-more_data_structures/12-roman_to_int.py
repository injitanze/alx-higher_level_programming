#!/usr/bin/python3
def to_subtract(list_num):
    to_sub = 0
    max_list = max(list_num)

    for num in list_num:
        if max_list > num:
            to_sub += num

    return (max_list - to_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_num.keys())

    numba = 0
    last_rom = 0
    list_num = [0]

    for roman in roman_string:
        for r_num in list_keys:
            if r_num == roman:
                if rom_num.get(roman) <= last_rom:
                    numba += to_subtract(list_num)
                    list_num = [rom_num.get(roman)]
                else:
                    list_num.append(rom_num.get(roman))

                last_rom = rom_num.get(roman)

    numba += to_subtract(list_num)

    return (numba)
