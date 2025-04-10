# Importing required libraries and APIs
import os
from dotenv import load_dotenv
load_dotenv()
import agno
from agno.playground import Playground,serve_playground_app
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools
agno.api=os.getenv("AGNO_API_KEY")

# Web search agent
web_search_agent=Agent(
    name="Web Search Agent",
    role="Search the web for Information",
    model=Groq(id="gemma2-9b-it"),
    tools=[DuckDuckGoTools()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True 
)

# Finance agent
finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True,company_news=True)],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

# Multi Agent
Multi_AI_Agent=Agent(
    team=[web_search_agent,finance_agent],
    model=Groq(id="gemma2-9b-it"),
    instructions=["Always include sources","Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

# Playground app to run in phidata cloud
app=Playground(agents=[finance_agent,web_search_agent]).get_app()
if __name__=="__main__":
    serve_playground_app("playground:app",reload=True)