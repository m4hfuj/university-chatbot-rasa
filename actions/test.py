# for database
import pandas as pd

teacher_entity = 'galib'
teacher_entity = teacher_entity.split(' ')[-1]
print(teacher_entity)

# df = pd.read_csv('./data/teacher_info.csv')

# for teacher in df['name']:
#     if teacher_entity in teacher:
#         info = df[df['name'] == teacher]
#         dept = info['dept'].values[0]
#         name = info['name'].values[0]
#         tele = info['telephone'].values[0] if not info['telephone'].isna().all() else None
#         email = info['email'].values[0] if not info['email'].isna().all() else None

#         print(dept, name, tele, email)