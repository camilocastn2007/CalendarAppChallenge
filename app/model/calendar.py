from dataclasses import dataclass, field
from datetime import datetime, date, time
from email.policy import default
from typing import ClassVar

from app.services.util import generate_unique_id, date_lower_than_today_error, event_not_found_error, \
    reminder_not_found_error, slot_not_available_error


@dataclass
class Reminder:

    EMAIL :str ="email"
    SYSTEM :str = "system"

    date_time = datetime
    type: str = type

    def __str__(self)-> str:
        f"Reminder on {self.date_time} of type {self.type}"


@dataclass
class Event:
    title: str
    description: str
    date_: date
    start_at: time
    end_at: time
    reminders: list[Reminder] = field(default=list)
    id: str = field(default_factory=generate_unique_id())

    def add_reminder(self,date_time :datetime,type :str):

        reminder = Reminder(date_time=datetime,type=type)
        self.reminders = Reminder.append(reminder)

    def delete_reminder(self,reminder_ex :int):
        pass

    def __str__(self):
        return
        ID: {self.id}
        Event_title: {self.title}
        Description: {self.description}
        Time: {self.start_at} - {self.end_at}




