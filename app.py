import streamlit as st
from crewai import Crew, Process
from tasks import (
    get_market_analysis_task, 
    get_ai_use_cases_task, 
    get_resource_collection_task
)
from agents import (
    market_research_analyst, 
    ai_solutions_strategist, 
    resource_collector
)
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

def generate_pdf(company_name, market_analysis, ai_use_cases, resources):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    c.drawString(100, height - 40, f"Complete Analysis Report for {company_name}")

    c.drawString(100, height - 80, "Industry and Market Analysis")
    text = c.beginText(100, height - 100)
    text.setTextOrigin(100, height - 100)
    text.setFont("Helvetica", 10)
    for line in market_analysis.split('\n'):
        text.textLine(line)
    c.drawText(text)

    c.showPage()

    c.drawString(100, height - 40, "AI/ML Opportunities and Use Cases")
    text = c.beginText(100, height - 60)
    text.setTextOrigin(100, height - 60)
    text.setFont("Helvetica", 10)
    for line in ai_use_cases.split('\n'):
        text.textLine(line)
    c.drawText(text)

    c.showPage()

    c.drawString(100, height - 40, "Implementation Resources and Guidelines")
    text = c.beginText(100, height - 60)
    text.setTextOrigin(100, height - 60)
    text.setFont("Helvetica", 10)
    for line in resources.split('\n'):
        text.textLine(line)
    c.drawText(text)

    c.save()
    buffer.seek(0)
    return buffer

def main():
    st.title("Market Research Analysis Tool")
    company_name = st.text_input("Enter the company name:", placeholder="e.g., Google, Amazon, Tesla")
    
    if st.button("Analyze"):
        if company_name:
            progress_placeholder = st.empty()
            
            with progress_placeholder.container():
                st.info("Step 1/3: Analyzing market data...")
            market_analysis_task = get_market_analysis_task(company_name)
            analysis_crew = Crew(
                agents=[market_research_analyst],
                tasks=[market_analysis_task],
                process=Process.sequential,
            )
            market_analysis_result = analysis_crew.kickoff()
            market_analysis_raw = market_analysis_result.raw if hasattr(market_analysis_result, 'raw') else "No market analysis found"

            with progress_placeholder.container():
                st.info("Step 2/3: Analyzing AI/ML opportunities...")
            ai_use_cases_task = get_ai_use_cases_task(market_analysis_raw)
            ai_use_cases_crew = Crew(
                agents=[ai_solutions_strategist],
                tasks=[ai_use_cases_task],
                process=Process.sequential,
            )
            ai_use_cases_result = ai_use_cases_crew.kickoff()
            ai_use_cases_raw = ai_use_cases_result.raw if hasattr(ai_use_cases_result, 'raw') else "No AI use cases found"

            with progress_placeholder.container():
                st.info("Step 3/3: Collecting implementation resources...")
            resource_task = get_resource_collection_task(ai_use_cases_raw, "")  # Add industry if available
            resource_crew = Crew(
                agents=[resource_collector],
                tasks=[resource_task],
                process=Process.sequential,
            )
            resource_result = resource_crew.kickoff()
            resource_raw = resource_result.raw if hasattr(resource_result, 'raw') else "No resources found"

            progress_placeholder.empty()

            st.header(f"Analysis Report for {company_name}")
            
            with st.expander("Industry and Market Analysis", expanded=True):
                st.markdown(market_analysis_raw)
            
            with st.expander("AI/ML Opportunities and Use Cases"):
                st.markdown(ai_use_cases_raw)
            
            with st.expander("Implementation Resources and Guidelines"):
                st.markdown(resource_raw)

            complete_report = f"""# Complete Analysis Report for {company_name}

## Industry and Market Analysis
{market_analysis_raw}

## AI/ML Opportunities and Use Cases
{ai_use_cases_raw}

## Implementation Resources and Guidelines
{resource_raw}
"""

            pdf = generate_pdf(company_name, market_analysis_raw, ai_use_cases_raw, resource_raw)

            st.download_button(
                label="Download Complete Report",
                data=pdf,
                file_name=f"{company_name}_analysis_report.pdf",
                mime="application/pdf"
            )

if __name__ == "__main__":
    main()