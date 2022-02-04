import pandas as pd
from src.decompose_word import WordDecomposition
from src.periodic_elements import PeriodElements
from src.solver import SolvePeriodicWord
from pandas.testing import assert_frame_equal


example_original_successful_word = "Lion"
example_lower_successful_word = "lion"

example_original_unsuccessful_word = "Tiger"
example_lower_unsuccessful_word = "tiger"

dummy_successful_word_df = pd.DataFrame({"Symbol":["l","i","o","n","li","io","on"]})
dummy_unsuccessful_word_df = pd.DataFrame({"Symbol":["t","i","g","e","r","ti","ig","ge","er"]})

dummy_periodic_df = pd.DataFrame({"Symbol":["h","he","li","be","b","c","n","o","f","ne","na","mg","al","si","p","s","cl","ar",
                                            "k","ca","sc","ti","v","cr","mn","fe","co","ni","cu","zn","ga","ge","as","se","br",
                                            "kr","rb","sr","y","zr","nb","mo","tc","ru","rh","pd","ag","cd","in","sn","sb","te",
                                            "i","xe","cs","ba","la","ce","pr","nd","pm","sm","eu","gd","tb","dy","ho","er","tm",
                                            "yb","lu","hf","ta","w","re","os","ir","pt","au","hg","tl","pb","bi","po","at","rn",
                                            "fr","ra","ac","th","pa","u","np","pu","am","cm","bk","cf","es","fm","md","no","lr",
                                            "rf","db","sg","bh","hs","mt","ds","rg","cn","nh","fl","mc","lv","ts","og"]})

def test_solver_successful():
    solver_class = SolvePeriodicWord(example_original_successful_word, example_lower_successful_word, dummy_successful_word_df, dummy_periodic_df)
    output_message = solver_class.compute_possible_combinations_and_check_for_input()
    success_message = f"Success! {example_original_successful_word} can be spelt using the periodic table"
    assert output_message == success_message

def test_solver_unsuccessful():
    solver_class = SolvePeriodicWord(example_original_unsuccessful_word, example_lower_unsuccessful_word, dummy_unsuccessful_word_df, dummy_periodic_df)
    output_message = solver_class.compute_possible_combinations_and_check_for_input()
    unsuccessful_message = f"Sorry! {example_original_unsuccessful_word} cannot be spelt using the periodic table"
    assert output_message == unsuccessful_message

def test_word_decomposed_correctly():
    word_elements_class = WordDecomposition(example_lower_successful_word)
    word_elements_df = word_elements_class.combine_all_word_elements()
    assert_frame_equal (dummy_successful_word_df, word_elements_df)

def test_periodic_table_read_correctly():
    periodic_elements_class = PeriodElements()
    periodic_elements_df = periodic_elements_class.read_periodic_elements_from_csv()
    assert_frame_equal (periodic_elements_df, dummy_periodic_df)