# for database
# import pandas as pd

# teacher_entity = 'galib'

# df = pd.read_csv('./data/teacher_info.csv')

# def get_teacher_info(teacher_entity):
#     teacher_entity = teacher_entity.split(' ')[-1]
#     for teacher in df['name']:
#         if teacher_entity in teacher:
#             info = df[df['name'] == teacher]
#             dept = info['dept'].values[0]
#             name = info['name'].values[0]
#             desig = info['designation'].values[0]
#             tele = info['telephone'].values[0] if not info['telephone'].isna().all() else None
#             email = info['email'].values[0] if not info['email'].isna().all() else None

#             return (dept, name, desig, tele, email)
        
# def get_dept_overview(dept_entity):
#     df = pd.read_csv('dept-overview.csv')
#     for dept in df['dept']:
#         if dept == dept_entity:
#             info = df[df['dept'] == dept]
#             overview = info["overview"].values[0]
#             return (dept, overview)

# get_dept_overview('cse')