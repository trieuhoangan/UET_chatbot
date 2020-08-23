# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Text, List, Optional, Union, Any, Dict, Tuple

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa.core.domain import Domain
from rasa_sdk.forms import FormAction
from enum import Enum
from rasa.core.actions.action import (
    ActionExecutionRejection,
    RemoteAction,
    ACTION_LISTEN_NAME,
)
# logger = logging.getLogger(__name__)
# class SlotMapping(Enum):
#     FROM_ENTITY = 0
#     FROM_INTENT = 1
#     FROM_TRIGGER_INTENT = 2
#     FROM_TEXT = 3
#     def __str__(self) -> Text:
#         return self.name.lower()

class PointFormActinon(FormAction):
    def name(self) -> Text:
        return "point_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["faculty","year"]
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message("diem khoa {} nam {} la day nhe".format(tracker.get_slot("faculty"),tracker.get_slot("year")))
        return []
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "faculty": self.from_entity(entity="faculty", not_intent="chitchat"),
            "year":self.from_entity(entity="year")
        }
    @staticmethod
    def faculty_db() -> List[Text]:
        """Database of supported cuisines"""

        return [
            "công nghệ thông tin"
            "điện tử viễn thông",
            "cơ kỹ thuật",
            "vật lý kỹ thuật","công nghệ nano","tự động hóa","cơ học kỹ thuật","công nghệ nông nghiệp"
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
            dispatcher.utter_message(text="không có khoa bạn nhắc đến")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"faculty": None}
    @staticmethod
    def  year_db() -> List[Text]:
        return ["2020","2019","2018","2017","2016","năm nay"]
    def validate_year(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate faculty value."""

        if value.lower() in self.year_db():
            # validation succeeded, set the value of the "cuisine" slot to value
            return {"year": value}
        else:
            dispatcher.utter_message(text="không có năm bạn nhắc đến")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"year": None}  
    # def run(self, dispatcher, tracker, domain):
    #     pass
    # def from_entity(self,entity,not_intent):
    #     return [SlotSet("account_type",entity)]