import pandas as pd
from src.decompose_word import WordDecomposition
from src.periodic_elements import PeriodElements
from src.solver import SolvePeriodicWord
from pandas.testing import assert_frame_equal


example_original_successful_word = "Lion"
example_lower_successful_word = "lion"

example_original_unsuccessful_word = "Tiger"
example_lower_unsuccessful_word = "tiger"


def test_solver_successful():
    word_elements_class = WordDecomposition(example_lower_successful_word)
    word_elements_df = word_elements_class.combine_all_word_elements()

    periodic_elements_class = PeriodElements()
    periodic_elements_df = periodic_elements_class.read_periodic_elements_from_csv()

    solver_class = SolvePeriodicWord(example_original_successful_word, example_lower_successful_word, word_elements_df, periodic_elements_df)
    output_message = solver_class.compute_possible_combinations_and_check_for_input()
    success_message = f"Success! {example_original_successful_word} can be spelt using the periodic table"
    assert output_message == success_message


def test_solver_unsuccessful():
    word_elements_class = WordDecomposition(example_original_unsuccessful_word)
    word_elements_df = word_elements_class.combine_all_word_elements()

    periodic_elements_class = PeriodElements()
    periodic_elements_df = periodic_elements_class.read_periodic_elements_from_csv()

    solver_class = SolvePeriodicWord(example_original_unsuccessful_word, example_lower_unsuccessful_word, word_elements_df, periodic_elements_df)
    output_message = solver_class.compute_possible_combinations_and_check_for_input()
    unsuccessful_message = f"Sorry! {example_original_unsuccessful_word} cannot be spelt using the periodic table"
    assert output_message == unsuccessful_message