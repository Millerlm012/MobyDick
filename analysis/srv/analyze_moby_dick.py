"""
To performance analysis on Moby Dick by Herman Melville.
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
    line = line.replace('-', ' ').replace('—', ' ').replace('’s', ' ')
    for punc in """!@#$%^&*()=+_`~[]\|;:'",./<>?“”""":
        line = line.replace(punc, '')
    return line

def count_top_100_frequent_words():
    occurrences = {}
    stop_words = load_file('stop-words.txt')
    moby_text = load_file('mobydick.txt')

    for line in moby_text:
        line = clean_line(line)
        line = line.strip().lower()

        for word in line.split(' '):
            if word not in stop_words and word != '':
                try:
                    occurrences[word] += 1
                except KeyError:
                    occurrences[word] = 1
    
    occurrences_sorted = []
    for key, value in occurrences.items():
        occurrences_sorted.append((value, key))
    occurrences_sorted.sort(reverse=True)

    with open('./files/top_100.txt', 'w') as f:
        f.write(json.dumps(occurrences_sorted[:100]))


if __name__ == '__main__':
    count_top_100_frequent_words()