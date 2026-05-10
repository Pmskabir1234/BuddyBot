import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage



load_dotenv()

st.set_page_config(page_title='Buddy Bot', page_icon='🤖')
# st.header("Buddy Bot")
# st.subheader("A general conversational chatbot made in langchain")
import streamlit as st

# Fixed header CSS
st.markdown("""
<style>
.fixed-header {
    position: fixed;
    top: 2%;
    left: 0;
    width: 100%;
    background-color: #0e1117;
    padding: 1rem;
    z-index: 9999;
    border-bottom: 1px solid #333;
}

/* Prevent content from hiding under header */
.block-container {
    padding-top: 120px;
}
</style>
""", unsafe_allow_html=True)

# Fixed header
st.markdown("""
<div class="fixed-header">
    <h1>Buddy Bot</h1>
    <p>A general conversational chatbot made in LangChain</p>
</div>
""", unsafe_allow_html=True)

llm = HuggingFaceEndpoint(
    model='google/gemma-4-31B-it',
    task='text-generation',
    temperature=0.5,
    max_new_tokens=1000
)



model = ChatHuggingFace(llm=llm)

# to persist the chat history
if 'messages' not in st.session_state:
    st.session_state.messages = [
        SystemMessage('You are helpful assistant')
    ]

# display previous user messages
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("You"):
            st.write(msg.content)

# display previous Ai messages
for msg in st.session_state.messages:
    if isinstance(msg, AIMessage):
        with st.chat_message("Buddy"):
            st.write(msg.content)

user_input = st.chat_input("Ask anything...")

if user_input:
    with st.chat_message("You"):
        st.write(user_input)
    
    st.session_state.messages.append(
        HumanMessage(content=user_input)
    )
    res = model.invoke(st.session_state.messages)
    with st.chat_message("Buddy"):
        st.write(res.content)
    
    st.session_state.messages.append(
        AIMessage(content=res.content)
    )
    