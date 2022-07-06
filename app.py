from turtle import width
import streamlit as st
from robin import *
import datetime
import pandas as pd
import pytz

st.header('Pigeonhole', anchor=None)
st.caption('Get a list of emails of people present in the office.')

robin_key = st.text_input('Enter Robin access token:')
if not robin_key:
  st.warning('Please input an access token.')
  st.stop()

locations = get_locations(robin_key)

col1, col2, col3 = st.columns(3)

with col1:
    selected_location = st.selectbox("Office", locations.keys())
    timezones = list(set([location['timezone'] for location in locations.values()]))
    default_ix = timezones.index(locations[selected_location]['timezone'])
    selected_timezone = st.selectbox('Timezone', timezones, index=default_ix)

with col2:
    date_from = st.date_input("Start date", datetime.date.today())
    time_from = st.time_input('Start time', datetime.time(8, 00))

with col3:
    date_to = st.date_input("End date", datetime.date.today())
    time_to = st.time_input('End time', datetime.time(18, 00))

tz = pytz.timezone(selected_timezone)
start = datetime.datetime.combine(date_from, time_from).replace(tzinfo=tz).isoformat()

end = datetime.datetime.combine(date_to, time_to).replace(tzinfo=tz).isoformat()

emails = get_emails(locations[selected_location]['id'], start, end, robin_key)

df = pd.DataFrame({'Email': emails})

styler = df.style.hide_index()
st.write(styler.to_html(), unsafe_allow_html=True)