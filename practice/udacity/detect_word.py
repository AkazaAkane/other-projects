import urllib.request

def read_text():
    quotes = open("/Users/yuhaochen/Desktop/movie_quotes.txt")
    contents = quotes.read()
    print(contents)
    quotes.close()
    result = str(check_profanity(contents))
    if "true" in result:
        print("It is a curse word")
    else:
        print("It is not a curse word")

def check_profanity(text_to_check):
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+ text_to_check)
    output = connection.read()
    return(output)
    connection.close()

read_text()
