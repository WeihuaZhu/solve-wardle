# solve-wordle

The popular puzzle game Wordle https://www.powerlanguage.co.uk/wordle/ is developed by Josh Wardle (https://twitter.com/powerlanguish?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor)
This is a fun puzzle!
This repo is for my thoughts and approaches on figuring out an optimal strategy for solving daily wordle challenge within 6 tries.
The end result would also contain some stats on mean, variance and distribution of the number of guesses needed for all possible words as answer.

## Problem Statement:

The popular puzzle game Wordle [https://www.powerlanguage.co.uk/wordle/](https://www.powerlanguage.co.uk/wordle/) developed by [Josh Wardle](https://twitter.com/powerlanguish?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor) got viral on the internet and among my friends and colleagues. So my initial thought is that this game is very similar to hangman, and there should be an optimal strategy to solve it (at least statistically, meaning with an optimal strategy, it tries to minimize the expeceted value and variance of the number of tries to get the answer with 100% probability.)

## Brianstorm:

- starting with vowels should be a good start: the first guess can be a word with as many vowels as possible (or ideally the combination of the most frequent 5 letters). e.g. adieu is good a starting word
- even though we got an evidence that a letter is green/yellow, meaning it is part of the word. There is still a trade off for the decision of the next guess:
  - immediately narrow down the possible words using the evidence, like if e is in the middle, only guessing words like green, cream, etc.
  - vs. ignore the current evidence, this open up spaces for getting more information in the next guess, i.e., to see if any of the 5 new letters are in the word or not, which seems like a good long-term strategy. Only narrow down when we got enough info on which letters are in the word, and then form combinations.

## Strategy Input/Output definition:

The strategy should work like a blackbox, given an input of current evidence (a dictionary with key: letter, value: one of 3 colors: green with position x / yellow with position x / gray), the strategy should output a word for next guess(str).

## Ideas

### Idea 1 - Narrow down the sub-branches as evenly as possible, inspired by binary search

My initial thought on this problem is if each guess can tell us information for the next branch with ruling out 50% of the possible words each time, 6 guess can only get us to 64 words, but we have much more words than that. Also a good news is for each guess we have much more information than cutting possible choices by half. Like guessing "vowel-rich" word like "adieu", with either each letter is in/out of the word, we can have 32 branches, and the possibilities should be as close as each other. This is why guessing letter like "z" for the first guess doesn't make sense, yes it can narrow down pretty quickly if "z" is in the word, but if it is in the word, which is 99% of the case, the guess of this letter is wasted.
