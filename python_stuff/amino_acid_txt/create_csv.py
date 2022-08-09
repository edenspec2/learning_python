import pandas as pd
import os
f=open(r'C:\Users\עדן\Documents\GitHub\learning_python\project\function_tests\A_THR_13_5Angs_noHOH.xyz')
lines=f.readlines()
df=pd.DataFrame(lines)
print(df)
os.makedirs('C:\Users\עדן\Documents\GitHub\learning_python\project\function_tests', exist_ok=True)  
df.to_csv('C:\Users\עדן\Documents\GitHub\learning_python\project\function_tests/out.csv')
f.close()
