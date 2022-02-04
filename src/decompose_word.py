import pandas as pd

class WordDecomposition():

    def __init__(self, input_word):
        """
        Breaks down the input word into single letters and pairs of letters

            Args: 
                "input_word": String containing the users input word
        """
        self.input_word = input_word
        self.word_to_letters()
        self.word_to_pairs_of_letters()

    def word_to_letters(self):
        """
        Breaks the word down into single letters
        """
        self.one_letter = list(self.input_word)
        return self.one_letter
        
    def word_to_pairs_of_letters(self):
        """
        Breaks the word down into pairs of letters
        """
        self.two_letter=[]
        self.two_letter.extend([''.join(t) for t in zip(self.input_word, self.input_word[1:])])
        return self.two_letter

    def combine_all_word_elements(self):
        """
        Combines the single and paired letters into a dataframe
        """
        self.word_elements = pd.DataFrame(self.one_letter + self.two_letter)
        self.word_elements.columns = ['Symbol']
        self.word_elements = pd.DataFrame(self.word_elements['Symbol'].str.lower())
        return self.word_elements