#!/usr/bin/python3
def weight_average(my_list=[]):
    # Return 0 immediately if the input list
    # is empty to handle edge cases.
    if not my_list:
        return 0
    # Initialize variables for the sum of
    # weighted scores and the sum of weights.
    sum_weighted_scores = 0
    sum_weights = 0
    # Iterate over each tuple in the list.
    for score, weight in my_list:
        # Multiply the score by its weight and
        # add it to the sum of weighted scores.
        sum_weighted_scores += score * weight
        # Add the weight to the sum of weights.
        sum_weights += weight
    # Calculate the weighted average by dividing
    # the sum of weighted scores
    # by the sum of weights. Return this value.
    return sum_weighted_scores / sum_weights
