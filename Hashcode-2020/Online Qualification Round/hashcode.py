""" Algorithm Implementation:
1. Sign up those libraries which have the highest score of books
2. Make a for loop that runs in signed up
3. Start signing the books of the libraries from the start date till number_of_days
4. Add the books to an array, and each time before adding, check if the book is already there in the array
5. Calculate the sum of the scores of each book and that is the max.
"""
import json
# Reading the input from the file.
with open("b_read_on.txt") as f:
	number_of_books, number_of_libraries, number_of_days = list(map(int, f.readline().split(" ")))
	book_scores = {}
	signed_up = []
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
		"book_limit": details[2]
		}

def signup(libs):
	days_taken = 0
	for i in libs:
		days = libs[i]['signup']
		days_taken += days
		if days_taken > number_of_days:
			break
		signed_up.append(i)
		libraries[i]['starting_day'] = days_taken + 1
		print(days, days_taken)
	print(signed_up)
	print(json.dumps(libraries))

print(number_of_days)
signup(libraries)
for i in signed_up:
	print(libraries[i]['starting_day'])