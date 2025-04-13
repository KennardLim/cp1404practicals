from wikipedia import *
from wikipedia import DisambiguationError, PageError

title = input("Enter page title: ")
while title != "":
    try:
        print(page(title, auto_suggest=False).title)
        print(summary(title, auto_suggest=False))
    except DisambiguationError:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(search(title))
    except PageError:
        print(f"Page id \"{title}\" does not match any pages. Try another id!")
    title = input("\nEnter page title: ")
print("Thank you.")