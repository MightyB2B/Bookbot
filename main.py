import sys
from stats import word_count
from stats import letter_count
from stats import sorted_letter_count

if __name__ == '__main__':
    args = sys.argv
    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

        
file_path = sys.argv[1]



#Path of the book to read
#file_path = "books/frankenstein.txt"

#Open the text file, read the contents, and return the contents
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    #Call function "get_book_text" and return contents of book to "book_contents" string
    book_contents = get_book_text(file_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")

    print("----------- Word Count ----------")
    #Call function "word_count" print the returned results
    count = word_count(book_contents)
    print(f"Found {count} total words")

    print("--------- Character Count -------")
    #Call the letter_count function, put returned results into a string "letters_stat"
    letters_stat = letter_count(book_contents)

    #Call the function "sorted_letter count"Take the results from "letter_count" from the variable "letters_stat" and pass the results 
    # to "sorted_letter_count" function to sort through the results and print the results to the console
    #sorted_letters = sorted_letter_count(letters_stat)
    for letters in sorted_letter_count(letters_stat):
        char = letters["char"]
        num = letters["num"]
        print(f"{char}: {num}")

    print("============= END ===============") 

main()
