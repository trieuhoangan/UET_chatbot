# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
class PointFormActino(Action):
    def name(self) -> Text:
        return "point_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["faculty", "year"]
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(template="utter_submit")
        return []
    # def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
    #     """A dictionary to map required slots to
    #         - an extracted entity
    #         - intent: value pairs
    #         - a whole message
    #         or a list of them, where a first match will be picked"""

    #     return {
    #         "faculty": self.from_entity(entity="cuisine", not_intent="chitchat")
    #     }
    @staticmethod
    def faculty_db() -> List[Text]:
        """Database of supported cuisines"""

        return [
            "công nghệ thông tin",
            "khoa học máy tính",
            "điện tử viễn thông",
            "hệ thống thông tin",
            "truyền thông và mạng máy tính",
            "cơ điện tử",
        ]
    def validate_faculty(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate faculty value."""

        if value.lower() in self.faculty_db():
            # validation succeeded, set the value of the "cuisine" slot to value
            return {"faculty": value}
        else:
            dispatcher.utter_message(template="utter_wrong_cuisine")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"faculty": None}    
    def from_entity(self,entity,not_intent):
        
        pass