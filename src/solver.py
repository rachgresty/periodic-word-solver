import itertools
import pandas as pd
from src.decompose_word import WordDecomposition


class SolvePeriodicWord():

    def __init__(self, original_input_word, lowercase_input_word, word_df, periodic_df):
        self.original_input_word = original_input_word
        self.lowercase_input_word = lowercase_input_word
        self.word_df = word_df
        self.periodic_df = periodic_df
        self.join_period_and_word_dataframes()


    def join_period_and_word_dataframes(self):
        """
        Join the tables for the word 1 & 2 letters and periodic table elements together to eliminate non-period letters
        """
        self.periodic_letters = self.word_df.merge(self.periodic_df, on='Symbol', how='inner')
        self.periodic_letters = self.periodic_letters['Symbol'].to_list()
        return self.periodic_letters


    def compute_possible_combinations_and_check_for_input(self):
        """
        Get every combination of the letters
        Cap at word length to save space but some elements have 2 characters so won't be exact
        """
        word_length = len(self.original_input_word)

        self.shuffled_words = []

        for x in itertools.permutations(self.periodic_letters, word_length):
            joined_letters = ''.join(x)
            self.shuffled_words.append(joined_letters)

        if not self.shuffled_words:
            response = f"Sorry! {self.original_input_word} cannot be spelt using the periodic table"
        else:
            df = self._convert_to_dataframe()
            response = self._check_combinations_for_input_word(df)

        return response

    def _convert_to_dataframe(self):
        """
        Convert to a dataframe
        """
        self.shuffled_words_df = pd.DataFrame(self.shuffled_words)
        self.shuffled_words_df.columns = ['Symbol']
        return self.shuffled_words_df

    def _check_combinations_for_input_word(self, full_df):
        """
        Check the combined words to see if it's a match for the input word
        """
        if full_df['Symbol'].str.contains(self.lowercase_input_word).any():
            output_message = f"Success! {self.original_input_word} can be spelt using the periodic table"
        else: 
            output_message = f"Sorry! {self.original_input_word} cannot be spelt using the periodic table"

        return output_message