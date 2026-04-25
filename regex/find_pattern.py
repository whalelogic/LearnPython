import re

def find_pattern(pattern, text):
    """
    This function takes a regex pattern and a text string, and returns a list of all matches of the pattern in the text.
    
    :param pattern: A string representing the regex pattern to search for.
    :param text: A string in which to search for the pattern.
    :return: A list of all matches of the pattern in the text.
    """
    matches = re.findall(pattern, text)
    return matches



# Example usage:

if __name__ == "__main__":
    text = "The rain in Spain stays mainly in the plain."
    pattern = r'\b\w+ain\b'  # This pattern matches words that end with 'ain'
    matches = find_pattern(pattern, text)
    print(matches)  # Output: ['rain', 'Spain', 'plain']
