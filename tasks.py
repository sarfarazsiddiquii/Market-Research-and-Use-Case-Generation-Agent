from crewai import Task
from tools import tool
from agents import market_research_analyst, ai_solutions_strategist, resource_collector

def get_market_analysis_task(company_name):
    return Task(
        description=(
            f"Conduct a thorough market analysis for the company {company_name}. "
            f"Research the industry and segment the company operates in (e.g., Automotive, Manufacturing, Finance, Retail, Healthcare, etc.). "
            f"Identify the company’s key offerings, strategic focus areas, and market position. "
            f"Analyze the competitive landscape and potential growth opportunities. "
            f"Company: {company_name}"
        ),
        expected_output=(
            "A comprehensive market research report that includes:\n"
            "1. Industry and segment overview\n"
            "2. Key offerings and strategic focus areas\n"
            "3. Detailed analysis of the company's market position\n"
            "4. Competitive landscape with at least 5 competitors\n"
            "5. Potential growth opportunities"
        ),
        tools=[tool],
        agent=market_research_analyst,
    )

def get_ai_use_cases_task(market_analysis_content):
    return Task(
        description=(
            f"Based on the provided market analysis, identify and propose relevant AI/ML and GenAI use cases "
            f"that could benefit the company. Emphasize researching recent reports and case studies from consulting firms like McKinsey, Deloitte, etc., "
            f"or using Google to understand how competitors are leveraging AI/ML in similar segments. "
            f"Ensure the use cases are specific to industry trends and competitive landscape. "
            f"Analysis content: {market_analysis_content}"
        ),
        expected_output=(
            "A brief summary of the company (what it does, how it works, and its segment).\n"
            "AI use cases(at least 10 if not more):\n"
            "   - Use Case 1: ...\n"
            "   - Use Case 2: ...\n"
            "   - Use Case 3: ...\n"
            "Each use case should be explained in 3 points:\n"
            "   a. Objective/Use Case: ...\n"
            "   b. AI Application: ...\n"
            "   c. Cross-Functional Benefit: ...\n"
        ),
        tools=[tool],
        agent=ai_solutions_strategist
    )

def get_resource_collection_task(ai_use_cases_content, company_industry):
    return Task(
        description=(
            f"Based on the AI/ML use cases provided and the company's industry ({company_industry}), conduct a comprehensive "
            f"resource search including:\n"
            f"1. Technical resources: datasets, pre-trained models, and implementation examples\n"
            f"2. Industry insights: Recent reports and case studies from consulting firms about AI in this industry\n"
            f"Use cases content: {ai_use_cases_content}"
        ),
        expected_output=(
            "A comprehensive resource collection with two main sections:\n\n"
            "## Technical Implementation Resources\n"
            "For each AI use case:\n"
            "1. Relevant datasets from platforms like Kaggle (if available)\n"
            "2. Pre-trained models from HuggingFace or similar platforms (if available)\n"
            "3. Similar open-source projects or implementations on GitHub (if available)\n"
            "4. Brief description of how each resource could be useful\n"
            "5. Implementation directions for the company's specific needs\n\n"
            "Format as a markdown document with clear sections and links.\n"
            "Only include resources that are available and relevant, do not direct on how to find one."
        ),
        agent=resource_collector,
        tools=[tool]  
    )