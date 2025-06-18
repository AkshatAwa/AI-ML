import streamlit as st
st.set_page_config(
    page_title="Bot 1 ",
    page_icon="💬",
)

st.header("🤖 Bot 1: ")
st.write("This bot is a chatbot")

st.subheader("Chat with Bot 1")

user_input = st.text_input("You:", "Hello Bot 1!")

if user_input:
    st.write(f"**Bot 1 (Echo):** You said '{user_input}'")
    if "hello" in user_input.lower():
        st.write("Bot 1: Hello there!")
    elif "how are you" in user_input.lower():
        st.write("Bot 1: I'm just a program, but I'm functioning well! How about you?")
    else:
        st.write("Bot 1: I'm not sure how to respond to that yet.")

st.markdown("---")
st.write("Future features: Integrate with an LLM, add memory, etc.")
