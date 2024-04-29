# -*- coding: utf-8 -*-

def filter_short_strings(input_array):
    output_array = []
    for string in input_array:
        if len(string) <= 3:
            output_array.append(string)
    return output_array
