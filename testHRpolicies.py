from contextual import ContextualAI

# Initialize the client
contextual = ContextualAI(api_key="key-h5YQeAdoKapuVqK-2N2Ii35j6ruRFgORpQSHJ7u1PtIJ4WGjw")

# Use your existing agent's ID
HRPOLICIES_AGENT_ID = "0ac61640-7c68-4fbf-95f3-76829f33529d"

# query = "I am a part-time employee. Am I eligible for medical/dental? How does ACA apply to me ?"
# query ="I am a full-time employee in IT department. How much life insurance do I have from the company??"
query = "I am a part-time employee in IT department. What documents are needed for dependent verification?"

# Send a query to the agent
response = contextual.agents.query.create(
    agent_id=HRPOLICIES_AGENT_ID,
    messages=[{
        "role": "user",
        "content": query
    }]
)

# Print the response
print(" Response:", response.message.content)
