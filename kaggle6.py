#1

"""
There is a saying that "Data scientists spend 80% of their time cleaning data,
and 20% of their time complaining about cleaning data." Let's see if you can
write a function to help clean US zip code data. Given a string, it should
return whether or not that string represents a valid zip code. For our purposes,
a valid zip code is any string consisting of exactly 5 digits.
"""

def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    return zip_code.isdigit() and len(zip_code) == 5
# self note: conditional >>> boolean !!


#2
"""
A researcher has gathered thousands of news articles. But she wants to focus he
attention on articles including a specific word. Complete the function below to
help her filter her list of articles.

Your function should meet the following criteria:

Do not include documents where the keyword string shows up only as a part of a
larger word. For example, if she were looking for the keyword “closed”, you
would not include the string “enclosed.”
She does not want you to distinguish upper case from lower case letters. So the
 phrase “Closed the case.” would be included when the keyword is “closed”
Do not let periods or commas affect what is matched. “It is closed.” would be
 included when the keyword is “closed”. But you can assume there are no other
 types of punctuation.
"""

def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword.
    Returns list of the index values into the original list for all documents
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car",
    "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    indlist = []
    for phrase in doc_list:
        for word in phrase.split():
            onlyword = word.strip(".,?")
            if onlyword.lower() == keyword.lower():
                indlist.append(doc_list.index(phrase))
                break

    return indlist
    print(indlist)

"""
Kaggle: uses the function enumerate & list comprehension

def word_search(documents, keyword):
    indices = []
    for i, doc in enumerate(documents):
        tokens = doc.split()
        normalized = [token.rstrip('.,').lower() for token in tokens]
        if keyword.lower() in normalized:
            indices.append(i)
    return indices
"""



#3
"""
Now the researcher wants to supply multiple keywords to search for.
Complete the function below to help her.
"""

def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    multi_word_indices = {}
    for key in keywords:
        indices = word_search(doc_list, key)
        multi_word_indices[key] = indices
    return multi_word_indices
