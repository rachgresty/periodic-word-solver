# periodic-word-solver
Identifies whether an input word can be spelt using the periodic table symbols.

To run the streamlit app locally run:
```
streamlit run periodic_word_app.py
```

Otherwise this app can be visited at:
https://share.streamlit.io/rachgresty/periodic-word-solver/main/periodic_word_app.py


## src
There are 3 elements to this periodic word solver model:
1. decompose_word.py: this class takes the input word, converts it to lowercase and splits this into single and pairs of letters in line with the character limits within the periodic table.
2. periodic_elements.py: this class reads in the periodic table elements from a csv file, converts them to lowercase and stores this as a dataframe.
3. solver.py: takes the decomposed word dataframe and joins to the periodic elements dataframe to identify letters or pairs that are in both. Then this iterates through every combination of these to find whether this matches the input word.


## tests
- unit tests: these test the individual functions of the classes to ensure they are robust to further model developments
- end to end tests: ensures that all elements of the model work as expected.


## streamlit app
The front end for this model is a streamlit app that contains a logo and a text input box where the user can add their word and it returns a message confirming whether this word can successfully be built from the periodic table or not.


## environments
Uses poetry environments to ensure reproducability across machines.