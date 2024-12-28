# Importing required libraries and APIs
import os
from dotenv import load_dotenv
load_dotenv()
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

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

# To get response using Agents
Multi_AI_Agent.print_response("Summarize analyst recommendation and share the latest news for NVDA",stream=True)