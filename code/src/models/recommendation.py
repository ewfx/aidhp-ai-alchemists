import autogen

class RecommendationEngine:
    def __init__(self,config_list):
        self.config_list = config_list
        self.recommendation_agent = autogen.AssistantAgent(
            name="Recommendation_Agent",
            llm_config={ "config_list": config_list},
            system_message="""
    You provide concise, actionable, and personalized recommendations in the following format:

    Recommendations for cust_001:
    1. [Recommendation 1]
    2. [Recommendation 2]
    3. [Recommendation 3]

    Follow these guidelines:
    - Recommendations must align with the customer's spending habits, preferences, and sentiment.
    - Use the example output as a reference for tone and specificity.
    - Do not include explanations or additional analysis. Only provide the recommendations.
    """
        )
        self.user_proxy = autogen.UserProxyAgent(
            name="User_proxy",
            human_input_mode="NEVER",
            code_execution_config={"work_dir":"coding","use_docker": False},
            max_consecutive_auto_reply=1
        )

    def generate_recommendations(self,cust_id,customer_data):
        custom_prompt = f"""
    Analyze the following customer data and provide **concise, actionable, and personalized recommendations** in the following format:

    Recommendations for {cust_id}:
    1. [Recommendation 1]
    2. [Recommendation 2]
    3. [Recommendation 3]

    **Example Output**:
    Recommendations for cust_001:
    1. A premium travel credit card with no foreign transaction fees to align with luxury spending habits.
    2. Early access to Gucci's upcoming collection with an exclusive discount.
    3. A financial planning tool to address budget concerns.

    **Customer Data**:
    {customer_data}
    """
        final_response = self.user_proxy.initiate_chat(
            self.recommendation_agent,
            message=custom_prompt
        )
        recommendations = None
        for message in final_response.chat_history:
            if message["role"] == "user" and message["name"] == "Recommendation_Agent":
                recommendations = message["content"]
                break
        return recommendations