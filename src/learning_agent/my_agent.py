from agents import Agent, Runner , AsyncOpenAI , set_default_openai_client , set_tracing_disabled , OpenAIChatCompletionsModel
from dotenv import load_dotenv
from pydantic import BaseModel

import os


load_dotenv()  
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("❌ GEMINI_API_KEY is missing. Please set it in your .env file.")




external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash", 
    openai_client=external_client,

)


set_default_openai_client(external_client)
set_tracing_disabled(True)








def center():
   
    
    #   agent = Agent(
    #     name="Gemini Agent",
    #     instructions="You are a joke agent .Whatever topic you are given you gives a joke on that",
    #     model=model,
    # )

    # topic = "India"
    # result = Runner.run_sync(agent, topic)
    # print(result.final_output)


    # urdu_agent = Agent(
    #     name="Urdu Agent",
    #     model = model,
    #     instructions = "You are a hinglish translation agent . Whatever given to you , you translate that into hinglish."
    # )

    # print("Uru Agent works from here!")
    # joke_agent_response = Runner.run_sync(agent , topic)
    # urdu_agent_response = Runner.run_sync(urdu_agent , joke_agent_response.final_output)
    # print(urdu_agent_response.final_output)*/

#-----------------------example of structured output 


    # class Recipe(BaseModel):
    #         title: str
    #         ingredients: list[str]
    #         cooking_time: int
    #         servings: int



    # recipe_agent = Agent(
    #     name="Recipe Agent",
    #     model = model,
    #     instructions= """
    #     **Role:**
    # You are a **Recipe Agent**. Your job is to provide clear, structured, and easy-to-follow cooking recipes for any dish requested.

    # **Behavior Guidelines:**

    # 1. Always format the recipe in **sections**:

    # * **Title**
    # * **Ingredients (with quantities)**
    # * **Instructions (step-by-step)**
    # * **Serving Suggestions**
    # * **Tips & Variations**

    # 2. Use **bullet points** for ingredients.

    # 3. Use **numbered steps** for instructions.

    # 4. Keep language **simple, friendly, and motivating** (imagine you’re teaching a beginner).

    # 5. If the user doesn’t specify a dish, suggest **3 popular recipes** they might like.

    # 6. If the recipe has cultural or dietary variations (e.g., vegan, gluten-free), mention them.

    # 7. Keep portions for **2–4 people by default**, unless the user specifies otherwise.

    # **Example Output Format:**

    # ---

    # ### 🍝 Spaghetti Aglio e Olio

    # **Ingredients:**

    # * 200g spaghetti
    # * 4 garlic cloves (thinly sliced)
    # * ¼ cup olive oil
    # * 1 tsp chili flakes
    # * Salt (to taste)
    # * Fresh parsley (chopped, for garnish)

    # **Instructions:**

    # 1. Boil pasta in salted water until al dente.
    # 2. In a pan, heat olive oil and sauté garlic until golden.
    # 3. Add chili flakes, then toss in the cooked pasta.
    # 4. Mix well, garnish with parsley, and serve hot.

    # **Serving Suggestions:**

    # * Pair with garlic bread or a green salad.

    # **Tips & Variations:**

    # * Add parmesan cheese for extra flavor.
    # * Use whole wheat pasta for a healthier option.

    # ---

    # 👉 This way, every time the agent runs, it outputs a **well-structured recipe** instead of random text.

    # ---

    # Do you want me to make this Recipe Agent **strictly stick to food only**, or also allow fun variations like *“recipe for studying,” “recipe for success,”* etc.?""",

    # output_type = Recipe


    # )

    # prompt = "Make a recipe on biryani"
    # response = Runner.run_sync(recipe_agent , prompt)
    # print(response.final_output)






#     #---------------TOOL CALLING IN AGENT SDK-----------------------
#     from agents import function_tool


#     @function_tool
#     def get_weather(city: str) ->str:
#         """This tool gives the weather """
#         print("weather tool is being called")
#         return (f"The weather in {city} is sunny ")

#     @function_tool
#     def get_temperature(city: str) ->str:
#         """This tool gives the temprature """
#         print("Temperature tool is being called")
#         return (f"The temperature in {city} is 30 dgeree celsius ")
# #----------------------------websearch tool---------------------------
#     from agents import WebSearchTool



#     function_calling_agent = Agent(
#         name = "Function_calling_agent",
#         model = model,
#         tools = [get_weather , get_temperature , ],
#         instructions = "You are a helpful assistant and you call a tool when it is needed" 
#     )


#     response = Runner.run_sync(function_calling_agent,"How old is the moon")
#     print(response.final_output)




# #----------------------------websearch tool---------------------------
# #built in tools can be used with openai api key
#     from agents import WebSearchTool



#----------------------------handoffs--------------------------


    # from pydantic import BaseModel

    # class  Tutorial(BaseModel):
    #     topic : str
    #     outline : str
    #     tutorial: str

    # tutorial_agent = Agent(
    #     name = "Tutorial Agent" ,
    #     model = model , 
    #     handoff_description = "used for making tutroial on the given outline"
    #     instructions ="You are a tutorial agent that takes an outline as input and generates a detailed, step-by-step tutorial with explanations, examples, and clear formatting so the content is easy to follow and suitable for learners.",
    #     output_type=Tutorial

    # )



    # outline_agent = Agent(
    #     name ="Outline generator",
    #     model = model,
    #     instructions = "You are an outline generator agent that takes a topic as input and produces a clear, structured outline with major sections and subpoints, designed to guide an AI agent in creating a step-by-step tutorial based on the outline.",
    #     handoffs = [tutorial_agent],

    # )



    # tutorial = Runner.run_sync(outline_agent , "loops in python")
    # print(tutorial.final_output)




        # #------------------handoff agents more detailed--------------------


        from agents import handoff, RunContextWrapper, Agent, Runner

        # # --- Handoff callbacks ---
        # def on_history_handoff(ctx: RunContextWrapper[None]):
        #     print("👉 Handing off to History Tutor Agent")

        # def on_math_handoff(ctx: RunContextWrapper[None]):
        #     print("👉 Handing off to Math Tutor Agent")

        # def on_english_handoff(ctx: RunContextWrapper[None]):
        #     print("👉 Handing off to English Tutor Agent")


        # # --- Tutor Agents ---
        # history_tutor_agent = Agent(
        #     name="History_tutor_agent",
        #     model=model,
        #     handoff_description="This agent answers any question related to history. It specializes in historical analysis, facts, timelines, important events, and detailed explanations of historical concepts.",
        #     instructions="You are a history tutor. Explain historical events, timelines, and concepts in a clear and engaging way. Provide examples, causes, effects, and significance of events. Adapt explanations based on the learner’s level."
        # )

        # mathematics_tutor_agent = Agent(
        #     name="Mathematics_tutor_agent",
        #     model=model,
        #     handoff_description="This agent is best at solving mathematical problems, explaining formulas, and providing step-by-step solutions across arithmetic, algebra, calculus, geometry, and applied mathematics.",
        #     instructions="You are a mathematics tutor. Solve problems step by step, explain formulas, and provide examples for clarity. When needed, show multiple approaches and explain why they work. Adjust difficulty based on the learner’s background."
        # )

        # english_tutor_agent = Agent(
        #     name="English_tutor_agent",
        #     model=model,
        #     handoff_description="This agent helps with English grammar, vocabulary, comprehension, writing, and literature. It is best at improving communication skills and understanding texts.",
        #     instructions="You are an English tutor. Teach grammar rules, improve vocabulary, and help with reading comprehension and writing. Provide examples, practice exercises, and corrections with clear explanations. Encourage learners to practice with real-world examples."
        # )


        # # --- Router Agent ---
        # router_agent = Agent(
        #     name="Router Agent",
        #     model=model,
        #     instructions=(
        #         "You are a smart routing agent. When given a user question:\n"
        #         "- If it is related to **History**, hand it off to the History Tutor Agent.\n"
        #         "- If it is related to **Mathematics**, hand it off to the Mathematics Tutor Agent.\n"
        #         "- If it is related to **English**, hand it off to the English Tutor Agent.\n"
        #         "- If it is a **general or unrelated question**, answer it yourself directly."
        #     ),
        #     handoffs=[
        #         handoff(history_tutor_agent, on_handoff=on_history_handoff),
        #         handoff(mathematics_tutor_agent, on_handoff=on_math_handoff),
        #         handoff(english_tutor_agent, on_handoff=on_english_handoff)
        #     ]
        # )


        # # --- Run ---
        # prompt = "Gimme the information about HAZRAT MUHAMMAD P.B.U.H"
        # result = Runner.run_sync(router_agent, prompt)

        # print("\n=== FINAL OUTPUT ===")
        # print(result.final_output)

        # # print("\n=== AGENTS INVOKED ===")
        # # for task in result.completed_tasks:
        # #     print(f"- {task.agent_name}")



#---------------------------handof explanation with customer service agent-------------------
       

        class EsclationReason(BaseModel):
            reason : str
            why : str
       

        def on_handoff_to_manager_agent(ctx: RunContextWrapper[None]  , input : EsclationReason):
                print(f"esclating to manager agent becasue of the issue {input.reason}")
                print(f"The reason for esclation is {input.why}")


        manager_agent = Agent(
            name="Manager Agent",
            model=model,
            handoff_description=(
                "Handles managerial tasks such as escalation of issues, "
                "approval requests, policy changes, and complex decision-making "
                "that the customer service agent cannot resolve."
            ),
            instructions=(
                "You are the Manager Agent. You deal with higher-level problems "
                "such as escalations, managerial approvals, and cases where the "
                "customer service agent cannot handle the query. Provide clear "
                "and authoritative responses."
            )
        )
    




        customer_service_agent = Agent(
            name="Customer Service Agent",
            model=model,
            # handoff_description=(
            #     "This agent handles general customer queries, FAQs, account issues, "
            #     "basic troubleshooting, and service-related questions. "
            #     "If a query requires managerial decision-making or escalations, "
            #     "handoff to the Manager Agent."
            # ),
            instructions=(
                """You are the Customer Service Agent. Your job is to resolve 
                customer queries as best as you can. If the customer’s request involves managerial approval, escalation, or policy change, "
                handoff to the Manager Agent instead of answering."""
            ),
            handoffs = [handoff(agent = manager_agent , 
                                input_type = EsclationReason,
                                on_handoff = on_handoff_to_manager_agent)]
        )





        result = Runner.run_sync(customer_service_agent ,"I want to speak to your manager about getting a refund beyond the allowed policy.")
        print(result.final_output)