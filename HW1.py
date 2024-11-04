import streamlit as st

# Sidebar Navigation - list of available pages
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Choose a Page:",
    ["Exam Page", "Shiny App Page", "Projects Page"]
)

# Exam Page
if page == "Exam Page":
    st.title("Exam Preparation Bot")

    # Sidebar options for the Exam Page
    st.sidebar.subheader("Exam Options")
    exam_option = st.sidebar.radio(
        "Select an Option:",
        ["Exam Preparation Tips", "Summary of Libraries and Concepts", "Insight for Previous Exam Questions"]
    )

    if exam_option == "Exam Preparation Tips":
        st.header("Exam Preparation Tips")
        st.write("Enter your query to get tips for exam preparation.")
        exam_tips_query = st.text_input("Enter your question:")
        if st.button("Get Exam Tips"):
            st.write(f"Fetching tips for: {exam_tips_query}")
    
    elif exam_option == "Summary of Libraries and Concepts":
        st.header("Summary of Libraries and Concepts")
        summary_query = st.text_input("Enter a concept or library name:")
        if st.button("Get Summary"):
            st.write(f"Fetching summary for: {summary_query}")
    
    elif exam_option == "Insight for Previous Exam Questions":
        st.header("Insight for Previous Exam Questions")
        exam_insight_query = st.text_input("Enter a topic or previous exam question to get insights:")
        if st.button("Get Insights"):
            st.write(f"Fetching insights for: {exam_insight_query}")

# Shiny App Page
elif page == "Shiny App Page":
    st.title("Shiny App Assistance")

    # Options within the Shiny App Page
    st.sidebar.subheader("Shiny App Options")
    shiny_option = st.sidebar.radio(
        "Select an Option:",
        ["Alternate Applications", "Template Based on Project Requirements", "References and Best Practices"]
    )

    if shiny_option == "Alternate Applications":
        st.header("Recommendation for Alternate Applications")
        shiny_app_query = st.text_input("Describe your project to get recommendations for alternate applications:")
        if st.button("Get Recommendations"):
            st.write(f"Fetching alternate applications for: {shiny_app_query}")
    
    elif shiny_option == "Template Based on Project Requirements":
        st.header("Template Recommendations")
        shiny_template_query = st.text_input("Enter your project requirements:")
        if st.button("Get Templates"):
            st.write(f"Fetching templates for: {shiny_template_query}")
    
    elif shiny_option == "References and Best Practices":
        st.header("References and Best Practices")
        shiny_reference_query = st.text_input("Enter a specific technique or ask for best practices:")
        if st.button("Get References"):
            st.write(f"Fetching references and best practices for: {shiny_reference_query}")
        # Add links to Shiny app documentation
        st.markdown("[Shiny App User Guide](https://docs.posit.co/shinyapps.io/guide/)")
        st.markdown("[Shiny App Community Forum](https://forum.posit.co/c/posit-professional-hosted/shinyappsio/24)")

# Projects Page
elif page == "Projects Page":
    st.title("Projects Assistance")

    # Options within the Projects Page
    st.sidebar.subheader("Projects Options")
    project_option = st.sidebar.radio(
        "Select an Option:",
        ["Metadata Explanations", "Domain Knowledge", "High-Level Approach", "Feature Engineering Recommendations"]
    )

    if project_option == "Metadata Explanations":
        st.header("Metadata Explanations")
        metadata_query = st.text_input("Enter a metadata value for explanation:")
        if st.button("Get Explanation"):
            st.write(f"Fetching explanation for: {metadata_query}")
    
    elif project_option == "Domain Knowledge":
        st.header("Domain Knowledge Explanation")
        domain_query = st.text_input("Enter a domain-specific term or question:")
        if st.button("Explain"):
            st.write(f"Providing explanation for: {domain_query}")
    
    elif project_option == "High-Level Approach":
        st.header("High-Level Approach Recommendations")
        high_level_query = st.text_input("Describe your project or approach requirements:")
        if st.button("Get High-Level Approach"):
            st.write(f"Fetching high-level approach for: {high_level_query}")
        # Provide link to CRISP-DM guide
        st.markdown("[CRISP-DM Guide](https://www.crisp-dm.org/)")
    
    elif project_option == "Feature Engineering Recommendations":
        st.header("Feature Engineering Recommendations")
        feature_eng_query = st.text_input("Describe your project for feature engineering recommendations:")
        if st.button("Get Feature Engineering Variables"):
            st.write(f"Fetching feature engineering recommendations for: {feature_eng_query}")
