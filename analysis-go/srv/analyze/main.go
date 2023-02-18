package main

import (
	"fmt"
	"os"
	"bufio"
	"log"
	"strings"
	"sort"
	"encoding/json"
)

func loadFile(filename string) []string {
	// loadFile() is utilized for loading and returnign a slice of all the lines in the specified {filename}.
	filePath := fmt.Sprintf("./files/%s", filename)
	file, err := os.Open(filePath)
	if err != nil {
		log.Fatalf("Failed to open %s: %s", filePath, err)
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	if scanner.Err() != nil {
		log.Fatalf("Failed to read %s: %s", filePath, err)
	}

	return lines
}

func cleanLine(line *string) {
	// cleanLine() is utilized for replacing hyphens and the possesive "'s" with a space 
	// also replacing punctuation below with nothing 
	// ALL in the specified {line}.
	// *line = strings.ReplaceAll(strings.ReplaceAll(strings.ReplaceAll(*line, "-", " "), "—", " "), "’s", " ")
	*line = strings.ReplaceAll(*line, "-", " ")
	*line = strings.ReplaceAll(*line, "—", " ")
	*line = strings.ReplaceAll(*line, "’s", " ")
	

	for _, punc := range `!@#$%^&*()=+_~[]\|;:'` + "`" + `",./<>?“”` {
		*line = strings.ReplaceAll(*line, string(punc), "")
	}
}

func wordInStopWords(word string, stopWords []string) bool {
	for _, stopWord := range stopWords {
		if stopWord == word {
			return true
		}
	}
	return false
}

func main() {
	/*
	count_top_100_frequent_words() is the true logic behind finding the 100 most frequent words in Moby Dick.
	*/
	occurrences := make(map[string]int)
	stopWords := loadFile("stop-words.txt")
	mobyText := loadFile("mobydick.txt")

	start := false
	for _, line := range mobyText {
		// if we reached this line, this is the end of Moby Dick - thus we're done counting words
		if line == "End of Project Gutenberg’s Moby Dick; or The Whale, by Herman Melville" {
			break
		}

		// cleaning our line of text
		// pass pointer for line to cleanLine, cleanLine will use pointer to update value
		cleanLine(&line)
		line = strings.TrimSpace(strings.ToLower(line))

		// if we passed the start line (end of the pre-writing), we begin counting words
		if start {
			// for each word in the line, if it's not in list of stop_words and it's not ''
            // we'll try to increment the occurrence and catch the KeyError if the word hasn't already been added to the dict,
            // then add it with it's first occurrence of 1
			for _, word := range strings.Split(line, " ") {
				if !wordInStopWords(word, stopWords) && word != "" {
					// NOTE: in GO, if you try to access a key in a map that doesn't exist, the map will return a value of 0
					// in the below example, we're able to take the 0 as _, and fetch the bool as "exists" to then be evaluated in the conditional
					_, exists := occurrences[word]
					if exists {
						occurrences[word] += 1
					} else {
						occurrences[word] = 1
					}
				}
			}
		}

		if line == "start of this project gutenberg ebook moby dick or the whale" {
			start = true
		}
	}

	// creating final sorted solution
	type Occurrences struct {
		Word string
		Count int
	}

	var sortedOccurrences []Occurrences
	for word, count := range occurrences {
		sortedOccurrences = append(sortedOccurrences, Occurrences{word, count})
	}

	sort.Slice(sortedOccurrences, func(i, j int) bool {
		return sortedOccurrences[i].Count > sortedOccurrences[j].Count
	})

	// writing sortedOccurrences to JSON and saving
	occurrencesJson, err := json.Marshal(sortedOccurrences[:100])
	if err != nil {
		fmt.Printf("Failed to write occurrences to json: %s", err)
	}

	err = os.WriteFile("./files/top_100.txt", []byte(string(occurrencesJson)), 0666)
	if err != nil {
		log.Fatalf("Something went wrong writing top 100 occurrences JSON to file: %s", err)
	}
}