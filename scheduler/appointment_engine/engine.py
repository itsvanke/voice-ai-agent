
appointments = []

doctor_slots = {
    "cardiologist": ["10am","2pm","4pm"],
    "dermatologist": ["11am","3pm"]
}

def check_availability(doctor, date):
    slots = doctor_slots.get(doctor, [])
    return f"Available slots for {doctor} on {date}: {slots}"

def book_appointment(patient, doctor, date, time):
    for a in appointments:
        if a["doctor"] == doctor and a["date"] == date and a["time"] == time:
            return "Slot already booked"

    appointment = {
        "patient": patient,
        "doctor": doctor,
        "date": date,
        "time": time
    }

    appointments.append(appointment)

    return f"Appointment booked with {doctor} on {date} at {time}"

def cancel_appointment(patient):
    global appointments
    appointments = [a for a in appointments if a["patient"] != patient]
    return "Appointment cancelled"

def reschedule_appointment(patient, new_time):
    for a in appointments:
        if a["patient"] == patient:
            a["time"] = new_time
            return "Appointment rescheduled"

    return "No appointment found"
