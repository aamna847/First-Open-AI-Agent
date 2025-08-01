from dotenv import load_dotenv
import os
from agents import Agent, AsyncOpenAI , OpenAIChatCompletionsModel , RunConfig, Runner

load_dotenv()
openrouter_api_key=os.getenv("OPENROUTER_API_KEY")

#Check if the api key is present or not.
if  not openrouter_api_key:
    raise ValueError("Openrouter_api_key is not present.Please ensure that it is in .env file.")
# Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=openrouter_api_key,
    base_url="https://openrouter.ai/api/v1"
)

model= OpenAIChatCompletionsModel (
    model="z-ai/glm-4.5-air:free",
    openai_client= external_client
)

config=RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

agent=Agent(
    name="Writer Agent",
    instructions="You are a writer agent.Generate stories poems or essay etc."
)

response=Runner.run_sync(
    agent,
    input="Write a horror Anabella Story in simple english",
    run_config=config
)

print(response)