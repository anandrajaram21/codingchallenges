# Main Algorithm

- Reading Input from the file
	1. While reading input from the file, store all details of all libraries in a dictionary.
	2. Sort the book ids of each library based on their scores.
	3. Each library will have a value called average which is the average score of a book of the library.

- Signing up a library
	1. Make a list with library ids and sort it based on each individual library's "average".
	2. Iterate through this list and start signing up libraries till there is time.
	3. Add a key for each library which tells you on which day it can start scanning books.
	4. Append the libraries signed up to a new list which contains all ids of the signed up libraries.
	5. Remove all the libraries from this list that have their starting date greater than or equal to the total number of days.

	TODO:

	1. Remove all libraries which have more than a specified number of books common between them before signing them up.
	2. Doing this will remove all libraries that have a lot of common books among them and allow room for other libraries to be signed up that have a greater variety of books, thus allowing for a higher score.

- Scanning books from a library
	1. Iterate through the list of signed up libraries.
	2. For each library, find the maximum number of books that it can scan.
	3. Iterate through the books of each library and start scanning.
	4. For each book, first check if the number of books scanned is lesser than or equal to the maximum number of books that it can scan.
	5. If it is lesser, check if that particular book has already been scanned.
	6. If it hasn't been scanned, append the id of the book to a books list which contains the ids of books that have previously been scanned, and also append the id to the scanned books list of each library.