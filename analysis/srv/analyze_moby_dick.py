"""
To perform analysis on Moby Dick by Herman Melville.
"""

import json

def load_file(filename):
    """
    load_file() is utilized for loading and returning a list of all the lines in the specified {filename}.
    """
    with open(f'./files/{filename}') as f:
        lst_lines = list(filter(None, f.read().split('\n')))
    return lst_lines

def clean_line(line):
    """
    clean_line() is utilized for replacing hyphens, the possesive "'s", and the listed punctuation below with a space in the specified {line}.
    """
    line = line.replace('-', ' ').replace('—', ' ').replace('’s', '')
    for punc in """!@#$%^&*()=+_`~[]\|;:'",./<>?“”""":
        line = line.replace(punc, '')
    return line

def count_top_100_frequent_words():
    """
    count_top_100_frequent_words() is the true logic behind finding the 100 most frequent words in Moby Dick.

    Please note: my original solution did not have anything for checking to see if we were truly looking at the story, Moby Dick.
    To resolve this, I added the start / break statement to find where the text is Moby Dick and not the pre/post writing.
    See https://github.com/Millerlm012/MobyDick/commit/08247595a7fa8c801308072d1c0604bd265c737b for additional information.
    """
    # intializing data structure and loading files to list of lines
    occurrences = {}
    stop_words = load_file('stop-words.txt')
    moby_text = load_file('mobydick.txt')

    start = False
    for line in moby_text:
        # if we reached this line, this is the end of Moby Dick - thus we're done counting words
        if line == 'End of Project Gutenberg’s Moby Dick; or The Whale, by Herman Melville':
            break

        # cleaning our line of text
        line = clean_line(line)
        line = line.strip().lower()

        # if we passed the start line (end of the pre-writing), we begin counting words
        if start:
            # for each word in the line, if it's not in list of stop_words and it's not ''
            # we'll try to increment the occurrence and catch the KeyError if the word hasn't already been added to the dict,
            # then add it with it's first occurrence of 1
            for word in line.split(' '):
                if word not in stop_words and word != '':
                    try:
                        occurrences[word] += 1
                    except KeyError:
                        occurrences[word] = 1

        if line == 'start of this project gutenberg ebook moby dick or the whale':
            start = True
    
    # logic for sorting our occurrences from greatest to least:
    # accomplished via adding a tuple of word and # of occurrences to a list, then using python built in sort()
    occurrences_sorted = []
    for key, value in occurrences.items():
        occurrences_sorted.append((value, key))
    occurrences_sorted.sort(reverse=True)

    # finally, we write the json dump of the top 100 results of our occurrences to top_100.txt for our API to utilize
    with open('./files/top_100.txt', 'w') as f:
        f.write(json.dumps(occurrences_sorted[:100]))


if __name__ == '__main__':
    count_top_100_frequent_words()