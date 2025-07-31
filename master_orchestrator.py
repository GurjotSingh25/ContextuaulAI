from contextual import ContextualAI

# Initialize the client
contextual = ContextualAI(api_key="key-h5YQeAdoKapuVqK-2N2Ii35j6ruRFgORpQSHJ7u1PtIJ4WGjw")

# Replace with your actual agent IDs
PERSONA_AGENT_ID = "82365336-ef80-43de-a0f7-fd6a4c7c1c7a"
HR_POLICY_AGENT_ID = "0ac61640-7c68-4fbf-95f3-76829f33529d"

def ask_persona_agent(employee_name: str) -> str:
    """Ask PersonaAgent for the user's employment details"""
    lookup_prompt = f"What is the employment status and department of {employee_name}?"
    
    response = contextual.agents.query.create(
        agent_id=PERSONA_AGENT_ID,
        messages=[{"role": "user", "content": lookup_prompt}]
    )
    return response.message.content.strip()

def ask_policy_agent(enriched_query: str) -> str:
    """Ask HRPolicyAgent using context + user query"""
    response = contextual.agents.query.create(
        agent_id=HR_POLICY_AGENT_ID,
        messages=[{"role": "user", "content": enriched_query}]
    )
    return response.message.content.strip()

def master_orchestrator(user_query: str, employee_name: str) -> str:
    print(" User Query:", user_query)
    print(" Employee Name:", employee_name)

    # Step 1: Get user context
    persona_context = ask_persona_agent(employee_name)
    print(" PersonaAgent Response:", persona_context)

    # Step 2: Enrich the original question
    enriched_query = f"{persona_context}. Now answer this question: {user_query}"

    # Step 3: Pass to HRPolicyAgent
    policy_response = ask_policy_agent(enriched_query)
    return policy_response

# 🔁 Example usage
if __name__ == "__main__":
    # Simulated inputs
    employee_name = "Christabel Poxton"
    user_question = "Why do I see no deduction for medical insurance??"

    final_response = master_orchestrator(user_question, employee_name)
    print("\n Final Answer:", final_response)
