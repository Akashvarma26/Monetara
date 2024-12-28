# Importing required libraries and APIs
import os
from dotenv import load_dotenv
load_dotenv()
import phi.api
import phi
from phi.playground import Playground,serve_playground_app
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
phi.api=os.getenv("PHI_API_KEY")

# Web search agent
web_search_agent=Agent(
    name="Web Search Agent",
    role="Search the web for Information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True 
)

# Finance agent
finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True,company_news=True)],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

# Multi Agent
Multi_AI_Agent=Agent(
    team=[web_search_agent,finance_agent],
    model=Groq(id="llama-3.1-70b-versatile"),
    instructions=["Always include sources","Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

# Playground app to run in phidata cloud
app=Playground(agents=[finance_agent,web_search_agent]).get_app()
if __name__=="__main__":
    serve_playground_app("playground:app",reload=True)