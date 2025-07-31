from contextual import ContextualAI

# Initialize the client
contextual = ContextualAI(api_key="key-h5YQeAdoKapuVqK-2N2Ii35j6ruRFgORpQSHJ7u1PtIJ4WGjw")

# Replace with your actual datastore ID for general HR info
GENERAL_HR_DATASTORE_ID = "f4366781-d344-4215-8ee4-88d914b38208"

# Define the system prompt
general_prompt = """
You are an HR General Enquiry Agent.

Your role is to answer common HR-related questions that are not specific to policies or employee types.

Examples of such questions:
- How do I update my contact details?
- What are the HR department's contact hours?
- How do I apply for reimbursement?

Only use the uploaded documents to answer.
If the answer isn’t found, respond with: "Please contact HR directly for that information."
"""

# Create the GeneralQueryAgent
general_agent = contextual.agents.create(
    name="GeneralQueryAgent",
    system_prompt=general_prompt,
    datastore_ids=[GENERAL_HR_DATASTORE_ID]
)

print(" GeneralQueryAgent created with ID:", general_agent.id)
