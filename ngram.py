'''
Markov n-gram demo program.
by Paul Ebreo

Inspired by Brit Cruise's Markov videos:
https://www.khanacademy.org/math/applied-math/informationtheory/moderninfotheory/v/a-mathematical-theory-of-communication
'''
from collections import Counter
from random import choice
import re


class Cup:
    """A class defining a cup that will hold the words that we will pull out"""
    def __init__(self):
        self.next_word = Counter() # will keep track of how many times a word appears in a cup

    def add_next_word(self,word):
        """Used to add words to the cup and keep track of how many times we see it"""
        self.next_word[word] += 1

class NGRAM:

    @staticmethod
    def make_cups(order,string):
        """Get a string of input text and make all the unique cups with the different words in it"""
        cups = dict()
        words = re.findall(r"([\w]+)",string)
        token = []
        next_word = ''
        for i in range(len(words)-order):
            token = []
            next_word = words[i+order]
            for j in range(order):
                token.append(words[i+j])
            # Create a cup if we've never seen this token before
            if not cups.has_key(tuple(token)):
                cups[tuple(token)] = Cup()
                cups[tuple(token)].add_next_word(next_word)
            else:
                cups[tuple(token)].add_next_word(next_word)
        return cups


    @staticmethod
    def print_cups(cups):
        """You can use this to see what cups there are and the words inside of it """
        for token in cups.keys():
            print "key %s : nextword %s" %(token,cups[token].next_word)

    @staticmethod
    def topword(n,cup):
        """ A function that picks the top words in a cup. I realized I could've just randomly picked from a list of words
            but instead a made a Counter() object of words to keep track of them
        """
        # reverse sort based on values
        temp = list(reversed(sorted(cup.next_word,key=cup.next_word.get)))
        if len(temp[:n]) > 0:
            return choice(temp[:n]) # random element from the temp list
        else:
            return ""

    @staticmethod
    def generate(order, filename, number_of_words):
        """ Generate words based on a text file
            Usage: Ngram.generate_from_file(order=2,'sample-sal.txt')
        """
        # put file in one big string
        with open(filename,'r') as f:
            string = f.read()

        string = re.sub('[,\.?"-\'!:;]','',string)

        cups = {}
        cups = NGRAM.make_cups(order, string)

        first_token = choice(cups.keys()) # random first token
        this_token = first_token
        generated_words = []
        generated_words += list(this_token)
        next_word = "" # first next word is blank

        for i in range(number_of_words):
            next_word = NGRAM.topword(1, cups[this_token])
            temp = list(this_token)
            temp.pop(0) # remove first word in token
            temp.append(next_word) # add new word to the token
            next_token = tuple(temp)
            this_token = next_token
            generated_words += [next_word]

        print ' '.join(generated_words)

    @staticmethod
    def generate_from_string(order, string, number_of_words):
        """Generate words based on a string"""
        string = re.sub('[,\.?"-\'!:;]','',string)
        cups = {}
        cups = NGRAM.make_cups(order, string)
        first_token = choice(cups.keys()) # random first token
        this_token = first_token
        generated_words = []
        generated_words += list(this_token)
        next_word = "" # first next_word is blank

        for i in range(1,number_of_words):
            # if the name of the token exists
            if cups.has_key(this_token):
                next_word = NGRAM.topword(2,cups[this_token])
            else:
                this_token = choice(cups.keys()) # random token
                next_word = NGRAM.topword(2,cups[this_token])

            temp = list(this_token)
            temp.pop(0) # remove first word in token
            temp.append(next_word) # add new word to the end of the token
            next_token = tuple(temp)
            this_token = next_token
            generated_words += [next_word]

        print ' '.join(generated_words)


if __name__ == "__main__":
    print "SAMPLE OUTPUT FROM FILE:\n"
    NGRAM.generate(3,'sample-hamlet.txt', 50)

    print "\nSAMPLE OUTPUT FROM STRING:\n"
    str = "Let's say we have the equation 7 times x is equal to 14. Now before even trying to solve this equation, what I want to do is think a little bit about what this actually means. 7x equals 14, this is the exact same thing as saying 7 times x - let me write it this way -- 7 times x -- we'll do the x in orange again -- 7 times x is equal to 14. Now you might be able to do this in your head. You could literally go through the 7 times table. You say well 7 times 1 is equal to 7, so that won't work. 7 times 2 is equal to 14, so 2 works here. So you would immediately be able to solve it. You would immediately, just by trying different numbers out, say hey, that's going to be a 2. But what we're going to do in this video is to think about how to solve this systematically. Because what we're going to find is as these equations get more and more complicated, you're not going to be able to just think about it and do it in your head. So it's really important that one, you understand how to manipulate these equations, but even more important to understand what they actually represent. This literally just says 7 times x is equal to 14. In algebra we don't write the times there. When you write two numbers next to each other or a number next"
    NGRAM.generate_from_string(2, str, 50)
