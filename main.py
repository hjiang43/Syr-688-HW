import streamlit as st
from Exam_Page import run_exam_page
from Shiny_App_Page import run_shiny_page
from Projects_Page import run_projects_page
from FAQ_Page import run_faq_page  # Import FAQ Page
from Requirements_Page import run_requirements_page  # Import Requirements Page
from Google_Calendar_Page import run_google_calendar_page

exam_page = st.Page(run_exam_page, title="Exam Page", icon="👉")
shiny_page = st.Page(run_shiny_page, title="Shiny App Page", icon="🔥")
projects_page = st.Page(run_projects_page, title="Projects Page", icon="📚")
faq_page = st.Page(run_faq_page, title="FAQ Page", icon="❓")  # New FAQ Page
requirements_page = st.Page(run_requirements_page, title="Requirements Page", icon="📄")  # New Requirements Page
google_calendar_page = st.Page(run_google_calendar_page, title="Google Calendar Page", icon="📅")  # New Page

pg = st.navigation([exam_page, shiny_page, projects_page, faq_page, requirements_page, google_calendar_page])

pg.run()
