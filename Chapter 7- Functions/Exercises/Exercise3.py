#Summarize the shirt that's going to be made
def shirt(size, message):
    print("I'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')
shirt('large', 'I love Python!')
shirt(message="Readability counts.", size='medium')