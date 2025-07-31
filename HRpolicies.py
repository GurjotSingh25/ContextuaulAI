from contextual import ContextualAI

contextual = ContextualAI(api_key="key-h5YQeAdoKapuVqK-2N2Ii35j6ruRFgORpQSHJ7u1PtIJ4WGjw")

# Replace with actual datastore ID where HR policy is uploaded
DATASTORE_ID = "f4366781-d344-4215-8ee4-88d914b38208"

policy_prompt = """
You are an HR Policy Agent.

Your job is to:
- Answer employee questions about HR policies (e.g., leave policy, sick days, working hours, etc.)
- Use only the content from the uploaded HR policy documents.
- Tailor your answer based on the employee type: Full-Time, Part-Time, or Contractor. This will be provided in the question.
- If the policy is not found in the document, reply: "I couldn't find the relevant HR policy in the documents."
"""

policy_agent = contextual.agents.create(
    name="HRPolicyAgent",
    system_prompt=policy_prompt,
    datastore_ids=[DATASTORE_ID],
)

print(" HRPolicyAgent created with ID:", policy_agent.id)
