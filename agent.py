from langchain_groq import ChatGroq

# Initialize the Language Model
llm = ChatGroq(model="llama-3.1-8b-instant", api_key="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")

# Install necessary packages
from langchain_community.tools import DuckDuckGoSearchRun
import os
import re
from langchain_community.chat_models import ChatOpenAI
from langchain.tools import Tool
from langchain.agents import AgentType, initialize_agent
from langchain.memory import ConversationBufferMemory

# Set OpenAI API Key
os.environ["OPENAI_API_KEY"] = 'YOUR_OPENAI_API_KEY'

# Mock Data for Venues, Caterers, and Entertainment
venues = [
    {"name": "Sunset Gardens", "capacity": 100, "price": 1000},
    {"name": "Ocean View Hall", "capacity": 200, "price": 2000},
    {"name": "Mountain Retreat", "capacity": 50, "price": 800},
]

caterers = [
    {"name": "Gourmet Bites", "cuisine": "Italian", "price_per_person": 25},
    {"name": "Fiesta Feast", "cuisine": "Mexican", "price_per_person": 20},
    {"name": "Sushi World", "cuisine": "Japanese", "price_per_person": 30},
]

entertainment_options = [
    {"name": "DJ Spin", "type": "DJ", "price": 500},
    {"name": "The Jazz Band", "type": "Live Band", "price": 800},
    {"name": "Magic Mike", "type": "Magician", "price": 400},
]
duckduckgo_search = DuckDuckGoSearchRun()

# Define Tools
def search_tool(input_text):
    query = f"{input_text} near me"
    results = duckduckgo_search.run(query)
    return results

def search_venues(query):
    capacity = int(query.get("capacity", 0))
    results = [v for v in venues if v["capacity"] >= capacity]
    return results

def search_caterers(query):
    cuisine = query.get("cuisine", "").lower()
    results = [c for c in caterers if cuisine in c["cuisine"].lower()]
    return results

def search_entertainment(query):
    type_ = query.get("type", "").lower()
    results = [e for e in entertainment_options if type_ in e["type"].lower()]
    return results

def book_service(service_type, name):
    return f"{service_type} '{name}' has been booked successfully!"

# Tool Wrappers
def venue_tool(input_text):
    capacity_matches = re.findall(r'\b\d+\b', input_text)
    capacity = capacity_matches[0] if capacity_matches else "0"
    query = {"capacity": capacity}
    results = search_venues(query)
    return f"Available venues: {results}"

def caterer_tool(input_text):
    cuisine_match = re.search(r'cuisine\s+(\w+)', input_text, re.IGNORECASE)
    cuisine = cuisine_match.group(1) if cuisine_match else ""
    query = {"cuisine": cuisine}
    results = search_caterers(query)
    return f"Available caterers: {results}"

def entertainment_tool(input_text):
    type_match = re.search(r'type\s+(\w+)', input_text, re.IGNORECASE)
    type_ = type_match.group(1) if type_match else ""
    query = {"type": type_}
    results = search_entertainment(query)
    return f"Available entertainment options: {results}"

def booking_tool(input_text):
    parts = input_text.split(" ", 2)
    if len(parts) < 3:
        return "Invalid booking format. Please use 'book [service_type] [name]'."
    service_type = parts[1]
    name = parts[2]
    confirmation = book_service(service_type, name)
    return confirmation

# Define LangChain Tools
tools = [
    Tool(
        name="WebSearch",
        func=search_tool,
        description="Use this tool to search for information on the web.",
    ),
    Tool(
        name="SearchVenues",
        func=venue_tool,
        description="Use this tool to find venues based on capacity requirements."
    ),
    Tool(
        name="SearchCaterers",
        func=caterer_tool,
        description="Use this tool to find caterers based on cuisine preferences."
    ),
    Tool(
        name="SearchEntertainment",
        func=entertainment_tool,
        description="Use this tool to find entertainment options based on type."
    ),
    Tool(
        name="BookService",
        func=booking_tool,
        description="Use this tool to book a service. Input should be 'book [service_type] [name]'."
    ),
]

# Initialize Memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

agent_kwargs = {'prefix': f'You are a helpful birthday event planner assistant. Your job is to assist users in planning their events by finding venues, caterers, and entertainment, and also help with booking services.'}

# Initialize Agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    agent_kwargs=agent_kwargs,
    verbose=True,
    memory=memory,
)


# define q and a function for frontend
def get_response(user_input):
    response = agent.invoke({"input": user_input})
    return response


# Example Interaction
def run_agent():
    print("Assistant: Hello! I'm here to help you plan your birthday party. What would you like to start with?")
    while True:
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Assistant: Goodbye! Feel free to reach out if you need more help.")
            break
        try:
            response = agent.invoke({"input": user_input})
            print(f"Assistant: {response['output']}")
        except Exception as e:
            print(f"Assistant: I'm sorry, an error occurred: {e}")

# Run the agent
if __name__ == "__main__":
    run_agent()
