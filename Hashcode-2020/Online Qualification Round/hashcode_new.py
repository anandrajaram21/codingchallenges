import time
# Sorting Method

def sorting(arr):
	temp_arr = [(i, book_scores[i]) for i in arr]
	temp_arr.sort(key=lambda elem: elem[1], reverse=True)
	sorted_arr = [i[0] for i in temp_arr]
	return sorted_arr

# Signup Method

def signup():
	temp_arr = [(i,  libraries[i]['average']) for i in libraries]
	temp_arr.sort(key=lambda elem: elem[1], reverse=True)
	libraries_sorted = [i[0] for i in temp_arr]
	days_taken = 0
	for i in libraries_sorted:
		days = libraries[i]['signup']
		days_taken += days - 1
		if days_taken > number_of_days:
			break
		signed_up.append(i)
		days_taken += 1
		libraries[i]['starting day'] = days_taken

# Book Scanning Method

def bookscan():
	for i in signed_up:
		if libraries[i]['starting day'] >= number_of_days:
			libraries[i]['valid'] = False
			continue
		max_books = (number_of_days - libraries[i]['starting day']) * libraries[i]['limit']
		i_books = libraries[i]['books']
		counter = 0
		for j in i_books:
			if j in books:
				continue
			counter += 1
			if counter > max_books:
				break
			libraries[i]['books scanned'].append(j)
			books.add(j)
		libraries[i]['output number of books'] = len(libraries[i]['books scanned'])
		if libraries[i]['output number of books'] < 1:
			libraries[i]['valid'] = False
	for i in signed_up:
		if libraries[i]['valid']:
			signed_up_valid.append(i)

with open("a_example.txt") as f:
	number_of_books, number_of_libraries, number_of_days = list(map(int, f.readline().split(" ")))
	signed_up = []
	signed_up_valid = []
	books = set()
	library_books = []
	scores = list(map(int, f.readline().split(" ")))
	libraries = {}
	book_scores = {elem:scores[elem] for elem in range(number_of_books)}
	for i in range(number_of_libraries):
		details = list(map(int, f.readline().split(" ")))
		library_books = list(map(int, f.readline().split(" ")))
		sorted_library_books = sorting(library_books)
		libraries[i] = {
		"library books number": details[0],
		"books in set form": set(sorted_library_books),
		"books": sorted_library_books,
		"signup": details[1],
		"limit": details[2],
		"books scanned": [],
		"scores sum": sum(list(map(lambda x: book_scores[x], sorted_library_books))),
		"average": (sum(list(map(lambda x: book_scores[x], sorted_library_books))) / details[0]),
		"valid": True
		}

signup()
bookscan()

with open("a_output.txt", "w+") as output:
	output.write(str(len(signed_up_valid)) + '\n')
	for i in signed_up_valid:
		output.write(str(i) + ' ' + str(libraries[i]['output number of books']) + '\n')
		counter = 0
		for j in libraries[i]['books scanned']:
			if counter == len(libraries[i]['books scanned']) - 1:
				output.write(str(j) + '\n')
			else:
				output.write(str(j) + ' ')
			counter += 1

print("A - Example is Done!")			

with open("b_read_on.txt") as f:
	number_of_books, number_of_libraries, number_of_days = list(map(int, f.readline().split(" ")))
	signed_up = []
	signed_up_valid = []
	books = set()
	library_books = []
	uncommon_libraries = set()
	scores = list(map(int, f.readline().split(" ")))
	libraries = {}
	book_scores = {elem:scores[elem] for elem in range(number_of_books)}
	for i in range(number_of_libraries):
		details = list(map(int, f.readline().split(" ")))
		library_books = list(map(int, f.readline().split(" ")))
		sorted_library_books = sorting(library_books)
		libraries[i] = {
		"library books number": details[0],
		"books in set form": set(sorted_library_books),
		"books": sorted_library_books,
		"signup": details[1],
		"limit": details[2],
		"books scanned": [],
		"scores sum": sum(list(map(lambda x: book_scores[x], sorted_library_books))),
		"average": (sum(list(map(lambda x: book_scores[x], sorted_library_books))) / details[0]),
		"valid": True
		}

signup()
bookscan()

with open("b_output.txt", "w+") as output:
	output.write(str(len(signed_up_valid)) + '\n')
	for i in signed_up_valid:
		output.write(str(i) + ' ' + str(libraries[i]['output number of books']) + '\n')
		counter = 0
		for j in libraries[i]['books scanned']:
			if counter == len(libraries[i]['books scanned']) - 1:
				output.write(str(j) + '\n')
			else:
				output.write(str(j) + ' ')
			counter += 1

print("B - Read On is Done!")			

with open("c_incunabula.txt") as f:
	number_of_books, number_of_libraries, number_of_days = list(map(int, f.readline().split(" ")))
	signed_up = []
	signed_up_valid = []
	books = set()
	library_books = []
	uncommon_libraries = set()
	scores = list(map(int, f.readline().split(" ")))
	libraries = {}
	book_scores = {elem:scores[elem] for elem in range(number_of_books)}
	for i in range(number_of_libraries):
		details = list(map(int, f.readline().split(" ")))
		library_books = list(map(int, f.readline().split(" ")))
		sorted_library_books = sorting(library_books)
		libraries[i] = {
		"library books number": details[0],
		"books in set form": set(sorted_library_books),
		"books": sorted_library_books,
		"signup": details[1],
		"limit": details[2],
		"books scanned": [],
		"scores sum": sum(list(map(lambda x: book_scores[x], sorted_library_books))),
		"average": (sum(list(map(lambda x: book_scores[x], sorted_library_books))) / details[0]),
		"valid": True
		}

signup()
bookscan()

with open("c_output.txt", "w+") as output:
	output.write(str(len(signed_up_valid)) + '\n')
	for i in signed_up_valid:
		output.write(str(i) + ' ' + str(libraries[i]['output number of books']) + '\n')
		counter = 0
		for j in libraries[i]['books scanned']:
			if counter == len(libraries[i]['books scanned']) - 1:
				output.write(str(j) + '\n')
			else:
				output.write(str(j) + ' ')
			counter += 1	

print("C - Incunabula is Done!")			

with open("d_tough_choices.txt") as f:
	number_of_books, number_of_libraries, number_of_days = list(map(int, f.readline().split(" ")))
	signed_up = []
	signed_up_valid = []
	books = set()
	library_books = []
	uncommon_libraries = set()
	scores = list(map(int, f.readline().split(" ")))
	libraries = {}
	book_scores = {elem:scores[elem] for elem in range(number_of_books)}
	for i in range(number_of_libraries):
		details = list(map(int, f.readline().split(" ")))
		library_books = list(map(int, f.readline().split(" ")))
		sorted_library_books = sorting(library_books)
		libraries[i] = {
		"library books number": details[0],
		"books in set form": set(sorted_library_books),
		"books": sorted_library_books,
		"signup": details[1],
		"limit": details[2],
		"books scanned": [],
		"scores sum": sum(list(map(lambda x: book_scores[x], sorted_library_books))),
		"average": (sum(list(map(lambda x: book_scores[x], sorted_library_books))) / details[0]),
		"valid": True
		}

signup()
bookscan()

with open("d_output.txt", "w+") as output:
	output.write(str(len(signed_up_valid)) + '\n')
	for i in signed_up_valid:
		output.write(str(i) + ' ' + str(libraries[i]['output number of books']) + '\n')
		counter = 0
		for j in libraries[i]['books scanned']:
			if counter == len(libraries[i]['books scanned']) - 1:
				output.write(str(j) + '\n')
			else:
				output.write(str(j) + ' ')
			counter += 1	

print("D - Tough Choices is Done!")	

with open("e_so_many_books.txt") as f:
	number_of_books, number_of_libraries, number_of_days = list(map(int, f.readline().split(" ")))
	signed_up = []
	signed_up_valid = []
	books = set()
	library_books = []
	uncommon_libraries = set()
	scores = list(map(int, f.readline().split(" ")))
	libraries = {}
	book_scores = {elem:scores[elem] for elem in range(number_of_books)}
	for i in range(number_of_libraries):
		details = list(map(int, f.readline().split(" ")))
		library_books = list(map(int, f.readline().split(" ")))
		sorted_library_books = sorting(library_books)
		libraries[i] = {
		"library books number": details[0],
		"books in set form": set(sorted_library_books),
		"books": sorted_library_books,
		"signup": details[1],
		"limit": details[2],
		"books scanned": [],
		"scores sum": sum(list(map(lambda x: book_scores[x], sorted_library_books))),
		"average": (sum(list(map(lambda x: book_scores[x], sorted_library_books))) / details[0]),
		"valid": True
		}

signup()
bookscan()

with open("e_output.txt", "w+") as output:
	output.write(str(len(signed_up_valid)) + '\n')
	for i in signed_up_valid:
		output.write(str(i) + ' ' + str(libraries[i]['output number of books']) + '\n')
		counter = 0
		for j in libraries[i]['books scanned']:
			if counter == len(libraries[i]['books scanned']) - 1:
				output.write(str(j) + '\n')
			else:
				output.write(str(j) + ' ')
			counter += 1	

print("E - So Many Books is Done!")			

with open("f_libraries_of_the_world.txt") as f:
	number_of_books, number_of_libraries, number_of_days = list(map(int, f.readline().split(" ")))
	signed_up = []
	signed_up_valid = []
	books = set()
	library_books = []
	uncommon_libraries = set()
	scores = list(map(int, f.readline().split(" ")))
	libraries = {}
	book_scores = {elem:scores[elem] for elem in range(number_of_books)}
	for i in range(number_of_libraries):
		details = list(map(int, f.readline().split(" ")))
		library_books = list(map(int, f.readline().split(" ")))
		sorted_library_books = sorting(library_books)
		libraries[i] = {
		"library books number": details[0],
		"books in set form": set(sorted_library_books),
		"books": sorted_library_books,
		"signup": details[1],
		"limit": details[2],
		"books scanned": [],
		"scores sum": sum(list(map(lambda x: book_scores[x], sorted_library_books))),
		"average": (sum(list(map(lambda x: book_scores[x], sorted_library_books))) / details[0]),
		"valid": True
		}

signup()
bookscan()

with open("f_output.txt", "w+") as output:
	output.write(str(len(signed_up_valid)) + '\n')
	for i in signed_up_valid:
		output.write(str(i) + ' ' + str(libraries[i]['output number of books']) + '\n')
		counter = 0
		for j in libraries[i]['books scanned']:
			if counter == len(libraries[i]['books scanned']) - 1:
				output.write(str(j) + '\n')
			else:
				output.write(str(j) + ' ')
			counter += 1	

print("F - Libraries Of The World is Done!")				