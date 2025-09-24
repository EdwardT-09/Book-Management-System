# Name: Book Checker (Main Menu)
# Date Created: 22/11/2023
# Date Modified: 11/12/2023
# Function: Contains the different options for user to select

# import os is used to clear terminal using os.system ("cls")
# import datetime is used to get the format for dates
import os
import datetime

''' ANSI Colour codes to print in terminal with coloured text '''


class Colors:
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    BOLD = "\033[1m"
    END = "\033[0m"


''' Prints the message box containing the options for user to choose from '''
# msg parameter is the message to be displayed inside the box
def print_msg_box(msg):
    # lines stores the msg split by line(\n)
    # space is the indent before the message in the box is printed
    # width is used to set the width of the box to the longest line in msg
    lines = msg.split("\n")
    space = " "
    # Map is ued to get the number of characters per item in the list
    width = max(map(len, lines))

    # box stores the message box and contents
    # f"╔{'═' * (width + 2)}╗\n" is the top of the message box based on the width
    # "".join ([f"║{space}{line:<{width}}{space}║\n" for line in lines]) is the height of the message box based on the-
    # -number of items in lines
    # f"╚{'═' * (width + 2)}╝" is the bottom of the message box based on the width
    box = f"╔{'═' * (width + 2)}╗\n"
    box += "".join([f"║{space}{line:<{width}}{space}║\n" for line in lines])
    box += f"╚{'═' * (width + 2)}╝"
    print(box)


''' Prints the name box of the bird above the message box '''
# name parameter is the name of the bookkeeper bird
# Same as print_msg_box (msg), except no bottom is printed
def print_name_box(name):
    lines = name.split("\n")
    space = " "
    width = max(map(len, lines))
    box = f"╔{'═' * (width + 2)}╗\n"
    box += "".join([f"║{space}{line:<{width}}{space}║\n" for line in lines])
    print(box, end="")


''' Displays the bokk information of the books in the library '''


def display_all_books():
    cont = return_to_menu(f"{Colors.BOLD}Display All Books{Colors.END}")
    while cont:
        # Define the format for each line
        format_line = "{:<19} {:<25} {:<35} {:<30} {:<21} {:<17} {:<17} {:<8}"

        # Display header for each category
        print(format_line.format(f"{Colors.BOLD}ISBN", "Author", "Title", "Publisher", "Genre", "Year Published",
                                 "Date Purchased", f"Status{Colors.END}"))

        # search through each line in the text file as a list
        for line in contents:
            # separate each category in the line
            cut = line.strip().split(',')

            # take titles with commas into account
            # merging the separated title into 1
            if len(cut) >= 9:
                cut[2:-5] = [', '.join(cut[2:-5])]

            # extract each information
            isbn, author, title, publisher, genre, year_published, date_purchased, status = cut

            # author_lines is used to split long information into multiple lines
            # this is done using the first element as the first line while the second is the second line
            author_lines = []
            # current_line holds on to each word found in author
            current_line = ""
            # look through each word in author to make sure its length is below 25
            for word in author.split():
                if len(current_line) + len(word) + 1 <= 24:
                    current_line += word + ' '
                else:
                    # If exceeding the limit, add the current line to the list
                    author_lines.append(current_line)
                    # Start new line with the current word
                    current_line = word + ''
            # place current line as second element if exceeds 25
            author_lines.append(current_line)

            # titles_lines is used to split long information into multiple lines
            # this is done using the first element as the first line while the second is the second line
            title_lines = []
            # current_line holds on to each word found in title
            current_line = ""
            # look through each word in title to make sure its length is below 25
            for word in title.split():
                if len(current_line) + len(word) + 1 <= 34:
                    current_line += word + " "
                else:
                    # If exceeding the limit, add the current line to the list
                    title_lines.append(current_line)
                    # Start new line with the current word
                    current_line = word + " "
            # place current line as second element if exceeds 25
            title_lines.append(current_line)

            # publisher_lines is used to split long information into multiple lines
            # this is done using the first element as the first line while the second is the second line
            publisher_lines = []
            # current_line holds on to each word found in publisher
            current_line = ''
            # look through each word in publisher to make sure its length is below 25
            for word in publisher.split():
                if len(current_line) + len(word) + 1 <= 29:
                    current_line += word + ' '
                else:
                    # If exceeding the limit, add the current line to the list
                    publisher_lines.append(current_line)
                    # Start new line with the current word
                    current_line = word + ' '
            # place current line as second element if exceeds 25
            publisher_lines.append(current_line)

            # genre_lines is used to split long information into multiple lines
            # this is done using the first element as the first line while the second is the second line
            genre_lines = []
            # current_line holds on to each word found in genre
            current_line = ''

            for word in genre.split():
                if len(current_line) + len(word) + 1 <= 19:
                    current_line += word + ' '
                else:
                    # If exceeding the limit, add the current line to the list
                    genre_lines.append(current_line)
                    # Start new line with the current word
                    current_line = word + ' '
            # place current line as second element if exceeds 25
            genre_lines.append(current_line)

            # obtain the max length of the line
            max_lines = max(len(author_lines), len(title_lines), len(publisher_lines), len(genre_lines))
            # Print each line with proper formatting
            format_line = "{:<15} {:<25} {:<35} {:<30} {:<20} {:<17} {:<17} {:<7}"

            # Print each line with proper formatting
            for i in range(max_lines):
                # Retrieve the lines or an empty string if not available
                author_line = author_lines[i] if i < len(author_lines) else ""
                title_line = title_lines[i] if i < len(title_lines) else ""
                publisher_line = publisher_lines[i] if i < len(publisher_lines) else ""
                genre_line = genre_lines[i] if i < len(genre_lines) else ""

                # Print the formatted line using the specified format
                print(format_line.format(
                    isbn if i == 0 else "",
                    author_line,
                    title_line,
                    publisher_line,
                    genre_line,
                    year_published if i == 0 else '',
                    date_purchased if i == 0 else '',
                    status if i == 0 else ''
                ))

        input(f"\n{Colors.YELLOW}<Press Enter to Exit to Main Menu>{Colors.END}")
        # Exits to Main Menu
        break


''' Allows user to search for books in the book library '''


def search_for_book():
    def search(data, selection, search_type):
        matches = []

        for book in data:
            # Check if the line has enough columns
            if len(book) < 3:
                continue

            # Determine the search type of book information
            if search_type == '1':
                book_info = book[0]  # ISBN column
                search_label = "ISBN"
            elif search_type == '2':
                book_info = book[2]  # Book title column
                search_label = "book title"
            elif search_type == '3':
                book_info = book[1]  # Author's name column
                search_label = "author"
            else:
                raise ValueError(f"{Colors.LIGHT_RED}Invalid Search Type.{Colors.END}")

            # Convert the information to a string for ISBN search
            if isinstance(book_info, int):
                book_info = str(book_info)

            # Perform case-insensitive string matching for book title
            if selection.lower() in str(book_info).lower():
                matches.append(book)

        return matches, search_label

    def get_valid_input(prompt, input_type, min_value=None, max_value=None):
        # Function to get user input and validate it
        while True:
            user_input = input(prompt)
            os.system("cls")
            try:
                value = input_type(user_input)
                if (min_value is None or value >= min_value) and (max_value is None or value <= max_value):
                    return value
                else:
                    print(f"Please Enter a Value Between {min_value} - {max_value}.")
            except ValueError:
                os.system("cls")
                print(f"{Colors.LIGHT_RED}Invalid! Please Enter a Valid Number.{Colors.END}")

    ''' Removes the "\n" at the end of all items in contents '''
    # i is used to keep track of the index in contents
    i = 0
    # Goes through each item in contents one by one
    for line in contents:
        # Enters if "\n" is in the current item of contents
        if "\n" in line:
            # Deletes the "\n" in the current item by equaling to everything else
            contents[i] = f"{contents[i][0: -1]}"
            i += 1

    cont = return_to_menu(f"{Colors.BOLD}Search for Book{Colors.END}")

    while cont:
        # Split each line into columns (columns are separated by commas)
        book_data = [line.split(', ') for line in contents]

        # Ask the user how they want to search
        print("1. ISBN\n2. Book Title\n3. Author's name")
        search_type = get_valid_input("Please Choose a Method to Search for a Book [Ex: 1, 2, or 3]: ", str)

        # Making the search type a string
        if search_type == '1':
            selection = get_valid_input("Please Enter the ISBN code: ", int)
        elif search_type == '2':
            selection = input("Please Enter the Book's Title: ")
        elif search_type == '3':
            selection = input("Please Enter the Author's Name: ")
        else:
            print(f"{Colors.LIGHT_RED}Invalid!\nPlease Choose a Way to Search for a Book.{Colors.END}")
            continue  # Go back to the start of the loop

        # Search using regular expressions with the search_type argument
        results, search_label = search(book_data, str(selection), search_type)

        if results:
            os.system("cls")
            print(f"{Colors.LIGHT_GREEN}Matching Books:{Colors.END}")
            for i, result_item in enumerate(results, start=1):
                print(f"{i}. {', '.join(result_item)}")
        else:
            os.system("cls")
            # Specific "No matching" message based on search type
            print(f"{Colors.LIGHT_RED}No Matching {search_label} Found.{Colors.END}")

        while True:
            # Ask the user whether they want to continue
            user_input = input("Continue Searching? [Y/N]: ")
            os.system("cls")
            if user_input.upper() == 'N':
                cont = False
                break  # Exit the loop if the user enters anything other than 'yes'
            elif user_input.upper() == 'Y':
                break
            else:
                print(f"{Colors.LIGHT_RED}Invalid!\nPlease Enter Either Y/N.{Colors.END}")

    ''' Adds "\n" to the end of all items in contents except the last item'''
    # i is used to keep track of the index in contents
    i = 0
    # Goes through each item in contents one by one
    for line in contents:
        # Enters if "\n" is not in the current item of contents and i < len (contents), meaning the current item is not-
        # -the last item in contents
        if "\n" not in line and i < len(contents):
            # Adds "\n" by equaling to itself with a "\n" at the end
            contents[i] = f"{contents[i]}\n"
        i += 1


''' Allows user to add multiples books into the book library '''


def add_book():
    # Function created to make each front letter in the word user inputs for variables [book_author, book_title,-
    # -book_publisher, book_genre]
    def capitalize_first_letter(sentence):
        return ' '.join(word.capitalize() for word in sentence.split())

    # Function created to collect the information for the specified number of books
    def get_book_info(NumOfBooks):
        book_info_list = []  # List to hold information for all books
        for i in range(NumOfBooks):
            while True:
                try:
                    # Prompts user to enter ISBN for the book
                    book_isbn = input("Enter ISBN of the Book [Ex: 9780060850524]: ")
                    os.system("cls")
                    if (len(book_isbn) != 13) or (not book_isbn.startswith('978')):
                        raise ValueError(f"{Colors.LIGHT_RED}ISBN Must be 13 Digits, Starting with '978'.{Colors.END}")

                    elif not book_isbn.isdigit():
                        raise ValueError(f"{Colors.LIGHT_RED}ISBN Must Contain Only Digits.{Colors.END}")

                    # Raises error if ISBN entered already exists in book library
                    for line in contents:
                        if book_isbn in line:
                            raise ValueError(f"{Colors.LIGHT_RED}Duplicate ISBN Found in Book Library.{Colors.END}")
                    break

                except ValueError as e:
                    os.system("cls")
                    print(f"{Colors.LIGHT_RED}Invalid!{Colors.END}\n", e)

            '''
            Prompt user to insert author, title, publisher, and genre of the book 
            Each front letter in the string data user insert must be capitalized before getting saved
            '''
            while True:
                try:
                    # User enter author of the book
                    book_author = input("Enter the Author of the Book: ")
                    os.system("cls")
                    # Check to ensure author name contains at least one letter and no comma
                    for x in book_author.lower():
                        if x in letters:
                            i += 1
                    if i == 0 or book_author == "":
                        raise ValueError(f"{Colors.LIGHT_RED}Invalid!\nPlease Ensure that the Author's Name Contains"
                                         f" at Least 1 Letter and No \",\".{Colors.END}")
                    elif "," in book_author:
                        raise ValueError(f"{Colors.LIGHT_RED}Invalid!\nPlease Ensure that the Author's Name Contains"
                                         f" at Least 1 Letter and No \",\".{Colors.END}")
                    book_author = capitalize_first_letter(book_author)
                    break
                except ValueError as e:
                    os.system("cls")
                    print(e)

            while True:
                try:
                    # User enter title of the book
                    book_title = input("Enter the Title of the Book: ")
                    os.system("cls")
                    # Check to ensure title contains at least one letter or number
                    for x in book_title.lower():
                        if x in characters:
                            i += 1
                    if i == 0 or book_title == "":
                        raise ValueError(f"{Colors.LIGHT_RED}Invalid!\nPlease Ensure the Title Contains at Least"
                                         f" 1 Letter or Number.{Colors.END}")
                    book_title = capitalize_first_letter(book_title)
                    break
                except ValueError as e:
                    os.system("cls")
                    print(e)

            while True:
                try:
                    # User enter publisher of the book
                    book_publisher = input("Enter the Publisher of the Book: ")
                    os.system("cls")
                    # Checking user to input only string values except special symbols
                    for x in book_publisher.lower():
                        if x in characters:
                            i += 1
                    if i == 0 or book_publisher == "":
                        raise ValueError(f"{Colors.LIGHT_RED}Invalid!\nPlease Ensure the Publisher Contains at Least"
                                         f" 1 Letter or Number.{Colors.END}")
                    book_publisher = capitalize_first_letter(book_publisher)
                    break
                except ValueError as e:
                    os.system("cls")
                    print(e)

            while True:
                try:
                    # User enter genre of the book
                    book_genre = input("Enter the Genre of the book: ")
                    os.system("cls")
                    # Checking user to input only string values except special symbols
                    if not book_genre.replace(' ', '').isalpha():
                        raise ValueError(f"{Colors.LIGHT_RED}Invalid!\nPlease Letters Only.{Colors.END}")
                    book_genre = capitalize_first_letter(book_genre)
                    break
                except ValueError as e:
                    os.system("cls")
                    print(e)

            while True:
                try:
                    # Prompt user to insert year published and warn them to use 4 digits only
                    year_published = int(input("Enter the Year this Book was Published [Ex: 2004]: "))
                    os.system("cls")

                    # Code for checking user only input years in the 4 digits only
                    if len(str(year_published)) != 4:
                        raise ValueError
                    break
                except ValueError:
                    os.system("cls")
                    print(f"{Colors.LIGHT_RED}Invalid!\nPlease Enter the Year in the Format, \"YYYY\".{Colors.END}")

            while True:
                try:
                    # Prompt user to insert date purchased and warn them to write in the format given
                    date_purchased = input("Enter the Date this Book was Purchased [Ex: 20-02-2020]: ")
                    os.system("cls")

                    # Users must follow the format given to input the date and it makes them input the date again
                    datetime.datetime.strptime(date_purchased, "%d-%m-%Y")
                    break
                except ValueError:
                    os.system("cls")
                    print(f"{Colors.LIGHT_RED}Invalid!\nPlease Enter Date in the Format, \"DD-MM-YYYY\".{Colors.END}")

            while True:
                try:
                    # Prompt user to insert status of the book and warn them to only use 1 for to-read and 2 for read
                    status = int(input("Enter the status of the book [1 = to-read] or [2 = read]: "))
                    os.system("cls")

                    # If the user insert value other than 1 and 2, then give the users a warning and makes them to-
                    # -enter the data again
                    if status not in [1, 2]:
                        raise ValueError
                    break
                except ValueError:
                    os.system("cls")
                    print(f"{Colors.LIGHT_RED}Invalid!\nEnter Either 1 for \"to-read\" or 2 for \"read\".{Colors.END}")

            # Determine book status based on input
            book_status = "to-read" if status == 1 else "read"

            # Collect all book info and append it to the list
            book_info = (f"{book_isbn}, {book_author}, {book_title}, {book_publisher}, {book_genre}, {year_published},"
                         f" {date_purchased}, {book_status}")
            contents.append(str(book_info))
            print(f"{Colors.LIGHT_GREEN}Book title:{Colors.END} \"{book_title}\" {Colors.LIGHT_GREEN}"
                  f"Successfully Added.{Colors.END}")

    # letters is used to ensure at least one letter is entered for an input
    # characters is used to ensure at least one letter or number is entered for an input
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
               "t", "u", "v", "w", "x", "y", "z"]
    characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                  "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # Asks user for confirmation to continue
    cont = return_to_menu(f"{Colors.BOLD}Add Book{Colors.END}")
    # Main Loop
    while cont:
        # Ask user for the number of books to add
        # Loop 1 nested in main loop
        while True:
            # Checking input so, user only enter 1 or 2 as input
            try:
                NumOfBooks = int(input("Number of Books to Add: "))
                os.system("cls")
                break
            except ValueError as e:
                os.system("cls")
                print(f"{Colors.LIGHT_RED}Invalid!\nPlease Enter a Number.{Colors.END}")
        # Collect information for multiple books
        get_book_info(NumOfBooks)

        while True:
            try:
                addBookAgain = int(input("1. Add More Books."
                                         "\n2. Exit to Main Menu."
                                         "\nChoose One [Ex: 1]:  "))
                os.system("cls")
                if addBookAgain not in [1, 2]:
                    raise ValueError(f"{Colors.LIGHT_RED}Invalid!\nPlease Enter Either 1 or 2.{Colors.END}")
                break
            except ValueError:
                os.system("cls")
                print(f"{Colors.LIGHT_RED}Invalid!\nPlease Enter Either 1 or 2.{Colors.END}")

        if (addBookAgain == 1):
            pass
        elif (addBookAgain == 2):
            cont = False

    ''' Adds "\n" to the end of all items in contents except the last item'''
    # i is used to keep track of the index in contents
    i = 0
    # Goes through each item in contents one by one
    for line in contents:
        # Enters if "\n" is not in the current item of contents and i < len (contents), meaning the current item-
        # -is not the last item in contents
        if "\n" not in line and i < len(contents):
            # Adds "\n" by equaling to itself with a "\n" at the end
            contents[i] = f"{contents[i]}\n"
        i += 1


''' Allows user to edit selected books in the book library '''


def edit_book():
    i = 0
    ''' Removes the "\n" at the end of all items in contents '''
    # Goes through each item in contents one by one
    for line in contents:
        # Enters if "\n" is in the current item of contents
        if "\n" in line:
            # Deletes the "\n" in the current item by equaling to everything else
            contents[i] = f"{contents[i][0: -1]}"
            i += 1

    # these alphabets are used to make sure that empty string is not accepted
    # at least an alphabet have to be used in the necessary inputs
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']

    # Asks user for confirmation to continue
    cont = return_to_menu(f"{Colors.BOLD}Edit Book{Colors.END}")

    # only run when true.
    # turns false when user enters 'n' into the modifying more books input
    # Main Loop
    while cont:
        # identifier is used to search for the book in the list
        identifier = ''
        # add more information into the same book
        addInfo = True
        # to retrieve old information
        old_info = []
        # retrieve new information to change
        new_info = []
        # slice the book's specific line into individual elements in the list
        cut = []
        # the specific line of the searched book
        lines = None

        # loops when error occurs in the input of identifier and id_method
        # name( to keep track) = infinity loop 1
        # nested in main loop (cont)
        while True:
            try:
                # prompt user to enter the method of identifying the book
                print("1. ISBN\n2. Author's Name & Book Title")
                id_method = int(input("Use the ISBN or the Author's Name & Book Title to Find the Book: "))
                os.system('cls')
                # only allows '1' and '2' to be inputted
                assert id_method == 1 or id_method == 2
            # does not accept any number other than 1 and 2 as well as anything that is not a value
            except (AssertionError, ValueError):
                os.system('cls')
                print(f"{Colors.LIGHT_RED}Invalid!\nPlease Enter Either 1 or 2.{Colors.END}")
                # continue loop to try again
                continue
            else:
                # name = infinity loop 2
                # nested in infinity loop 1
                while True:
                    # only runs when id_method is 1
                    if id_method == 1:
                        # name = infinity loop 3
                        # nested in infinity loop 2
                        while True:
                            # prompts user to enter the ISBN of the books
                            try:
                                identifier = int(input("Please Enter the ISBN: "))
                                os.system('cls')
                                # ensure that the ISBN entered is valid to 13 places only and starts with 978
                                assert 9780000000000 <= identifier <= 9789999999999

                            # error occurs when place is not 13 places or ISBN provided does not start with 978
                            # also an error when invalid value is provided
                            except (AssertionError, ValueError):
                                os.system('cls')
                                print(f'{Colors.LIGHT_RED}Invalid!\nISBN Must be 13 Digits and Start with 978.'
                                      f'{Colors.END}')
                                continue

                            # move on with the program when ISBN is true
                            else:
                                # ensures that it will not move into if author_title code
                                # This is because the block of code is only used when id_method is selected
                                author_title = False
                                # break infinity loop 3
                                break
                    # when 2 is selected this block of code will be executed
                    # the reason elif id_method is unnecessary because assert have defined
                    # that 1 and 2 are the only acceptable input
                    else:
                        # prompt user to enter the author's name and book title
                        author = input("Please Enter the Author's Name: ")
                        os.system('cls')
                        title = input("Please Enter the Book Title: ")
                        os.system('cls')
                        # author_title is true to execute if author_title block of code
                        author_title = True
                        # format to fit into the variable, identifier
                        identifier = f"{author}, {title}"

                    # used to track whether the book has been found
                    i = 0

                    # search each line of book in contents
                    for line in contents:
                        # split each line when comma is found into individual information
                        place = line.split(', ')
                        # join the author and title into one element
                        place = str([", ".join(place[1: -5])])
                        place = place.lower()[2:-2]

                        # execute when id_method == 2
                        if author_title:
                            # execute when identifier matches the information in text file
                            if identifier.lower() == place.lower():
                                lines_idx = contents.index(line)
                                print(f"{Colors.LIGHT_GREEN}Book Found For{Colors.END} \"{Colors.BOLD}{identifier}"
                                      f"{Colors.END}\"")
                                i += 1
                                break
                        # execute when author_title is false
                        else:
                            # executes when id_method == 1
                            if str(identifier) in line:
                                lines_idx = contents.index(line)
                                print(f"{Colors.LIGHT_GREEN}Book Found.{Colors.END}")
                                i += 1
                                break
                    # when the above if else code is not executed, i will have any increment
                    # remaining the i at 0
                    if i == 0:
                        print(f"{Colors.LIGHT_RED}Book Not found.{Colors.END}")
                        # Name = infinity loop 4
                        # nested in infinity loop 2
                        while True:
                            try:
                                # prompt user to enter whether they would like to search for books again
                                again = input("Try Again? [Y/N]").lower()
                                os.system('cls')
                                # only accept 'y' and 'n' as an answer
                                assert again == 'y' or again == 'n'
                            # display error message when neither y nor n is entered
                            except AssertionError:
                                print(f'{Colors.LIGHT_RED}Invalid!\nPlease Enter Either Y/N{Colors.END}')

                            else:
                                # break infinity loop 4
                                break
                        # when 'y' is entered, the search runs again
                        if again == 'y':
                            continue
                        # when 'n' is entered, thank you message shows and the code quits
                        else:
                            cont = False
                            # break infinity loop 2
                            break

                    # when if else above is executed, this else block will execute and move on to the next code
                    else:
                        # break infinity loop 2
                        break
                # break infinity loop 1
                break
        # when cont is false
        if not cont:
            # break cont
            break

        # split the information of the book individually
        cut = str(line).split(',')

        # to ensure that books with titles are turned into 1 element into the list
        if len(cut) >= 9:
            cut[2:-5] = [', '.join(cut[2:-5])]

        # nested in cont
        while addInfo:
            try:
                # prompt user to input the information of the book they want to modify
                print(f'1.{Colors.BOLD}ISBN:{Colors.END} {cut[0]}\n2.{Colors.BOLD}Author:{Colors.END}{cut[1]}\n'
                      f'3.{Colors.BOLD}Title:{Colors.END}{cut[2]}\n4.{Colors.BOLD}Publisher:{Colors.END}{cut[3]}\n'
                      f'5.{Colors.BOLD}Genre:{Colors.END}{cut[4]}'
                      f'\n6.{Colors.BOLD}Year Published:{Colors.END}{cut[5]}\n7.{Colors.BOLD}'
                      f'Date Purchased:{Colors.END}{cut[6]}\n8.{Colors.BOLD}Status:{Colors.END}{cut[7]} ')
                category = int(input('Which category would you like to change?[Ex: 1]: '))
                os.system('cls')
                # ensure that the input is within the range of 1 to 8
                assert 1 <= category <= 8
            # display error message and prompt the use to input again
            except (AssertionError, ValueError):
                os.system('cls')
                print(
                    f"{Colors.LIGHT_RED}Invalid!\nValue is Not Between 1 - 8 or value is invalid.{Colors.END}")
            # execute when input for category is accepted
            else:
                match category:
                    # prompt user to enter new information
                    # category == 1 is for ISBN
                    case 1:
                        # Name = infinity loop 5
                        # nested in addInfo
                        while True:
                            try:
                                # old ISBN is retrieved and displayed
                                old_info = cut[0]
                                print('Current ISBN:', old_info)
                                # prompt user to enter the ISBN
                                new_info = input("Enter the New ISBN: ")
                                os.system('cls')
                                # ensure ISBN is only digits
                                if not new_info.isdigit():
                                    raise Exception(f'{Colors.LIGHT_RED}Invalid!\nISBN Must be 13 Digits and'
                                                    f' Start with 978.{Colors.END}')
                                # ensure no duplicate ISBN in book library
                                for line in contents:
                                    if str(new_info) == line.split(", ")[0]:
                                        raise Exception(f'{Colors.LIGHT_RED}Invalid!\nDuplicate ISBN Found in'
                                                        f' Book Library.{Colors.END}')
                                # ensure that the new ISBN entered starts with a 978 and has 13 places
                                if int(new_info) < 9780000000000 or int(new_info) > 9789999999999:
                                    raise Exception(f'{Colors.LIGHT_RED}Invalid!\nISBN Must be 13 Digits and'
                                                    f' Start with 978.{Colors.END}')

                            # display error message
                            # prompt the user with new ISBN input again when error occurs
                            except Exception as e:
                                os.system('cls')
                                print(e)

                            # execute when new ISBN is accepted
                            else:
                                # break infinity loop 5
                                break

                    # category == 2 is used for author's name
                    case 2:
                        # Name = infinity loop 6
                        # nested in addInfo
                        while True:
                            # used to track for errors
                            i = 0
                            # old author's name is retrieved and displayed
                            old_info = cut[1]
                            print(f'Current Author: \b{old_info}')
                            # prompt user to enter the new author's name:
                            new_info = input("Enter the New Author: ")
                            os.system('cls')
                            new_info = ' ' + str(new_info)
                            for x in new_info.upper():
                                # execute when new_info consists of at least 1 alphabet
                                if x in alphabet:
                                    # i increase by 1 for error handling
                                    i += 1
                            # when i did not increase from the if statement above or consists of a ','.
                            # prompts the user to reenter new author's name
                            if i == 0 or "," in new_info:
                                print(f"Invalid!\nPlease Ensure Author Contains at Least One Letter and No \",\".")
                                continue
                            # when new_info is accepted, the code stops looping
                            else:
                                # break infinity loop 6
                                break

                    # category == 3 is used for book title
                    case 3:
                        # Name = infinity loop 7
                        # nested in addInfo
                        while True:
                            # used to track for errors
                            i = 0
                            # old title is retrieved and displayed
                            old_info = cut[2]
                            print(f'Current Title: \b{old_info}')
                            # prompt user to enter the new title
                            new_info = input("Enter the New Title: ")
                            os.system('cls')
                            new_info = ' ' + str(new_info)
                            for x in new_info.upper():
                                # execute when new_info consists of at least 1 alphabet
                                if x in alphabet:
                                    i += 1
                            # when i did not increase from the if statement above or consists of a ','.
                            # prompts the user to reenter title
                            if i == 0:
                                print(f"{Colors.LIGHT_RED}Invalid!\nPlease Ensure Title Contains at Least One"
                                      f" Letter or Number.{Colors.END}")
                                continue
                            # when new_info is accepted, the code stops looping
                            else:
                                # break infinity loop 7
                                break
                    # category == 4 is used for publisher name
                    case 4:
                        # Name = infinity loop 8
                        # nested in addInfo
                        while True:
                            # used to track for errors
                            i = 0
                            # old publisher name is retrieved and displayed
                            old_info = cut[3]
                            print(f'Current Publisher: \b{old_info}')
                            # prompt user to enter the new publisher name
                            new_info = input("Enter the New Publisher: ")
                            os.system('cls')
                            new_info = ' ' + str(new_info)
                            for x in new_info.upper():
                                # execute when new_info consists of at least 1 alphabet
                                if x in alphabet:
                                    i += 1
                            # when i did not increase from the if statement above or consists of a ','.
                            # prompts the user to reenter a new publisher name
                            if i == 0 or "," in new_info:
                                print(f"{Colors.LIGHT_RED}Invalid!\nPlease Ensure Publisher Contains at Least One"
                                      f" Letter and No \",\".{Colors.END}")
                                continue
                            # when new_info is accepted, the code stops looping
                            else:
                                # break infinity loop 8
                                break
                    # category == 5 is used for genre
                    case 5:
                        # Name = infinity loop 9
                        # nested in addInfo
                        while True:
                            # used to track for errors
                            i = 0
                            # old genre is retrieved and displayed
                            old_info = cut[4]
                            print(f'Current Genre: \b{old_info}')
                            # prompt user to enter the new genre
                            new_info = input("Enter the New Genre: ")
                            os.system('cls')
                            new_info = ' ' + str(new_info)
                            for x in new_info.upper():
                                # execute when new_info consists of at least 1 alphabet
                                if x in alphabet:
                                    i += 1
                            # when i did not increase from the if statement above or consists of a ','.
                            # prompts the user to reenter new genre
                            if i == 0 or "," in new_info:
                                print(f"{Colors.LIGHT_RED}Invalid!\nPlease Ensure Genre Contains at Least One"
                                      f" Letter and No \",\".{Colors.END}")
                                continue
                            # when new_info is accepted, the code stops looping
                            else:
                                # break infinity loop 9
                                break
                    # category == 6 is used for year published
                    case 6:
                        # Name = infinity loop 10
                        # nested in addInfo
                        while True:
                            try:
                                # old year published is retrieved and displayed
                                old_info = cut[5]
                                print(f'Current Year Published: \b{old_info}')
                                # prompt user to enter the new year published
                                new_info = int(input("Enter the New Year Published: "))
                                os.system('cls')
                                # ensure that the year only has 4 places
                                # ensures that the year provided is not more than the year the book was purchased
                                assert 1000 <= new_info <= 9999 and new_info <= int(cut[6][7:])

                            # error handling for invalid values, invalid year and year published is more than the-
                            # -year purchased
                            except (AssertionError, ValueError):
                                os.system('cls')
                                print(f"{Colors.LIGHT_RED}Invalid!\nPlease Ensure Year Published is 4 Digits and in the"
                                      f" Format, \"YYYY\" or that the year does not exceed the date of purchase."
                                      f"{Colors.END}")
                            # ensures that the year provided is valid with 4 places
                            else:
                                new_info = ' ' + str(new_info)
                                # break infinity loop 10
                                break

                    # category == 7 is used for date purchased
                    case 7:
                        # Name = infinity loop 11
                        # nested in addInfo
                        while True:
                            try:
                                # old date purchased is retrieved and displayed
                                old_info = cut[6]
                                print(f'Current Date Purchased: \b{old_info}')
                                # prompt user to enter the new date purchased
                                year = int(input("Enter the Year: "))
                                os.system('cls')
                                month = int(input("Enter the Month: "))
                                os.system('cls')
                                day = int(input("Enter the Day: "))
                                os.system('cls')
                                new_info = datetime.date(year, month, day)
                                new_info = str(new_info.strftime("%d-%m-%Y"))
                                # ensure that the year purchased is not less than the year published
                                assert year >= int(cut[5])

                            # error handling for invalid values and year purchased is less than the year published
                            except (AssertionError, ValueError):
                                os.system('cls')
                                print(f"{Colors.LIGHT_RED}Invalid!\nPlease Enter the Year, Month, then Day or ensure"
                                      f"that the date of publish does not exceed the date of purchase.{Colors.END}")
                                continue
                            new_info = ' ' + str(new_info)
                            # break infinity loop 11
                            break

                    # category == 8 is used for status
                    case 8:
                        # Name = infinity loop 12
                        # nested in addInfo
                        while True:
                            # old status is retrieved and displayed
                            old_info = cut[7]
                            print(f'Current Status: \b{old_info}')
                            # prompt user to status
                            new_info = input("Enter the New Status [read / to-read]: ")
                            os.system('cls')
                            # ensures that only to-read and read are the only status
                            if new_info == 'to-read' or new_info == 'read':
                                new_info = ' ' + str(new_info)
                                # break infinity loop 12
                                break
                            else:
                                print(f"{Colors.LIGHT_RED}Invalid!\nPlease Enter Either \"read\" or"
                                      f" \"to-read\".{Colors.END}")
                # replace old information with new information
                contents[lines_idx] = contents[lines_idx].replace(old_info, new_info)
                cut[category - 1] = new_info
                print(f"{Colors.LIGHT_GREEN}Successfully Changed to{Colors.END} \"{Colors.BOLD}"
                      f"{contents[lines_idx]}{Colors.END}\".")

                # Prompt user on whether they would like to modify more information
                # Name = infinity loop 13
                # nested in addInfo
                while True:
                    extra_changes = input('Change More Information of this Book? [Y/N]: ').lower()
                    os.system('cls')
                    if extra_changes == 'y':
                        # rerun to prompt user to choose which information to change again
                        addInfo = True
                    elif extra_changes == 'n':
                        print(f'{Colors.LIGHT_GREEN}Successful Updated Book Information.{Colors.END}')
                        addInfo = False
                    else:
                        print(f'{Colors.LIGHT_RED}Invalid!\nPlease Enter Either Y/N.{Colors.END}')
                        addInfo = False
                        continue
                    # break infinity loop 13
                    break
                # continue addInfo
                continue
        # prompt users to enter whether they would like to change information for other books
        # infinity loop 14
        # nested loop of cont
        while True:
            extra_changes = input("Would you like to change other book's information? [Y/N] : ").lower()
            os.system('cls')
            if extra_changes == 'y':
                # break infinity loop 14
                break
            elif extra_changes == 'n':
                cont = False
                # break infinity loop 14
                break
            else:
                print(f'{Colors.LIGHT_RED}Invalid!\nPlease Enter Either Y/N.{Colors.END}')

    # Adds "\n" to the end of all items in contents except the last item'''
    # i is used to keep track of the index in contents
    i = 0
    # Goes through each item in contents one by one
    for line in contents:
        # Enters if "\n" is not in the current item of contents and i < len (contents),
        # meaning the current item is not the last item in contents
        if "\n" not in line and i < len(contents):
            # Adds "\n" by equaling to itself with a "\n" at the end
            contents[i] = f"{contents[i]}\n"
        i += 1


''' Allows user to delete multiple books from the book library '''
def delete_book():
    ''' Deletes the selected book from book_list and from content '''
    # idx parameter is the index in book_list of the item to be deleted
    def delete(idx):
        # Informs user that the book has been deleted
        print(f"{Colors.LIGHT_GREEN}Deleted{Colors.END} \"{Colors.BOLD}{book_list[idx]}{Colors.END}\"")
        # "content.index (book_list [idx])" returns the index in contents of the book to delete
        del contents[contents.index(book_list[idx])]
        del book_list[idx]

    ''' ASks user if they wish to continue searching for books to delete '''
    def stop_loop():
        while True:
            # Enters if len (contents) != 0, meaning there is at least one book left in the book library
            if len(contents) != 0:
                # Prompts user to choose whether to continue searching for books to delete or not-
                # -(end stores the input)
                end = input(f"Continue Searching for Books to Delete? [Y/N]: ")
                os.system("cls")

                # Enters if user does not enter either y/Y or n/N
                # Executes its body contents
                # Returns to start of Loop - 4
                # .upper() is used to accept y/Y and n/N
                if end.upper() != "Y" and end.upper() != "N":
                    # Informs user to only enter either Y/N
                    print(f"{Colors.LIGHT_RED}Invalid!\nPlease Enter Either Y/N.{Colors.END}")
                    # Returns to start of this loop
                    continue
                # Enters if user chooses to continue searching for books to delete (end == "Y")
                elif end.upper() == "Y":
                    # Continues Main Loop
                    cont = True
                    # Exits function loop
                    break
                # Enters if user chooses not to continue searching for books to delete (end == "N")
                else:
                    # Stops Main Loop from executing
                    cont = False
                    # Exits function loop
                    break
            # Enters if there are no more books left in the book library
            else:
                # Informs user that the book library is empty and that they returned to the main menu
                input(f"{Colors.YELLOW}Book Library is Empty\nPress Enter to Return to Main Menu{Colors.END}")
                # Stops main loop from executing
                cont = False
                # Exits Loop - 4 (Back to Main Loop)
                break
        return cont

    ''' Prints the books found with the key-word '''
    def print_books_found():
        # i is used to prevent f"Book(s) Found with \"{key_word}\": " from printing more than once
        # i is also used to number the items in book_list when printed out
        i = 0
        # Goes through each item in book_list one by one
        for line in book_list:
            if i == 0:
                # Informs user that a book with key-word was found
                print(f"{Colors.LIGHT_GREEN}Book(s) Found with{Colors.END} \"{Colors.BOLD}{key_word}{Colors.END}\": ")
                i += 1
            if i != 0:
                # Prints each item in book_list
                print(f"{f'{i}.' : <3} {line}")
                i += 1

        # Enters if "0" is accepted as a valid input
        if not more:
            # Informs the user that entering "0" will exit the page
            print(f"{Colors.YELLOW}<To Exit Page, Enter \"0\">{Colors.END}")

    more = False
    ''' Removes the "\n" at the end of all items in contents '''
    # i is used to keep track of the index in contents
    i = 0
    # Goes through each item in contents one by one
    for line in contents:
        # Enters if "\n" is in the current item of contents
        if "\n" in line:
            # Deletes the "\n" in the current item by equaling to everything else
            contents[i] = f"{contents[i][0: -1]}"
            i += 1

    # Asks user for confirmation to continue
    cont = return_to_menu(f"{Colors.BOLD}Delete Book{Colors.END}")
    """ (Delete Function) Main loop """
    while cont:
        # low_content stores the same items as contents, except in lower case
        # book_list stores the books with key-word that were found
        # more is used to differentiate whether to print "<To Exit Page, Enter \"0\">" or not
        # found is used to differentiate when a book with key-word is found or not
        low_content = [line.lower() for line in contents]
        book_list = []
        more = False
        found = False

        # Prompts user to search the book library for the key-word they enter (key_word stores the input)
        key_word = input("Search Book Library for: ")
        # Clears terminal
        os.system("cls")

        ''' Searches for books in low_contents for the key-word(lower case) entered '''
        # i is used to prevent "f"Book(s) Found with \"{Colors.BOLD}{key_word}{Colors.END}\": "" from printing more-
        # -than once
        # i is used to number the items in book_list when printed out
        # i is used to determine how many books with key-word are found
        # i is used to determine how many books with the key-word are left to delete
        i = 0
        # Goes through each item in low_content one by one
        for line in low_content:
            # Enters if key-word(lower case) is in the current item of low_content and is not empty or just a comma-
            # -or space
            # Searches with lower case to avoid case sensitivity
            if key_word.lower() in line and key_word != "" and key_word != " " and key_word != "," and key_word != ", ":
                found = True
                if i == 0:
                    # Informs user that a book with key-word was found
                    print(
                        f"{Colors.LIGHT_GREEN}Book(s) Found with{Colors.END} \"{Colors.BOLD}{key_word}{Colors.END}\": ")
                    i += 1
                if i != 0:
                    # Adds each book(not lower case) found with the key-word to book_list
                    book_list.append(contents[low_content.index(line)])
                    # Prints the book(s)(not lower case) found with the key-word
                    print(f"{f'{i}.' : <3} {book_list[i - 1]}")
                    i += 1

        # Enters if no book is found with the key-word
        if not found:
            # Informs user that no books with key-word were found
            print(f"{Colors.LIGHT_RED}No Book Found with{Colors.END} \"{Colors.BOLD}{key_word}{Colors.END}\"")
            # Prompts user to continue or not
            cont = stop_loop()

        # Enters if at least one book is found with the key-word
        else:
            # Enters if i > 2, meaning more than one book with the key-word is found
            if i > 2:
                # Informs the user that entering "0" will exit the page
                print(f"{Colors.YELLOW}<To Exit Page, Enter \"0\">{Colors.END}")

                """ Loop - 1 (Nested in Main Loop) """
                ''' Asks user to select which books to delete '''
                while True:
                    try:
                        # Prompts user to choose which book to delete (choice stores the input)
                        # Raises ValueError if a number is not entered
                        choice = int(input("Choose a Book to Delete [Ex: 1]: "))
                        os.system("cls")

                        # Raises AssertionError if number entered is not between 0 - (i - 1)[(i - 1) = Total number of-
                        # -books with key-word found]
                        assert 0 <= choice <= (i - 1)

                    # Enters if an error is raised
                    # Executes its body contents
                    # Returns to start of Loop - 1
                    except (ValueError, AssertionError):
                        os.system("cls")
                        # print_books_found() reprints all the books with key-word excluding the deleted books
                        print_books_found()
                        # Informs the user to only enter a number between 0 - (i - 1)
                        print(f"{Colors.LIGHT_RED}Invalid!\nPlease Enter a Number Between 0 - {i - 1}.{Colors.END}")

                    # Enters if there is no error raised
                    else:
                        # Enters if choice is not "0", when user selects a book to delete
                        if choice != 0:
                            # delete_book (idx) deletes the selected book from contents
                            # more = True prevents "f"{Colors.YELLOW}<To Exit Page, Enter \"0\">{Colors.END}"" from-
                            # -printing
                            delete(choice - 1)
                            more = True
                            print_books_found()

                            # Iterates i by -1 when a book is deleted
                            i -= 1

                            """ Loop - 2 (Nested in Loop - 1) """
                            ''' Asks user if they wish to delete more books from the ones found with the key-word '''
                            # Enters loop if (i - 1) > 0, meaning there is at least one book with key-word left to-
                            # -delete
                            while (i - 1) > 0:
                                # Prompts user to choose to delete more or stop (confirm stores the input)
                                confirm = input("Delete More from this List? [Y/N]: ")
                                os.system("cls")

                                # Enters if user chooses to delete more books with key-word (confirm == "Y")
                                # .upper() is used to accept y/Y
                                if confirm.upper() == "Y":
                                    # Resets more if user chooses to delete more
                                    more = False
                                    print_books_found()
                                    # Exits Loop - 2 (Back to Loop - 1)
                                    break
                                # Enters if user chooses not to delete more (confirm == "N")
                                # .upper() is used to accept n/N
                                elif confirm.upper() == "N":
                                    # Exits Loop - 2 (Back to Loop - 1)
                                    break
                                # Enters if user does not enter either y/Y or n/N
                                # Executes its body contents
                                # Returns to start of Loop - 2
                                else:
                                    print_books_found()
                                    # Informs the user to only enter either Y/N
                                    print(f"{Colors.LIGHT_RED}Invalid!\nPlease Enter Either Y/N.{Colors.END}")

                            # Enters if user chooses to delete more books and there is at least one book with key-word-
                            # -left to delete
                            if confirm.upper() == "Y" and (i - 1) > 0:
                                # Returns to start of Loop - 1
                                continue
                            # Enters if user chooses not to delete more books or there is no more books with key-word-
                            # -left to delete
                            else:
                                # Enters if i == 1, meaning there are no more books with key-word to delete
                                if i == 1:
                                    # Informs user that all books with key-word have been deleted
                                    print(f"{Colors.YELLOW}All Books with{Colors.END} \"{Colors.BOLD}{key_word}"
                                          f"{Colors.END}\" {Colors.YELLOW}Have Been Deleted.{Colors.END}")
                                    # Exits Loop - 1 (Back to Main Loop)
                                    break
                                # Enters if there still books with the key-word to delete
                                else:
                                    # Exits Loop - 1 (Back to Main Loop)
                                    break

                        # Enters if choice == 0, meaning user chooses to exit the page
                        else:
                            # Exits Loop - 1 (Back to Main Loop)
                            break

            # Enters if only one book with key-word is found
            else:
                """ Loop - 3 (Nested in Main Loop) """
                ''' Asks user if they wish to delete the one book with key-word found '''
                while True:
                    # Prompts user to choose whether to delete the one book with key-word or not-
                    # -(confirm stores the input)
                    confirm = input("Delete this Book? [Y/N]: ")
                    os.system("cls")

                    # Enters if user chooses to delete the book (confirm == "Y")
                    # .upper() is used to accept y/Y
                    if confirm.upper() == "Y":
                        # delete_book (0) deletes the book
                        delete(0)
                        # Exits Loop - 3 (Back to Main Loop)
                        break
                    # Enters if user chooses not to delete the book (confirm == "N")
                    # .upper() is used to accept n/N
                    elif confirm.upper() == "N":
                        # Exits Loop - 3 (Back to Main Loop)
                        break
                    # Enters if user does not enter either y/Y or n/N
                    # Executes its body contents
                    # Returns to start of Loop - 3
                    else:
                        # Reprints the book with key-word that was found
                        print(f"{Colors.LIGHT_GREEN}Book(s) Found with{Colors.END} \"{Colors.BOLD}{key_word}"
                              f"{Colors.END}\": \n1. {str(book_list[0])}")
                        # Informs the user to only enter either Y/N
                        print(f"{Colors.LIGHT_RED}Invalid!\nPlease Enter Either Y/N.{Colors.END}")

            # Prompts user to choose to continue or not
            cont = stop_loop()

    ''' Adds "\n" to the end of all items in contents except the last item'''
    # i is used to keep track of the index in contents
    i = 0
    # Goes through each item in contents one by one
    for line in contents:
        # Enters if "\n" is not in the current item of contents and i < len (contents), meaning the current item-
        # -is not the last item in contents
        if "\n" not in line and i < len(contents):
            # Adds "\n" by equaling to itself with a "\n" at the end
            contents[i] = f"{contents[i]}\n"
        i += 1

    """ Back to Main Menu """


''' Asks user to confirm whether to continue with the function they chose '''
# selected parameter is the function the user chose
def return_to_menu(selected):
    print(f"You Have Selected \"{selected}\".")
    confirm = input("Continue? [Y/N]: ")
    # Clears terminal
    os.system("cls")

    # Informs user if they enter an invalid input and prompts them again
    while confirm.upper() != "Y" and confirm.upper() != "N":
        print(f"You Have Selected \"{selected}\".")
        print(f"{Colors.LIGHT_RED}Invalid!\nPlease Enter Either Y/N.{Colors.END}")
        confirm = input("Continue? [Y/N]: ")
        os.system("cls")

    # Enters if user chooses not to continue
    if confirm.upper() == "N":
        # Sets cont to False, which will return user to Main Menu
        cont = False
    # Enters if user chooses to continue
    else:
        # Sets cont to True, which will enter the chosen function's loop
        cont = True
    return cont


# valid is used to differentiate whether an invalid input has been entered
valid = True
# bird stores the ASCII art for the bookkeeper bird
bird = r'''
              .-"""""""-.
            .'       __  \_
           /        /  \/  \
          |         \_0/\_0/______        ____________________________________ 
          |:.          .'       oo`\     |      __  __ _____ _   _ _   _      | 
          |:.         /             \    |     |  \/  | ____| \ | | | | |     |
          |' ;        |             |    |     | |\/| |  _| |  \| | | | |     |
          |:..   .     \_______     |    |     | |  | | |___| |\  | |_| |     |
          |::.|'     ,  \,_____\   /     |     |_|  |_|_____|_| \_|\___/      |
          |:::.; ' | .  '|      )_/      |____________________________________|
          |::; | | ; ; | | 
         /::::.|-| |_|-|, \
'''
# title stores the ASCII art for the title screen in the main menu
title = r'''
╔══════════════════════════════════════════════╗
║                  __  ____   __               ║
║                 |  \/  \ \ / /               ║
║                 | |\/| |\ V /                ║
║                 | |  | | | |                 ║
║            ____ |_|__|_|_|_| _  __           ║
║           | __ ) / _ \ / _ \| |/ /           ║
║           |  _ \| | | | | | | ' /            ║
║           | |_) | |_| | |_| | . \            ║
║      _    |____/ \___/ \___/|_|\_\           ║
║     | |   (_) |__  _ __ __ _ _ __ _   _      ║
║     | |   | | '_ \| '__/ _` | '__| | | |     ║
║     | |___| | |_) | | | (_| | |  | |_| |     ║
║     |_____|_|_.__/|_|  \__,_|_|   \__, |     ║
║                                   |___/      ║
╚══════════════════════════════════════════════╝    
                Press Enter  
'''

print(title)
# Passes when user enters anything
input()

with open("books_22045579.txt") as file:
    contents = file.readlines()

""" (Main Menu) Main Loop """
while True:
    # Clears terminal
    os.system("cls")
    try:
        print(bird, end="")
        # print_name_box (name) prints the name box with the name for the bookkeeper bird
        # print_msg_box(msg) prints the options the user may choose from in a message box
        print_name_box("Big Black Hawk")
        print_msg_box(" Welcome to the Main Menu!\n Here are the available Functions:\n     1. Display All Books\n"
                      "     2. Search for Book\n     3. Add Book\n     4. Edit Book\n     5. Delete Book\n"
                      "     6. Exit Program\n Please Enter a Number Between 1 - 6."
                      "                                      ")
        # Prompts user to choose a function from the options listed (choice stores the input)
        # int () is used to raise ValueError if user does not enter a number
        choice = int(input("Choose Function: "))
        os.system("cls")

        # Raises AssertionError if user input is not between 1 - 6
        assert 1 <= choice <= 6

    # Enters if an error is raised
    # Executes its body contents
    # Returns to the start of Main Loop
    except (AssertionError, ValueError):
        os.system("cls")
        # Sets valid to False because an invalid input was entered
        valid = False

    # Enters if no error is raised
    else:
        # Matches the input for choice to the corresponding case
        match choice:
            # Enters if user chooses Display All Books
            case 1:
                display_all_books()
            # Enters if user chooses Search for Books
            case 2:
                search_for_book()
            # Enters if user chooses Add Book
            case 3:
                add_book()
            # Enters if user chooses Edit Book
            case 4:
                edit_book()
            # Enters if user chooses Delete Book
            case 5:
                delete_book()
            # Enters if user chooses Exit Program
            case 6:
                """ Loop - 1 (Nested in Main Loop) """
                ''' Asks user if they want to save the changes they have made to the text file '''
                while True:
                    # Prompts user to choose whether to save changes or not (save stores input)
                    save = input("Save All Changes? (Y/N): ")
                    os.system("cls")
                    # Enters if user does not enter Y or N
                    # .upper() is used to accept y/Y and n/N
                    if save.upper() != "Y" and save.upper() != "N":
                        print(f"{Colors.LIGHT_RED}Invalid!\nPlease Enter Either Y/N.{Colors.END}")
                        # Returns to the start of Loop - 1
                        continue
                    else:
                        # Exits Loop - 1 (Back to Main Loop)
                        break

                # Enters if user chooses to save changes
                if save.upper() == "Y":
                    print(f"{Colors.LIGHT_GREEN}Changes Saved.{Colors.END}")
                    # Writes the changed contents to books_StudentID.txt
                    with open("books_StudentID.txt", "w") as file:
                        file.write(''.join(str(i) for i in contents))
                    # Exits Main Loop
                    break
                # Enters if user chooses not to save changes
                else:
                    # Exits Main Loop
                    break

""" Program Stops """
