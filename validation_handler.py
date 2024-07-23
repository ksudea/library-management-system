# Validation helper methods for input

import re

def book_title_validate(title):
    match = re.match(r"\b([A-Za-z,0-9. ']{2,})+", title)
    if match != None:
          return True
    return False

#Matches ISBN13 (13 chars that start with 978 or 979) in the following formats:
# XXX-X-XXXX-XXXX-X
# XXX X XXXX XXXX X
# XXXXXXXXXXXXX
def book_ISBN_validate(isbn):
    match = re.match(r"\b(97(8|9){1}){1}[- \s]?[0-9]{1}[- \s]?[0-9]{4}[- \s]?[0-9]{4}[- \s]?[0-9]{1}$", isbn)
    if match != None:
          return True
    return False

#Matches the following formats:
#DD MM YYYY or DD/MM/YYYY or DD-MM-YYYY
#MM DD YYYY or MM/DD/YYYY or MM-DD-YYYY
#or the same, but with 2 digit YY
def book_publication_date_validate(date):
    match = re.match(r"^[0-9]{1,2}[\/\- ]?[0-9]{1,2}[\/\- ]?([0-9]{2}|[0-9]{4})$", date)
    if match != None:
          return True
    return False

#Matches availability = Available or Borrowed
def book_availability_validate(availability):
    match = re.match(r"^(Available|Borrowed)", availability)
    if match != None:
          return True
    return False

#At least 3 chars
def user_id_validate(id):
    match = re.match(r"\b([A-Za-z,0-9. ']{3,})+", id)
    if match != None:
          return True
    return False

#Name validation for user name, author name, and genre name (2 or more valid characters)
def name_validate(name):
    match = re.match(r"\b([A-Z-,a-z. ']{2,})+", name)
    if match != None:
          return True
    return False
