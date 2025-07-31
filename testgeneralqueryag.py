from contextual import ContextualAI

# Initialize the client
contextual = ContextualAI(api_key="key-h5YQeAdoKapuVqK-2N2Ii35j6ruRFgORpQSHJ7u1PtIJ4WGjw")

general_agent_id = "4dae0b15-6abd-443e-b069-8f867f897618"

response = contextual.agents.query.create(
    agent_id=general_agent_id,
    messages=[{
        "role": "user",
        "content": "How do I update my address in HR records?"
    }]
)

print("🤖 Response:", response.message.content)
