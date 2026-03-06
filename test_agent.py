from agent.reasoning.agent_engine import process_request

print("AI Appointment Agent Test")
print("Type something like: book cardiologist tomorrow at 10am")
print("Type 'exit' to stop")
print()

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    try:
        response = process_request(user_input)
        print("AI:", response)
    except Exception as e:
        print("Error:", e)