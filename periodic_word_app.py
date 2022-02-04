import streamlit as st
from PIL import Image
from src.decompose_word import WordDecomposition
from src.periodic_elements import PeriodElements
from src.solver import SolvePeriodicWord


# Title of the main page
image = Image.open("app_components/periodic_word_solver_logo.png")
st.image(image)

# User Input Word
with st.form(key='initial_word'):
	text_input = st.text_input(label="Enter Your Word Here", value="Check")
	submit_button = st.form_submit_button(label='Submit')

lower_case_input_word = text_input.lower()

# Model
word_elements_class = WordDecomposition(lower_case_input_word)
word_elements_df = word_elements_class.combine_all_word_elements()

periodic_elements_class = PeriodElements()
periodic_elements_df = periodic_elements_class.read_periodic_elements_from_csv()

solver_class = SolvePeriodicWord(text_input, lower_case_input_word, word_elements_df, periodic_elements_df)
solution = solver_class.compute_possible_combinations_and_check_for_input()
st.success(solution)