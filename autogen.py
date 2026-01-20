import asyncio
from autogen_core.models import UserMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import ModelInfo
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import StructuredMessage
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
import os 
import dotenv

dotenv.load_dotenv()

model_client = OpenAIChatCompletionClient(
    model="gemini-2.5-flash-lite",
    model_info=ModelInfo(vision=True, function_calling=True, json_output=True, family="unknown", structured_output=True),
    api_key = os.getenv("API_KEY"),
)

'''
async def main():
    response = await model_client.create([UserMessage(content="what is the purpose of the life?", source="user")])
    print(response)
    await model_client.close()

asyncio.run(main())
'''

# Define a tool that searches the web for information.
# For simplicity, we will use a mock function here that returns a static string.
async def web_search(query: str) -> str:
    """Find information on the web"""
    return "Renaissance art affair usually refers to the art produced during the Renaissance (c. 14th-16th centuries), a period of rebirth in Europe focusing on classical ideals, humanism, realism, and natural beauty, shifting from medieval abstraction to lifelike depictions of biblical, mythological, and contemporary subjects, exemplified by masters like Leonardo da Vinci, Michelangelo, and Raphael, often commissioned to celebrate love, marriage, and humanist ideals. It's a cultural movement marked by scientific interest, new techniques (like linear perspective), and a profound shift towards human experience in art. "




agent = AssistantAgent(
    name="assistant",
    model_client=model_client,
    tools=[web_search],
    system_message="use the tool to gather the information and then summarise it in 2 lines at max 20 words ",
    reflect_on_tool_use=True
    )

# Use asyncio.run(agent.run(...)) when running in a script.
async def run_agent():
    result = await agent.run(task="renisance give me a short overview")
    #print(type(result.messages))    ## class 'list'
    a= result.messages
    for i in a:
        print(i,end="\n\n\n")
        #print(type(i))  ##<class 'autogen_agentchat.messages.TextMessage'>
    #[TextMessage(source='user', models_usage=None, metadata={}, content='Find information on AutoGen', type='TextMessage'), ToolCallRequestEvent(source='assistant', models_usage=RequestUsage(prompt_tokens=61, completion_tokens=16), metadata={}, content=[FunctionCall(id='call_703i17OLXfztkuioUbkESnea', arguments='{"query":"AutoGen"}', name='web_search')], type='ToolCallRequestEvent'), ToolCallExecutionEvent(source='assistant', models_usage=None, metadata={}, content=[FunctionExecutionResult(content='AutoGen is a programming framework for building multi-agent applications.', name='web_search', call_id='call_703i17OLXfztkuioUbkESnea', is_error=False)], type='ToolCallExecutionEvent'), ToolCallSummaryMessage(source='assistant', models_usage=None, metadata={}, content='AutoGen is a programming framework for building multi-agent applications.', type='ToolCallSummaryMessage')]

asyncio.run(run_agent())

