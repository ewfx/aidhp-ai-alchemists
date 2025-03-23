# import autogen
# import pandas as pd

# # Load configuration
# config_list = autogen.config_list_from_json("OAI_CONFIG_LIST.json")

# llm_config = {
#     "config_list": config_list,
# }

# # Define agents
# recommendation_agent = autogen.AssistantAgent(
#     name="Recommendation_Agent",
#     llm_config=llm_config,
#     system_message="""
#     You provide concise, actionable, and personalized recommendations in the following format:

#     Recommendations for cust_001:
#     1. [Recommendation 1]
#     2. [Recommendation 2]
#     3. [Recommendation 3]

#     Follow these guidelines:
#     - Recommendations must align with the customer's spending habits, preferences, and sentiment.
#     - Use the example output as a reference for tone and specificity.
#     - Do not include explanations or additional analysis. Only provide the recommendations.
#     """,
# )

# user_proxy = autogen.UserProxyAgent(
#     name="User_Proxy",
#     human_input_mode="NEVER",
#     code_execution_config={"work_dir": "coding", "use_docker": False},
#     max_consecutive_auto_reply=1,
# )

# # Load customer data
# def load_customer_data(cust_id):
#     df = pd.read_csv(r'D:\hackathon\HACK\aidhp\data\final_data.csv')
#     customer_data = df[df['cust_id'] == cust_id].iloc[0]
#     return customer_data.to_string()

# # Custom prompt for recommendations
# def generate_recommendations(cust_id):
#     content = load_customer_data(cust_id)
#     custom_prompt = f"""
#     Analyze the following customer data and provide **concise, actionable, and personalized recommendations** in the following format:

#     Recommendations for {cust_id}:
#     1. [Recommendation 1]
#     2. [Recommendation 2]
#     3. [Recommendation 3]

#     **Example Output**:
#     Recommendations for cust_001:
#     1. A premium travel credit card with no foreign transaction fees to align with luxury spending habits.
#     2. Early access to Gucci's upcoming collection with an exclusive discount.
#     3. A financial planning tool to address budget concerns.

#     **Customer Data**:
#     {content}
#     """

#     # Initiate chat with the custom prompt
#     final_response = user_proxy.initiate_chat(
#         recommendation_agent,
#         message=custom_prompt
#     )

#     # Extract the recommendations from the chat history
#     recommendations = None
#     for message in final_response.chat_history:
#         if message["role"] == "user" and message["name"] == "Recommendation_Agent":
#             recommendations = message["content"]
#             break

#     return recommendations

# # Generate recommendations for a specific customer
# cust_id = "cust_002"  # Replace with dynamic customer ID if needed
# recommendations = generate_recommendations(cust_id)

# # Print the recommendations
# if recommendations:
#     print(recommendations)
# else:
#     print("No recommendations were generated.")

# # Save the recommendations to a file
# with open("recommendations.txt", 'w') as file:
#     file.write(recommendations if recommendations else "No recommendations were generated.")