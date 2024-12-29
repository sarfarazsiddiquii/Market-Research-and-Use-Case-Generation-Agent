from crewai import Agent, LLM
from tools import tool
from dotenv import load_dotenv
import os

load_dotenv()


llm = LLM(
    api_key='AIzaSyBnY_vwi625k8ViMuCqHM596uZfsD0gyCw',  
    model="gemini/gemini-1.5-flash",
    provider="google",
    verbose=True,
    temperature=0.5
)


market_research_analyst = Agent(
    role="Market Research Analyst",
    goal="Analyze market trends and provide insights about companies.",
    verbose=True,
    memory=True,
    backstory=(
        "You are a Market Research Analyst specializing in gathering and analyzing "
        "market data to understand trends, consumer behavior, and competitive dynamics. "
        "Your focus is to assess the market potential of companies and analyze their competitive landscape."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

content_summarizer = Agent(
    role="Content Summarizer",
    goal="Create concise, structured summaries of market analysis reports",
    verbose=True,
    memory=True,
    backstory=(
        "You are an expert in distilling complex information into clear, structured summaries. "
        "Your specialty is breaking down lengthy market analysis reports into key topics and "
        "providing concise summaries while maintaining the most important insights."
    ),
    llm=llm,
    allow_delegation=False
)

ai_solutions_strategist = Agent(
    role="AI/ML Solutions Strategist",
    goal="Identify and propose relevant AI/ML use cases based on company analysis",
    verbose=True,
    memory=True,
    backstory=(
        "You are an AI/ML Solutions Strategist with extensive experience in implementing "
        "AI, ML, and GenAI solutions across various industries. You excel at identifying "
        "opportunities where these technologies can drive business value, enhance operations, "
        "and improve customer experience. Your expertise includes understanding industry-specific "
        "challenges and proposing targeted AI solutions."
    ),
    llm=llm,
    allow_delegation=False
)

resource_collector = Agent(
    role="AI Resource Collector",
    goal="Find and collect relevant datasets and resources for AI/ML implementations",
    verbose=True,
    memory=True,
    backstory=(
        "You are an AI Resource Specialist who excels at finding relevant datasets, "
        "pre-trained models, and implementation resources. You have extensive knowledge "
        "of platforms like Kaggle, HuggingFace, and GitHub, and can identify the most "
        "suitable resources for specific AI/ML use cases."
    ),
    tools=[tool],  
    llm=llm,
    allow_delegation=False
)