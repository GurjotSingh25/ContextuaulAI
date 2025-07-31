from contextual import ContextualAI

contextual = ContextualAI(api_key="key-h5YQeAdoKapuVqK-2N2Ii35j6ruRFgORpQSHJ7u1PtIJ4WGjw")

# Replace with your actual datastore ID
DATASTORE_ID = "6abfd7bb-0067-4e10-95cb-6a1317af2a8b"

persona_prompt = """
You are an HR Persona Validation Agent.

Your job is to:
- Check whether a user (by name or employee ID) exists in the employee database.
- Return their employment status: Full-Time or Part-Time.
- If the employee is not found, respond with: "Employee not found."

Refer only to the document uploaded which contains employee records.
"""

persona_agent = contextual.agents.create(
    name="PersonaAgent",
    system_prompt=persona_prompt,
    datastore_ids=[DATASTORE_ID],
)
print("PersonaAgent created with ID:", persona_agent.id)


response = contextual.chat.create(
    agent_id=persona_agent.id,
    messages=[{"role": "user", "content": "What is the job status of Brena Galbreath?"}]
)

print("Bot:", response["message"]["content"])
