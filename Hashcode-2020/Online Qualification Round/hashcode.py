"""
Basic Algorithm Implementation:
1. Signing up of libraries:
	a. To determine which libraries to sign up, the libraries which have the ratio of the sum of the scores of their books to the number of days they take to sign up as the highest are signed up.
	b. In simple words, ratio = (total score of books) / (number of books)
	c. A new array is created with IDs of the libraries in the descending order of their ratios.
	d. Every time a library is signed up, it is added to the signed_up array which contains the IDs of the libraries which are signed up.
2. Signing up of books;
	a. Iterate through all libraries in the signed_up array
	b. For each library, iterate through its books, which will be sorted based on the their score.
	c. Some formulae used:
		days = number_of_days - starting_date of the library
		ex
"""

def signup():
	days_taken = 0
	# Creating a list with the library ids having highest score in sorted form
	library_score_temp = []
	for i in libraries:
		library_score_temp.append((i, libraries[i]['ratio']))
	library_score_temp.sort(key=lambda elem: elem[1], reverse=True)
	library_score = list(map(lambda x: x[0], library_score_temp))
	print("List of libraries and their ratios", library_score_temp)
	print("List of libraries with high ratios", library_score)
	for i in library_score:
		days = libraries[i]['signup']
		days_taken += days
		if days_taken > number_of_days:
			break
		signed_up.append(i)
		libraries[i]['starting_day'] = days_taken + 1
	print("Libraries signed up are: ", signed_up)

with open("e_so_many_books.txt") as f:
	number_of_books, number_of_libraries, number_of_days = list(map(int, f.readline().split(" ")))
	book_scores = {}
	signed_up = []
	books = []
	scores = list(map(int, f.readline().split(" ")))
	libraries = {}
	for i in range(number_of_books):
		book_scores[i] = scores[i]
	for i in range(number_of_libraries):
		details = list(map(int, f.readline().split(" ")))
		scores = list(map(int, f.readline().split(" ")))
		libraries[i] = {
		"library_books_number": details[0],
		"books": scores,
		"signup": details[1],
		"book_limit": details[2],
		"ratio": (sum(list(map(lambda x: book_scores[x], scores)))) / details[0]
		}

	signup()
	book_signing()