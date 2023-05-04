import pandas as pd

df_csv = pd.read_csv("../../data/raw/students_grades.csv",index_col=0)

df_excel = pd.read_excel('../../data/raw/students_school.xlsx', index_col=0)

df_txt = pd.read_csv('../../data/raw/students.txt', delimiter='\;')

print("CSV : -----")
print(df_csv.head())
print("EXCEL : -----")
print(df_excel.head())
print("TXT : -----")
print(df_txt.head())