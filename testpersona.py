from contextual import ContextualAI

# Initialize the client
contextual = ContextualAI(api_key="key-h5YQeAdoKapuVqK-2N2Ii35j6ruRFgORpQSHJ7u1PtIJ4WGjw")

# Use your existing agent's ID
PERSONA_AGENT_ID = "82365336-ef80-43de-a0f7-fd6a4c7c1c7a"

# Ask a query
query = "Who is Brena Galbreath ?"

# Send the query to the agent
response = contextual.agents.query.create(
    agent_id=PERSONA_AGENT_ID,
    messages=[{"role": "user", "content": query}]
)

# Print the result
print("\n Query:", query)
print(" Response:", response.message.content)

