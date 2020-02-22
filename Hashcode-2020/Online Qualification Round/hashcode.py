"""
Basic Algorithm Implementation:
1. Signing up of libraries:
	a. To determine which libraries to sign up, the libraries which have the ratio of the sum of the scores of their books to the number of days they take to sign up as the highest are signed up.
	b. In simple words, ratio = (total score of books) / (number of books)
	c. A new array is created with IDs of the libraries in the descending order of their ratios.
	d. Every time a library is signed up, it is added to the signed_up array which contains the IDs of the libraries which are signed up.
2. Signing up of books;
	a. Iterate through all libraries in the signed_up array
	b. For each library, iterate through its books, which will be sorted based on the their score. (Will sort based on score later)
	c. Some formulae used:
		days = number_of_days - starting_date of the library
		limit = maximum number of books that can be signed per day for each library
		example: days = 2, len(books) = 5, limit = 3
		max_books = days * limit
		if len(books) > max_books:
			books_to_scan = max_books
		else:
			books_to_scan = len(books)
	d. For each book, add it to an array, and increment a counter variable
	e. If the counter becomes greater than books_to_scan, break out of the inner loop.
"""

import json

# Signup Method

def signup():
	days_taken = 0
	library_score_temp = [] # A temporary list containing tuples with the library id and their corresponding ratios
	for i in libraries:
		library_score_temp.append((i, libraries[i]['ratio'])) # Initializing the list with its values
	library_score_temp.sort(key=lambda elem: elem[1], reverse=True) # Sorting the list in descending order of the library ID's ratio
	library_score = list(map(lambda x: x[0], library_score_temp)) # Making a list of all the library IDs only in descending order of their ratios
	for i in library_score:
		days = libraries[i]['signup'] # Number of days taken to signup
		days_taken += days - 1 # Incrementing a days_taken variable with days for each library
		if days_taken > number_of_days:
			break
		signed_up.append(i) # Adding the particular library signed_up array if they are within the deadline for signup
		days_taken += 1
		libraries[i]['starting_day'] = days_taken + 1 # The date on which the library can start scanning books

# Sorting Method

def sorting(arr):
	sorted_arr = []
	temp_arr = []
	for i in range(len(arr)):
		temp_arr.append((arr[i], book_scores[arr[i]]))
	temp_arr.sort(key=lambda elem: elem[1], reverse=True)
	for i in temp_arr:
		sorted_arr.append(i[0])
	return sorted_arr

# Book Scanning Method

def bookscan():
	books_to_scan = 0
	for i in signed_up:
		i_books = libraries[i]['books']
		if libraries[i]['starting_day'] >= number_of_days:
			libraries[i]['checking'] = False
			continue
		days = number_of_days - libraries[i]['starting_day']
		limit = libraries[i]['book_limit']
		max_books = days * limit
		if len(i_books) > max_books:
			books_to_scan = max_books
		else:
			books_to_scan = len(i_books)
		libraries[i]['output_number_of_books'] = books_to_scan
		libraries[i]['scanned_books'] = []
		counter = 0
		for j in i_books:
			counter += 1
			if counter > books_to_scan:
				break
			libraries[i]['scanned_books'].append(j)
	for i in range(len(signed_up)):
		if libraries[signed_up[i]]['checking'] == True:
			signed_up1.append(signed_up[i])

# Main Method!!!

with open("f_libraries_of_the_world.txt") as f:
	number_of_books, number_of_libraries, number_of_days = list(map(int, f.readline().split(" ")))
	book_scores = {} # A dictionary containing each book id and its corresponding score
	signed_up = [] # A list containing the IDs of the libraries which are signed up
	signed_up1 = [] # A list containing the IDs of the libraries which are valid and signed up
	books = [] # A list containg the book IDs that shoule be considered while taking the sum
	library_books = [] # A list that will contain the book IDs of the books in each library
	scores = list(map(int, f.readline().split(" "))) # A list containing all the scores of the books taken from the input file
	libraries = {} # A dictionary containing all details of each library with the library ID as its key
	for i in range(number_of_books):
		book_scores[i] = scores[i] # Initializing the book_scores dictionary with the values
	for i in range(number_of_libraries):
		details = list(map(int, f.readline().split(" "))) # The details of each library read from the input file
		library_books = list(map(int, f.readline().split(" "))) # The IDs of the books in each library
		sorted_library_books = sorting(library_books)
		libraries[i] = {
		"library_books_number": details[0], # Number of books in the library
		"books": sorted_library_books, # The IDs of the books in the library
		"signup": details[1], # Number of days taken for signup
		"book_limit": details[2], # Limit to the number of books that can be signed each day
		"checking": True,
		"ratio": (sum(list(map(lambda x: book_scores[x], library_books)))) / details[1] # The ratio of sum of scores of the books of the library to the number of days taken to sign up
		}

	signup()
	bookscan()

with open("f_output.txt", "w+") as output:
	output.write(str(len(signed_up1)) + "\n")
	for i in range(len(signed_up1)):
		if libraries[signed_up1[i]]['checking']:
			if i != len(signed_up1) - 1:
				output.write(str(signed_up1[i]) + " " + str(libraries[signed_up1[i]]['output_number_of_books']) + '\n')
				for j in range(len(libraries[signed_up1[i]]['scanned_books'])):
					if j == len(libraries[signed_up1[i]]['scanned_books']) - 1:
						output.write(str(libraries[signed_up1[i]]['scanned_books'][j]) + '\n')
					else:
						output.write(str(libraries[signed_up1[i]]['scanned_books'][j]) + ' ')
			else:
				output.write(str(signed_up1[i]) + " " + str(libraries[signed_up1[i]]['output_number_of_books']) + '\n')
				for j in range(len(libraries[signed_up1[i]]['scanned_books'])):
					if j == len(libraries[signed_up1[i]]['scanned_books']) - 1:
						output.write(str(libraries[signed_up1[i]]['scanned_books'][j]))
					else:
						output.write(str(libraries[signed_up1[i]]['scanned_books'][j]) + ' ')
					
