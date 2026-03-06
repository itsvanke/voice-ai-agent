
from scheduler.appointment_engine.engine import (
    check_availability,
    book_appointment,
    cancel_appointment,
    reschedule_appointment
)

def execute_tool(intent):
    action = intent.get("intent")

    if action == "availability":
        return check_availability(intent["doctor"], intent["date"])

    if action == "book":
        return book_appointment(
            "patient1",
            intent["doctor"],
            intent["date"],
            intent["time"]
        )

    if action == "cancel":
        return cancel_appointment("patient1")

    if action == "reschedule":
        return reschedule_appointment("patient1", intent["time"])

    return "I could not understand the request"
