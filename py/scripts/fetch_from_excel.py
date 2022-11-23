import pandas as pd

read_file = pd.read_excel(r'C:\Users\<myusername>\Documents\<myxlsxfile.xlsx>')

read_file.to_csv(r'C:\Users\<myusername>\Documents\<mycsvfile.csv>', index = None, header = True)
