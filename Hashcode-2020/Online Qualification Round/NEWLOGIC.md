# This is the main new logic that I will be using for the new file

- Main Variables used:
	1. number_of_books, number_of_libraries, number_of_days
	2. book_scores --> a dictionary containing keys as the book id and values as the respective books scores
	3. signed_up --> a list containing the IDs of the libraries which are valid and are signed up
	4. signed_up_valid --> a list containing the IDs of the valid signed up libraries
	5. books --> a set containing the IDs of books that have already been scanned
	6. library_books --> a list that will contain the book IDs of each library
	7. scores --> a list containing scores of the books(taken during input)
	8. libraries --> a dictionary containing all details of all libraries
		a. "library books number": number of books that the particular library contains
		b. "books": the book IDs of the libraries in sorted order based on their score
		c. "signup": the number of days the library takes to signup
		d. "limit": the limit to the number of books that can be signed each day
		e. "average" the average score of each book in the library
		f. "valid": a boolean to check if the library is valid or not

- The Logic:  
	1. Reading input from the input file  
		- average = sum of scores of books of the library / number of books  
		- sort the books of each library based on their score  
	2. Signing up the libraries  
		- create a list which contains IDs of the libraries in sorted order based on their average  
		- iterate through said list  
		- keep signing up libraries till the days taken is more than the number_of_days and append the library id to the signed_up list  
		- check if the starting day >= number_of_days, if it is, set its checking value to False  
		- TODO: remove all libraries that have more than "n" common books between them(use time.sleep() to reduce CPU load probably) before the signup process starts  
	3. Scanning the books  
		- iterate through the signed_up list  
		- find the maximum number of books that the library can scan  
		- iterate through the books of that library  
		- for each book check if number of books scanned is less than or equal to the maximum number of books and also check if the book is not there in the books set  
		- if the above conditions are satisfied, append the book id to the books scanned list of each library and also to the books set and increment the counter  
