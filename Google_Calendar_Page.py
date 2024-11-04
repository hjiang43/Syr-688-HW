import streamlit as st
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
CREDENTIALS_FILE = 'credential/client_secret_345904176433-l667urcgvugnrhr7be73ln2nkogrp5a9.apps.googleusercontent.com.json'  # Replace with your credentials file path

def run_google_calendar_page():
    st.title('Google Calendar Page')
    
    if 'credentials' not in st.session_state:
        st.session_state['credentials'] = None

    def authenticate():
        flow = InstalledAppFlow.from_client_secrets_file(
            CREDENTIALS_FILE, SCOPES
        )
        credentials = flow.run_local_server(port=0)
        st.session_state['credentials'] = credentials

    if st.session_state['credentials'] is None:
        st.button('Authenticate with Google', on_click=authenticate)
    else:
        st.write('Authenticated successfully!')
        creds = st.session_state['credentials']
        
        # Create a Google Calendar service
        service = build('calendar', 'v3', credentials=creds)

        # Fetch upcoming events
        events_result = service.events().list(
            calendarId='primary', maxResults=10, singleEvents=True,
            orderBy='startTime'
        ).execute()
        events = events_result.get('items', [])

        if not events:
            st.write('No upcoming events found.')
        else:
            st.write('Upcoming events:')
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                st.write(f"{start}: {event['summary']}")
