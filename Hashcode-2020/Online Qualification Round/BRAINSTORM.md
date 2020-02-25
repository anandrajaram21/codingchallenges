# ALGORITHM IMPLEMENTATION
- Variables Used:
	1. number_of_books, number_of_libraries, number_of_days
	2. scores
	3. book_scores
		a. book id : book score
	4. libraries
		a. number of books: total number of books in the library
		b. signup : days taken to signup
		c. limit : limit to the number of books that can be signed per day
		d. library books : the array of book ids that each library has(in sorted order based on their scores)
		e. average: average score of each book(sum of scores of all books in the library /  (number of books * signup)) 
		f. scanned books: books that have been scanned by the library
	5. signed_up
	6. signed_up_valid
	7. books
- Algorithm
	a. Signup process
		1. Signup those libraries which have the highest average and the lowest days taken to sign up(basically based on the "average" of each library)
		2. While signing up, add a variable to each library which states the day on which it can start signing books
	b. Book scanning process
		1. Calculate the maximum number of books that a particular library can scan after the starting day((number_of_days - starting day of the library) * limit)
		2. Before scanning a book in the library, check if the number of books scanned by the library is less than or equal to the max number of books
		3. Check if the book is already in the books array
		4. If the book isnt in the books array, append the book id to the scanned books value of each library and also to the books array
		5. Remove those libraries that have the number of scanned books lesser than 1
	c. Write the output to the file