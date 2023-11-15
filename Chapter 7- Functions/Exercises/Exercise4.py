#Summarize the shirt that's going to be made
def shirt(size='large', message='I love Python!'):
    print("I'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

shirt()
shirt(size='medium')
shirt('small', 'codeing is fun.')