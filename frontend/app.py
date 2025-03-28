import streamlit as st
import requests
import json
import pandas as pd
import os

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="UniQuestAI", layout="wide")

# Inject custom CSS to set the width of the sidebar
st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 500px !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize session state for results
if "result_json" not in st.session_state:
    st.session_state.result_json = None

# Initialize session state for research topic
if "discipline" not in st.session_state:
    st.session_state.discipline = ""

# Initialize session state for max papers
if "education_level" not in st.session_state:
    st.session_state.education_level = ""

# Initialize session state for selected paper
if "location" not in st.session_state:
    st.session_state.location = "Worldwide"

# Initialize session state for chat history
if "max_universities" not in st.session_state:
    st.session_state.max_universities = 10

# Create a two-column layout
col1, col2 =st.columns([1, 11])
with col1:
    st.image("../images/uniquest_logo.png", width=150)
with col2:
    st.title("UniQuestAI")

# Display the main title and search form in the sidebar  
with st.sidebar:
    st.subheader("Search the best unviversities")
    st.info("Enter your preferences to get started.")
    
    # User input fields
    discipline = st.text_input("Enter Discipline:")
    education_level = st.selectbox("Select Education Level:", ["Bachelors", "Masters", "PhD"])
    location = st.text_input("Enter Location:", "Worldwide")
    max_universities = st.number_input("Number of Universities:", 5, 50, 10)

    col_btn1, col_btn2 = st.columns([3, 1])

    with col_btn1:
        if st.button("Search"):
            st.session_state.searching = True
            if discipline:
                st.session_state.discipline = discipline
                st.session_state.education_level = education_level
                st.session_state.location = location
                st.session_state.max_universities = max_universities

                try:
                    with st.spinner("Searching for top universities..."):
                        st.warning("It may take a few minutes for the search to complete. Please be patient!")
                        response = requests.post(API_URL+"/search/", json={"discipline": discipline, "education_level": education_level, "location": location, "max_universities": max_universities})

                    if response.status_code != 200:
                        st.error("Error: Invalid response from server.")
                        st.stop()

                    result_decoded = response.content.decode("utf-8")
                    st.session_state.result_json = json.loads(result_decoded)  # Store in session state

                except json.JSONDecodeError:
                    st.error("Error: Received an unreadable response from the server.")
                    st.stop()
                except requests.exceptions.RequestException:
                    st.error("Error: Could not connect to the server.")
                    st.stop()

    with col_btn2:
        if st.button("🔄 Refresh"):
            st.session_state.result_json = None  # Clear stored results
            st.session_state.discipline = ""  # Clear stored discipline
            st.session_state.education_level = ""  # Clear stored education level
            st.session_state.location = "Worldwide"  # Clear stored location
            st.session_state.max_universities = 10  # Reset max universities
            st.rerun()  # Force a full page refresh
            
# Display results if available
if st.session_state.result_json:
    st.title(f"Top Universities for {discipline} ({education_level}) in {location if location else 'the World'}")
    # Display the results
    # st.write(st.session_state.result_json.get("response", "No results to display."))

    # If an excel path is provided in the response, display download option
    if "excel_path" in st.session_state.result_json:
        excel_path = st.session_state.result_json["excel_path"]
        excel_path = os.path.join("../backend", excel_path)

        filename = f"Top_Universities_{education_level}_{discipline}_{location}.xlsx"

        # Create a row layout for success message + download button
        col_success, col_download = st.columns([11, 1])

        with col_success:
            st.success("Top Universities Found!")

        with col_download:
            st.download_button(label="📥 Download", 
                            data=open(excel_path, "rb").read(), 
                            file_name=filename,
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    # Display universities information
    response = st.session_state.result_json.get("response")

    # universities = json.loads(response["universities"])
    # links = response["links"]
    # information = response["information"]
    # processed_info = json.loads(response["processed_info"])
    processed_info = response["processed_info"]

    # st.write(universities)
    # st.write(links)
    # st.write(information)
    # st.write(processed_info)

    json_info = json.loads(processed_info)

    universities = json_info.get("universities", [])  

    if universities:
        # Convert the list of university dictionaries into a Pandas DataFrame
        df = pd.DataFrame(universities)
        df.rename(columns={"name":"University Name", "location":"Location", "status":"Status", "founded":"Founded", 
                           "us_news_ranking":"US News Ranking", "qs_ranking":"QS Ranking", "times_ranking":"THE Ranking", 
                           "program":"Program", "program_begins":"Program Begins", "gre_requirement":"GRE Requirement", 
                           "toefl_score":"TOEFL Score", "ielts_score":"IELTS Score", "duolingo_accepted":"Duolingo Accepted?",
                           "english_proficiency_waiver":"English Proficiency Waiver", "application_fee":"Application Fee", 
                           "application_deadline":"Application Deadline", "office_contact_and_email":"Office Contact & Email",
                           "acceptance_rate":"Acceptance Rate", "required_documents":"Required Documents",
                           "number_of_lors":"Number of LORs", "additional_notes":"Additional Notes", "link":"Program Link"}, inplace=True,)
        st.dataframe(df)

        for i, university in enumerate(universities):
            st.subheader(f"🎓 {i+1}. {university['name']}")
            st.markdown(f"**📍 Location:** {university['location']}")
            st.markdown(f"**📚 Status:** {university['status']}")
            st.markdown(f"**📆 Founded:** {university['founded']}")
            st.markdown(f"**📈 US News Ranking:** {university['us_news_ranking']}")
            st.markdown(f"**📈 QS Ranking:** {university['qs_ranking']}")
            st.markdown(f"**📈 Times Higher Education Ranking:** {university['times_ranking']}")
            st.markdown(f"**📚 Program:** {university['program']}")
            st.markdown(f"**📅 Program Begins:** {university['program_begins']}")
            st.markdown(f"**📝 GRE Requirement:** {university['gre_requirement']}")
            st.markdown(f"**📝 TOEFL Score:** {university['toefl_score']}")
            st.markdown(f"**📝 IELTS Score:** {university['ielts_score']}")
            st.markdown(f"**📝 Duolingo Accepted?:** {university['duolingo_accepted']}")
            st.markdown(f"**📝 English Proficiency Waiver:** {university['english_proficiency_waiver']}")
            st.markdown(f"**💸 Application Fee:** {university['application_fee']}")
            st.markdown(f"**💸 Application Fee Waiver:** {university['application_fee_waiver']}")
            st.markdown(f"**💸 Tuition|Stipend:** {university['tuition_stipend']}")
            st.markdown(f"**📅 Application Opens:** {university['application_opens']}")
            st.markdown(f"**📅 Application Deadline:** {university['application_deadline']}")
            st.markdown(f"**📞 Office Contact and Email:** {university['office_contact_and_email']}")
            st.markdown(f"**📝 Acceptance Rate:** {university['acceptance_rate']}")
            st.markdown(f"**📝 Required Documents:** {university['required_documents']}")
            st.markdown(f"**📝 Number of LoRs:** {university['number_of_lors']}")
            st.markdown(f"**📝 Additional Notes:** {university['additional_notes']}")
            st.markdown(f"**📝 Link to the Program:** {university['link']}")
            st.divider()             
    else:
        st.error("No universities found!")
else:
    st.subheader("Your ultimate AI companion for finding the best universities around the world!")
    st.success("**Welcome to UniQuestAI**, your trusted AI companion for finding the best universities around the world!")
    st.markdown("- Here, you can search for universities based on your **education level**, **discipline**, and **preferred location**.")
    st.markdown("- Our AI-powered platform will help you find the top universities that match your preferences and requirements.")
    st.markdown("- Not only that, we'll compile a list of universities for you, including their names, locations, admission requirements, and other relevant information.")
    st.info("**So, what are you waiting for? Let's get started and find your dream university today!**")

    todo = ["📚 Enter a Discipline", "🎓 Select an Education Level", "📌 Enter a Location", "#️⃣ Enter Number of Universities", "🔍 Click Search"]
    st.markdown("\n".join([f"##### {i+1}. {item}" for i, item in enumerate(todo)]))
