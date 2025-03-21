import streamlit as st
import pandas as pd
from jobspy import scrape_jobs

st.title("Job Scraper App")

# User inputs
#site_name = st.text_input("Site Name (comma-separated)", "indeed, linkedin, zip_recruiter, glassdoor, google, bayt")
search_term = st.text_input("Search Term", "software engineer")
location = st.text_input("Location", "Kolkata")
results_wanted = st.number_input("Results Wanted", min_value=1, value=20)
hours_old = st.number_input("Job post hours Old", min_value=1, value=72)
country = st.text_input("Country", "INDIA")

if st.button("Scrape Jobs"):
    site_name_list = ["indeed", "linkedin", "zip_recruiter", "glassdoor", "google", "bayt"]
    google_search_term = f"{search_term} jobs near {location} since yesterday"
    jobs = scrape_jobs(
        site_name=site_name_list,
        search_term=search_term,
        google_search_term=google_search_term,
        location=location,
        results_wanted=results_wanted,
        hours_old=hours_old,
        country_indeed=country,
    )
    st.write(f"Found {len(jobs)} jobs")
    st.dataframe(jobs, use_container_width=True)
