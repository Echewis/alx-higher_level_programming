#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    numerate = sum(score * weight for score, weight in my_list)
    denominate = sum(weight for score, weight in my_list)
    return (numerate / denominate)
