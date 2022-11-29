# WordleSolver
## General Motivation
During Covid, my family, like many others, got very into doing the daily Wordle and comparing (read: competing over) how many guesses it took us to get to the correct word. Having a bit of a competative streak, I took it as an opportunity to practice some Python and create a potential word generator. Needless to say, it helped my scores considerably to have a list of possibilities in front of me.

## Program Overview
By feeding in the known parts of a word (using '-' to represent unknown values, for example "p--ch"), a list of blacklisted letters (ones the word is know not to contain), a dictionary mapping letters the word contains to indexes that have been eliminated, and a dictionary of 5-letter words. If desired, it is also possible to stipulate whether the possible words should be written to a "guesses" file, or printed to the console.
