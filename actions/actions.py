import random
from datetime import datetime
from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionFetchWeather(Action):
   def name(self) -> Text:
      return "action_fetch_weather"

   def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

      # Use today as date if time is not set or time has passed.
      time_string = tracker.get_slot('time')
      time = datetime.fromisoformat(time_string)
      if time is None or time < datetime.now(time.tzinfo):
        time = datetime.now()
      formatted_date = time.strftime("%m/%d/%Y")

      # Here we are returning mock weather data. In a real application this
      # would be an API call to a weather API using the time slot.
      weather_list = ["+24 °C, clear", "+16 °C, mostly clear", "+10 °C, overcast", "+12 °C, moderate rain", "+20 °C, mostly cloudy"]
      result = random.choice(weather_list)

      # Set the weather slot to match the result of the fetched weather data.
      # Set the formatted_date slot so the chatbot can use a more readable date.
      return [SlotSet("weather", result), SlotSet("formatted_date", formatted_date)]
