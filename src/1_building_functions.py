from typing import List

# PROGRESSION EXAMPLE

#region # ORIGINAL OBTUSE FUNCTION
# =============================================================================
# ORIGINAL OBTUSE FUNCTION
# =============================================================================
# Here is a function that processes text, but it is very hard to understand.
def a(b, c):
    d = c.split()
    e = []
    for f in d:
        g = f.lower()
        if g not in b:
            h = g.strip('.,!?')
            e.append(h)
    i = " ".join(e)
    return i

#endregion

#region # RENAMING
# =============================================================================
# RENAMING
# =============================================================================
# The function is now clearer with descriptive variable/function names.

def remove_stopwords_and_punctuation(ignore_words, text):
    words = text.split()
    filtered_words = []
    for word in words:
        lower_word = word.lower()
        if lower_word not in ignore_words:
            clean_word = lower_word.strip('.,!?')
            filtered_words.append(clean_word)
    cleaned_str = " ".join(filtered_words)
    return cleaned_str

#endregion

#region # ADDING LOTS OF COMMENTS
# =============================================================================
# ADDING LOTS OF COMMENTS
# =============================================================================
# Adding comments to explain each step of the function.
# Some people say that you should not need comments if your code is clear enough, but I disagree.
# worst case senari: your code goes to an expert and they are like "wth this is obvious"
# best case senario: your code goes to a beginner and they are like "why doesn't all code look like this?"
# additionally, tools like github copilot can use comments to help write code. so using them will speed up your coding anyway.

def remove_stopwords_and_punctuation(ignore_words, text):
    # Split the text into individual words
    words = text.split()

    # Initialize an empty list to store filtered words
    filtered_words = []

    # Iterate over each word in the list
    for word in words:
        # Convert the word to lowercase
        lower_word = word.lower()

        # If the word is not in the ignore list, process it
        if lower_word not in ignore_words:
            # Remove punctuation from the word
            clean_word = lower_word.strip('.,!?')
            
            # Add the cleaned word to the filtered list
            filtered_words.append(clean_word)
    
    # Join the filtered words back into a single string
    cleaned_str = " ".join(filtered_words)
    
    # Return the processed text
    return cleaned_str

#endregion

#region # ADDING A DOCSTRING
# =============================================================================
# ADDING A DOCSTRING
# =============================================================================
# Adding a docstring to describe the function's purpose, parameters, and return value.

def remove_stopwords_and_punctuation(ignore_words, text):
    """
    Processes a given text by filtering out specified words and removing punctuation.

    :param ignore_words: A list of words to ignore during processing.
    :param text: The text to be processed as a string.
    :return: A string with the specified words removed and punctuation stripped.
    """
    
    # Split the text into individual words
    words = text.split()

    # Initialize an empty list to store filtered words
    filtered_words = []

    # Iterate over each word in the list
    for word in words:
        # Convert the word to lowercase
        lower_word = word.lower()

        # If the word is not in the ignore list, process it
        if lower_word not in ignore_words:
            # Remove punctuation from the word
            clean_word = lower_word.strip('.,!?')
            
            # Add the cleaned word to the filtered list
            filtered_words.append(clean_word)
    
    # Join the filtered words back into a single string
    cleaned_str = " ".join(filtered_words)
    
    # Return the processed text
    return cleaned_str

#endregion

#region # ADDING TYPING
# =============================================================================
# ADDING TYPING
# =============================================================================
# Adding type annotations to the function for clarity and error prevention.

def remove_stopwords_and_punctuation(ignore_words: List[str], text: str) -> str:
    """
    Processes a given text by filtering out specified words and removing punctuation.

    :param ignore_words: A list of words to ignore during processing.
    :param text: The text to be processed as a string.
    :return: A string with the specified words removed and punctuation stripped.
    """
    
    # Split the text into individual words
    words = text.split()

    # Initialize an empty list to store filtered words
    filtered_words = []

    # Iterate over each word in the list
    for word in words:
        # Convert the word to lowercase
        lower_word = word.lower()

        # If the word is not in the ignore list, process it
        if lower_word not in ignore_words:
            # Remove punctuation from the word
            clean_word = lower_word.strip('.,!?')
            
            # Add the cleaned word to the filtered list
            filtered_words.append(clean_word)
    
    # Join the filtered words back into a single string
    cleaned_str = " ".join(filtered_words)
    
    # Return the processed text
    return cleaned_str

#endregion
