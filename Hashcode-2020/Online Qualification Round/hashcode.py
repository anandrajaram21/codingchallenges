""" Algorithm Implementation:
1. Sign up those libraries which have the highest score of books
2. Make a for loop that runs in signed up
3. Start signing the books of the libraries from the start date till number_of_days
4. Add the books to an array, and each time before adding, check if the book is already there in the array
5. Calculate the sum of the scores of each book and that is the max.
"""
import time

# def book_signing():
# 	end_date = number_of_days - 1
# 	max_sum = 0
# 	for i in signed_up:
# 		i_books = libraries[i]['books']
# 		print(i_books)
# 		start_date = libraries[i]['starting_day']
# 		start_date_copy = libraries[i]['starting_day']
# 		limit = libraries[i]['book_limit']
# 		# while start_date <= end_date:
# 		# 	counter = 0
# 		# 	for i in i_books:
# 		# 		if i not in books:
# 		# 			books.append(i)
# 		# 			counter += 1
# 		# 		if counter > limit:
# 		# 			counter = 0
# 		# 			break
# 		# 	start_date += 1
# 		counter = 0
# 		for i in i_books:
# 			if i not in books:
# 				books.append(i)
# 				counter += 1
# 			if counter > limit:
# 				counter = 0
# 	for i in books:
# 		max_sum += book_scores[i]
# 	print(max_sum)


def signup():
	days_taken = 0
	# Creating a list with the library ids having highest score in sorted form
	library_score_temp = []
	for i in libraries:
		library_score_temp.append((i, libraries[i]['score']))
	library_score_temp.sort(key=lambda elem: elem[1], reverse=True)
	library_score = list(map(lambda x: x[0], library_score_temp))
	print("List of libraries and their scores", library_score_temp)
	print("List of libraries with high scores", library_score)
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
		"score": sum(list(map(lambda x: book_scores[x], scores)))
		}

	signup()
	book_signing()