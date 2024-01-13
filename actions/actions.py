from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

#######################################################################################################

# for database
import pandas as pd

def get_teacher_info(teacher_entity):
    df = pd.read_csv('./actions/teacher_info.csv')
    teacher_entity = teacher_entity.split(' ')[-1]
    for teacher in df['name']:
        if teacher_entity in teacher:
            info = df[df['name'] == teacher]
            dept = info['dept'].values[0]
            name = info['name'].values[0]
            desig = info['designation'].values[0]
            tele = info['telephone'].values[0] if not info['telephone'].isna().all() else None
            email = info['email'].values[0] if not info['email'].isna().all() else None

            return (dept, name, desig, tele, email)
        
def get_dept_overview(dept_entity):
    df = pd.read_csv('./actions/dept_overview.csv')
    for dept in df['dept']:
        if dept == dept_entity:
            info = df[df['dept'] == dept]
            overview = info["overview"].values[0]
            return (dept, overview)
        
#######################################################################################################




class GetDeptInfo(Action):

    def name(self) -> Text:
        return "action_get_dept_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dept_entity = next(tracker.get_latest_entity_values('dept'), None)

        if not dept_entity:
            dispatcher.utter_message(f"Sorry I could not detect the department name.")
        else:
            try:
                dept, overview = get_dept_overview(dept_entity)
                dispatcher.utter_message(f"About {dept.upper()}: {overview}")
            except:
                dispatcher.utter_message(f"I can't tell you about {dept_entity.upper()} for now. I will be able to tell you once I have all the data.")



class GetTeacherInfo(Action):

    def name(self) -> Text:
        return "action_get_teacher_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        teacher_name = next(tracker.get_latest_entity_values('teacher_name'), None)

        if not teacher_name:
            dispatcher.utter_message(f"Sorry I could not detect the teacher name.")
        else:  
            dept, name, desig, tele, email = get_teacher_info(teacher_name)
            if desig[0] == 'a' or desig[0] == 'A': article = 'an'
            else: article = 'a'
            dispatcher.utter_message(f"{name.title()} is {article} {desig} of {dept.upper()}. You can contact him/her at {tele} or {email}.")

        

