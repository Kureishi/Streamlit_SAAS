import streamlit as st
from st_paywall import add_auth

st.set_page_config(layout='wide')
st.title('Best SaaS App!')

# conduct authentication -> turn app into SaaS -> adds login button automatically
add_auth(required=True)

# Only after Authentication and Subscription -> user sees following
# Email and subscription status stored in session state
st.write(f"Subscription Status: {st.session_state.user_subscribed}")
st.write('Congrats! All set and subscribed.')
st.write(f"BTW, email used is {st.session_state.email}")