import pandas as pd

class PeriodElements():

    def __init__(self):
        pass

    def read_periodic_elements_from_csv(self):
        """
        Read in data for period elements and take the symbols only
        """
        elements = pd.read_csv('./data/periodic_table_elements.csv')
        self.periodic_elements = pd.DataFrame(elements['Symbol'].str.lower())
        return self.periodic_elements

