def count_text(string):
    dictionary = {}
    density = {}
    dictionary['total_words'] = len(string.rsplit())
    dictionary['punctuations'] = string.count(",") + string.count("!") + string.count(".")
    dictionary['spaces'] = string.count(" ")
    
    if string[-1] == ".":
        dictionary['punctuations']+=1


    punc = '''!()-[]{};:'“”"\,<>./?@#$%^&*_~'''
 

    for ele in string:
        if ele in punc:
            string = string.replace(ele, "")

    words_ = string.rsplit()

    dictionary['upper_char'] = sum(1 for c in string if c.isupper())
    dictionary['lowercase_char'] = sum(1 for c in string if c.islower())

    total_words = len(words_)



    for word in words_:
        if word not in density:
            density[word] = {"counter":1,"percentange":""}
        else:
            density[word]["counter"] +=1


    for item in density:
        density[item]["percentage"] = int((density[item]["counter"]*100)//total_words )
    
    dictionary["words"] = density

    return dictionary


count_text("model, cascade on any user interface.")


# def count(string):

