import streamlit as st
from crewai import Crew, Process
from tasks import market_analysis, get_summary_task, get_ai_use_cases_task
from agents import market_research_analyst, content_summarizer, ai_solutions_strategist

def main():
    st.title("Market Research Analysis Tool")
    company_name = st.text_input("Enter the company name:", placeholder="e.g., Google, Amazon, Tesla")
    
    if st.button("Analyze"):
        if company_name:
            with st.spinner("Analyzing market data..."):
                market_analysis.description = (
                    f"Research the industry or segment of the company {company_name}. "
                    f"Identify the company's key offerings and strategic focus areas. "
                    f"Provide a detailed analysis for {company_name}."
                )

                analysis_crew = Crew(
                    agents=[market_research_analyst],
                    tasks=[market_analysis],
                    process=Process.sequential,
                )
                analysis_result = analysis_crew.kickoff()
                raw_result = analysis_result.raw if hasattr(analysis_result, 'raw') else "No raw result found"

            with st.spinner("Generating summary..."):
                summary_task = get_summary_task(raw_result)
                summary_crew = Crew(
                    agents=[content_summarizer],
                    tasks=[summary_task],
                    process=Process.sequential,
                )
                summary_result = summary_crew.kickoff()

            with st.spinner("Analyzing AI/ML opportunities..."):
                ai_use_cases_task = get_ai_use_cases_task(raw_result)
                ai_use_cases_crew = Crew(
                    agents=[ai_solutions_strategist],
                    tasks=[ai_use_cases_task],
                    process=Process.sequential,
                )
                ai_use_cases_result = ai_use_cases_crew.kickoff()

            st.header(f"Analysis Results for {company_name}")
            
            st.subheader("Executive Summary")
            st.write(summary_result.raw if hasattr(summary_result, 'raw') else "No summary generated")
            
            st.subheader("AI/ML Opportunities")
            st.write(ai_use_cases_result.raw if hasattr(ai_use_cases_result, 'raw') else "No AI use cases generated")
            
            with st.expander("View Detailed Market Analysis"):
                st.write(raw_result)
        else:
            st.error("Please enter a company name.")

if __name__ == "__main__":
    main()