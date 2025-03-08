# Text Analysis Tool

## Description
This Python program analyzes user input to extract key text properties, such as vowel count, unique words, and the three longest words. Users are prompted to enter a detailed sentence (minimum 10 words), and the script processes the input accordingly.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Functions](#functions)
- [Requirements](#requirements)
- [License](#license)

## Features
- Ensures user input contains at least 10 words.
- Counts and displays vowels in the sentence.
- Identifies unique words (case insensitive).
- Extracts the three longest words and their character counts.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/text-analysis-tool.git
   ```
2. Navigate to the project directory:
   ```sh
   cd text-analysis-tool
   ```
3. Ensure Python 3.x is installed.

## Usage
1. Run the script:
   ```sh
   python text_analysis.py
   ```
2. Enter a detailed response (minimum 10 words).
3. The script will analyze the text and display the following:
   - Vowel count
   - List of unique words
   - The three longest words

## Example
```sh
Hello there, please tell me how your day has been (more than 10 words):
I had an amazing day at the park where I enjoyed nature and relaxed.

You said: I had an amazing day at the park where I enjoyed nature and relaxed.
Thanks for sharing! You used 13 words.

The total amount of vowels in your sentence is 20.
The vowels in your sentence: ['a', 'e', 'i', 'o', 'u']

The unique words used in your sentence are: ['i', 'had', 'an', 'amazing', 'day', 'at', 'the', 'park', 'where', 'enjoyed', 'nature', 'and', 'relaxed']

The 3 largest words in your sentence are ['amazing'] (7 characters), ['relaxed'] (7 characters), and ['enjoyed'] (7 characters).

Take care. Adios!
```

## Functions
- **`userPrompt()`**: Prompts and validates user input.
- **`vowelCounter()`**: Counts and displays vowels.
- **`uniqueWords()`**: Extracts unique words from the input.
- **`charOrder()`**: Identifies the three longest words.

## Requirements
- Python 3.x

## License
This project is licensed under the MIT License.
