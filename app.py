import streamlit as st
from datetime import datetime
from RAG_pipeline import vector_store, llm

st.set_page_config(
    page_title="PharmaBot",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>

/* Hide sidebar */
[data-testid="stSidebar"],
[data-testid="collapsedControl"]{
    display:none !important;
}

/* App background */
.stApp{
    background:#f5f7fb;
}

/* Hero Banner */
.hero{
    background:linear-gradient(
    90deg,
    #2563eb 0%,
    #14b8a6 50%,
    #2563eb 100%);
    padding:30px;
    border-radius:18px;
    color:white;
    margin-bottom:22px;
    box-shadow:0 10px 30px rgba(0,0,0,.12);
}

.hero h1{
    margin:0;
    font-size:2.3rem;
    font-weight:700;
}

.hero p{
    margin-top:8px;
    margin-bottom:0;
    opacity:.95;
    font-size:1rem;
}

/* Chat bubbles */
[data-testid="stChatMessage"]{
    border-radius:28px !important;
    padding:14px 18px !important;
    margin-bottom:12px;
    max-width:85%;
    box-shadow:0 3px 10px rgba(0,0,0,.04);
}

/* Assistant bubble */
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]){
    background:#B8E0F2 !important;
    border:1px solid #93c5fd !important;
}

/* User bubble */
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]){
    background:#ffffff !important;
    border:1px solid #e5e7eb !important;
    margin-left:auto;
}

/* Input */
[data-testid="stChatInput"]{
    border-radius:14px;
}

/* Expander */
.streamlit-expanderHeader{
    font-weight:600;
}

/* Clear button */
button[kind="secondary"]{
    background:#FB7185 !important;
    color:white !important;
    border:none !important;
    border-radius:10px !important;
    font-weight:600 !important;
}

button[kind="secondary"]:hover{
    background:#F43F5E !important;
}

/* Footer */
.footer{
    text-align:center;
    color:#6b7280;
    font-size:.85rem;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)


# ---------- Hero Banner ----------
st.markdown("""
<div class="hero">
    <h1>PharmaBot</h1>
    <p>Your AI assistant for medicines, pharmacy products and pharmacy policies.</p>
</div>
""", unsafe_allow_html=True)


# ---------- Clear Button ----------
_, right = st.columns([5,1])

with right:
    st.write("")
    if st.button("Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


st.divider()


# ---------- Chat History ----------
if "messages" not in st.session_state:
    st.session_state.messages = []


if not st.session_state.messages:
    st.info(
        "Ask questions about medicines, products, pharmacy policies or follow-up questions."
    )


for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])
        st.caption(m["time"])


# ---------- Chat Input ----------
q = st.chat_input("Ask a question...")


if q:

    t = datetime.now().strftime("%H:%M")

    st.session_state.messages.append({
        "role":"user",
        "content":q,
        "time":t
    })


    with st.chat_message("user"):
        st.markdown(q)
        st.caption(t)


    with st.spinner("Searching the knowledge base..."):

        chat_history = "\n".join(
            f"{m['role']}: {m['content']}"
            for m in st.session_state.messages[-6:]
        )


        results = vector_store.similarity_search_with_score(q, k=3)


        ctx = "\n\n".join(
            doc.page_content
            for doc, score in results
        )


        prompt = f"""
You are a pharmacy customer support assistant.

Your role is to assist customers in a friendly, professional, and concise manner.

Instructions:
- Use the conversation history to understand follow-up questions.
- If the user greets you, respond naturally.
- Answer pharmacy-related questions ONLY using the provided context.
- Do not use outside knowledge or make assumptions.
- If information is unavailable in the context, politely say you couldn't find it.
- Do not mention the context, retrieved documents, or that you are an AI.
- Do not invent medicine names, prices, policies, or services.

Context:
{ctx}

Conversation History:
{chat_history}

Customer Question:
{q}

Answer:
"""

        response = llm.invoke(prompt)
        
        ans = response.content
        
        src = [
            doc.page_content[:250] + "..."
            for doc, score in results
        ]


    with st.chat_message("assistant"):

        st.markdown(ans)

        if src:
            with st.expander("Retrieved Information"):
                for i, s in enumerate(src, 1):
                    st.markdown(f"**Chunk {i}**")
                    st.write(s)

        st.caption(datetime.now().strftime("%H:%M"))


    st.session_state.messages.append({
        "role":"assistant",
        "content":ans,
        "time":datetime.now().strftime("%H:%M")
    })


# ---------- Footer ----------
st.markdown(
    """
    <div class="footer">
        Powered by Gemini • LangChain • FAISS
    </div>
    """,
    unsafe_allow_html=True
)