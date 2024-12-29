from crewai import Task
from tools import tool
from agents import market_research_analyst, content_summarizer, ai_solutions_strategist, resource_collector

market_analysis = Task(
    description=(
        "Research the company's industry and segment (e.g., Automotive, Manufacturing, Finance, Retail, Healthcare). "
        "Identify the company's key offerings and strategic focus areas, such as operations, supply chain, or customer experience."
    ),
    expected_output=(
        "A detailed market research report highlighting: "
        "1. Industry and segment of the company, "
        "2. Key offerings, "
        "3. Strategic focus areas, and "
        "4. At least 5 competitors."
    ),
    tools=[tool],
    agent=market_research_analyst,
)

def get_summary_task(content):
    return Task(
        description=(
            f"Create a structured summary of the following market analysis. "
            f"Break down the content into key topics and provide concise summaries for each. "
            f"Content to summarize: {content}"
        ),
        expected_output=(
            "A structured summary of the market analysis, broken down into key topics "
            "with concise summaries for each section. The summary should highlight "
            "the most important insights while maintaining clarity and brevity."
        ),
        agent=content_summarizer
    )

def get_ai_use_cases_task(market_analysis_content):
    return Task(
        description=(
            f"Based on the provided market analysis, identify and propose relevant AI/ML and GenAI use cases "
            f"that could benefit the company. Consider industry trends, company challenges, and competitive landscape. "
            f"Analysis content: {market_analysis_content}"
        ),
        expected_output=(
            "1. A basic 1 or 2 line summary of the company (what it does, how it works, and segment, etc.).\n"
            "2. Use cases with AI:\n"
            "   - Use Case 1: ...\n"
            "   - Use Case 2: ...\n"
            "   - Use Case 3: ...\n"
            "3. Each use case must be explained nicely in 3 points:\n"
            "   a. Objective/Use Case: ...\n"
            "   b. AI Application: ...\n"
            "   c. Cross-Functional Benefit: ...\n"
            "      - Operations & Maintenance: ...\n"
            "      - Finance: ...\n"
            "      - Supply Chain: ..."
        ),
        agent=ai_solutions_strategist
    )

def get_resource_collection_task(ai_use_cases_content):
    return Task(
        description=(
            f"Based on the AI/ML use cases provided, search for relevant datasets, "
            f"pre-trained models, and implementation resources on platforms like Kaggle, "
            f"HuggingFace, and GitHub. For each use case, find specific resources that "
            f"could help in implementation. Use cases content: {ai_use_cases_content}"
        ),
        expected_output=(
            "A structured collection of resources for each AI use case, including:\n"
            "1. Relevant datasets from Kaggle or similar platforms\n"
            "2. Pre-trained models from HuggingFace if applicable\n"
            "3. Similar open-source projects or implementations on GitHub\n"
            "4. Brief description of how each resource could be useful\n"
            "Format as a markdown document with clear sections and links."
        ),
        agent=resource_collector,
        tools=[tool]  
    )