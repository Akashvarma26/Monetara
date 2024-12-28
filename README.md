# 💸 Monetara
Finance assistant bot
     
This project demonstrates the implementation of AI agents for finance and web search tasks using the phi API. The agents are designed to perform specific tasks such as fetching financial data and conducting web searches. A multi-agent system is also included to enable collaboration between the agents. The project is packaged as a Playground app that can be locally hosted in the phidata cloud.


## 🚀 Features
### 1. Web Search Agent
- Purpose: Searches the web for information using DuckDuckGo.     
- Key Features:
    - Always includes sources.
    - Displays results in Markdown format.
    - Leverages the Groq model for enhanced understanding and output.

### 2. Finance AI Agent
- Purpose: Provides financial insights and data.      
- Key Features:
    - Fetches stock prices, analyst recommendations, stock fundamentals, and company news.
    - Displays data in tables for better readability.
    - Uses YFinanceTools for accessing financial data.

### 3. Multi-Agent System
- Purpose: Combines the capabilities of the Web Search Agent and Finance AI Agent.        
- Key Features:
    - Allows agents to work collaboratively.
    - Outputs results in tables and Markdown. 

### 4. Playground App
- Purpose: Runs the agents in a web application interface hosted on the phidata cloud.      
- Features:
    - Interactive agent execution.
    - Real-time tool calls and responses.
         

## 📦 Installation
If you want to use this locally on your system:

1. Clone the Repository:

```
git clone https://github.com/Akashvarma26/Monetara.git
```
2. Install the dependencies - Ensure Python 3.8+ is installed and run:
```
pip install -r requirements.txt
```
3. Set Up Environment Variables:
Create a .env file in the root directory and add the phi API key in this file.
4. Run the file 
```
python playground.py
```
5. Open phidata website and check your application in playground tab.

## 🛠️ Key Technologies

- PHI API: Powers the AI agents.
- Groq Models: High-performance AI models for agent tasks.
- YFinanceTools: Fetches financial data from Yahoo Finance.
- DuckDuckGo Tools: Performs web searches with source attribution.
- Phidata Cloud: Hosts the playground application.