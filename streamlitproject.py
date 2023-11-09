
import streamlit as st

from streamlit_chat import message as st_message

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://images.unsplash.com/photo-1544991936-9464fa9919d2?auto=format&fit=crop&q=80&w=1470&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
background-size: 100%;
 background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
</style>
"""
st.markdown("<h1 style='text-align: center; color: black; font-size: 55px;'>Welcome To GB-medibot</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: black;' class='subtitle'>Please Enter Your Symptoms!</h2>", unsafe_allow_html=True)
st.markdown(page_bg_img, unsafe_allow_html=True)

if "message" not in st.session_state:
    st.session_state.messages = []
   
    
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
     st.markdown(message["content"])

def main():

    # Initialize chat history as an empty list
    chat_history = []

    # User input text box
    user_input = st.text_input("Enter your message:")

    # Store user input in history on button click
    
    if st.button("Send"):
        chat_history.append({"user": user_input, "bot": "Response from the bot"})
      
    # Display chat history
    st.subheader("Chat History")
    for chat in chat_history:
        st.write(f"User: {chat['user']}")
        st.write(f"Bot: {chat['bot']}")
        st.write("----")

if __name__ == "__main__":
    main()
