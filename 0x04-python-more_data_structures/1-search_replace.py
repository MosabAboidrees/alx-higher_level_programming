#!/usr/bin/python3
def search_replace(my_list, search, replace):
	def find_search(element): # helper function to find and replace
		# if element is not search, return element, else return replace
		return element if element != search else replace
	# return list of elements after find_search is applied to each element
	return list(map(find_search, my_list))