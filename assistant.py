from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat
from dotenv import load_dotenv
from rag_assistant import knowledge_base
from reserach import DuckDuckGo, Newspaper4k
load_dotenv()

# assistant = Assistant(
#     llm=OpenAIChat(model="gpt-4o"),
#     description="You help people with their health and fitness goals.",
#     instructions=["Recipes should be under 5 ingredients"],
#     debug_mode=True,
# )

# assistant = Assistant(system_prompt="Share a 2 sentence story about")
# assistant.print_response("Love in the year 12000.")


# from phi.assistant import Assistant


referenece = knowledge_base.get_references()


assistant = Assistant(
    tools=[DuckDuckGo(), Newspaper4k()],
    description="You are a famous short story writer asked to write for a magazine",
    instructions=["You are a pilot on a plane flying from Hawaii to Japan."],
    markdown=True,
    debug_mode=True,
    add_references_to_prompt=True,
    add_chat_history_to_prompt=True,
    add_datetime_to_instructions=True,
    show_tool_calls=True
)
assistant.print_response("Tell me a 2 sentence horror story.")

user_prompt += f"""Use this information from the knowledge base if it helps:
<knowledge_base>
{referenece}
</knowledge_base>
"""

user_prompt += f"""Use the following chat history to reference past messages:
<chat_history>
{chat_history}
</chat_history>
"""