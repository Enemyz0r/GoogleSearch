import webbrowser

query = input("Please enter your search input: ")

base_url = "http://www.google.com/?#q="

final_url = base_url + query
webbrowser.open(final_url)
