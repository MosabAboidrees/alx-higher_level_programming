#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def find_search(element): # helper function to find and replace
        return element if element != search else replace # if element is not search, return element, else return replace
    return list(map(find_search, my_list)) # return list of elements after find_search is applied to each element