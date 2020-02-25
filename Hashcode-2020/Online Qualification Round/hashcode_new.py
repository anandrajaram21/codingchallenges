def sorting(arr):
	sorted_arr = []
	temp_arr = []
	for i in arr:
		temp_arr.append((i, book_scores[i]))
	temp_arr.sort(key=lambda elem: elem[1], reverse=True)
	sorted_arr = list(map(lambda x: x[0], temp_arr))
	return sorted_arr

def signup():
	temp_libraries = []
	for i in libraries:
		temp_libraries.append((i, libraries[i]['average']))
	temp_libraries.sort(key=lambda elem: elem[1], reverse=True)
	sorted_libraries = list(map(lambda x: x[0], temp_libraries))
	days_taken = 0
	for i in sorted_libraries:
		if days_taken >= number_of_days:
			break
		signed_up.append(i)
		days_taken += libraries[i]['signup'] - 1
		libraries[i]['starting day'] = days_taken + 1

def bookscan():
	for i in signed_up:
		max_books = (number_of_days - libraries[i]['starting day']) * libraries[i]['limit']
		counter = 0
		i_books = libraries[i]['library books']
		for j in i_books:
			if counter > max_books:
				break
			if j not in books:
				counter += 1
				libraries[i]['scanned books'].append(j)
				books.append(j)
		libraries[i]['output number of books'] = len(libraries[i]['scanned books'])
		if libraries[i]['output number of books'] > 0:
			signed_up_valid.append(i)

with open("d_tough_choices.txt") as f:
	number_of_books, number_of_libraries, number_of_days = list(map(int, f.readline().split(" ")))
	scores = list(map(int, f.readline().split(" ")))
	book_scores = {}
	signed_up = []
	signed_up_valid = []
	books = []
	for i in range(number_of_books):
		book_scores[i] = scores[i]
	libraries = {}
	for i in range(number_of_libraries):
		details = list(map(int, f.readline().split(" ")))
		book_ids = list(map(int, f.readline().split(" ")))
		sorted_book_ids = sorting(book_ids)
		libraries[i] = {
		"number of books": details[0],
		"signup": details[1],
		"limit": details[2],
		"library books": sorted_book_ids,
		"average": (sum(list(map(lambda elem: book_scores[elem], book_ids))) / (details[0] * details[1])),
		"scanned books": [],
		"output number of books": 0
		}

signup()
bookscan()

with open("d_output.txt", "w+") as output:
	output.write(str(len(signed_up_valid)) + '\n')
	for i in signed_up_valid:
		output.write(str(i) + ' ' + str(libraries[i]['output number of books']) + '\n')
		for j in range(len(libraries[i]['scanned books'])):
			if j == len(libraries[i]['scanned books']) - 1:
				output.write(str(libraries[i]['scanned books'][j]) + '\n')
			else:
				output.write(str(libraries[i]['scanned books'][j]) + ' ')