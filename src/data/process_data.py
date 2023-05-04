import pandas as pd

df_csv = pd.read_csv("../../data/raw/students_grades.csv",index_col=0)

df_excel = pd.read_excel('../../data/raw/students_school.xlsx', index_col=0)

df_txt = pd.read_csv('../../data/raw/students.txt', delimiter='\;')

"""
print("CSV : -----")
print(df_csv.head())
print("EXCEL : -----")
print(df_excel.head())
print("TXT : -----")
print(df_txt.head())"""

merged_df = pd.merge(df_csv, df_excel, on='student_id', how='outer')
merged_df = pd.merge(merged_df, df_txt, on='student_id', how='outer')

print(merged_df.head())

merged_df['final_grade'] = merged_df[['G1', 'G2', 'G3']].mean(axis=1)

print(merged_df.head())

processed_df = merged_df.drop(['G1', 'G2', 'G3'],axis=1)

print(processed_df.head())

processed_df.to_csv('../../data/processed/current_data.csv', index=False)



