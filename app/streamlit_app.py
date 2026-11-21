
import streamlit as st
from ai_response import generate_answer

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Clinical Assistant",
    page_icon="🏥",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Main content */
.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 6rem;
}

/* Prevent horizontal overflow */
.stApp,
[data-testid="stMain"],
[data-testid="stMainBlockContainer"] {
    overflow-x: hidden;
}

/* Header */
.main-title {
    color: #0D9488;
    font-size: 36px;
    font-weight: 700;
}

.subtitle {
    color: #64748b;
    font-size: 17px;
}

/* Suggested question cards */
div.stButton > button {
    width: 100%;
    min-height: 58px;
    height: auto;
    white-space: normal;
    overflow-wrap: anywhere;
    border-radius: 12px;
    padding: 12px 16px;
    transition: 0.2s ease;
}

/* Hover */
div.stButton > button:hover {
    border-color: #0D9488;
    color: #0D9488;
}

/* Chat messages */
[data-testid="stChatMessage"] {
    border-radius: 14px;
    padding: 12px;
}

/* Chat input */
[data-testid="stChatInput"] {
    width: 100%;
}

/* Alerts */
[data-testid="stAlert"] {
    border-radius: 12px;
}

/* Responsive screen */
@media (max-width: 768px) {
    .main-title {
        font-size: 28px;
    }

    .subtitle {
        font-size: 15px;
    }

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
}

</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("## 🏥 AI Clinical")
    st.caption("Healthcare Information Assistant")

    st.divider()

    st.markdown("### 👤 Your role")

    role = st.selectbox(
        "Select your role",
        ["Patient", "Doctor", "Staff", "Admin"],
        label_visibility="collapsed"
    )

    st.divider()

    if st.button("🗑️ Clear conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    # Export conversation
    if st.session_state.messages:
        chat_export = "\n\n".join(
            f"{message['role'].upper()}:\n{message['content']}"
            for message in st.session_state.messages
        )

        st.download_button(
            label="📥 Download Conversation",
            data=chat_export,
            file_name="ai_clinical_chat.txt",
            mime="text/plain",
            use_container_width=True
        )

    st.markdown("### ℹ️ About")
    st.write(
        "Your AI assistant helps you find information "
        "from available clinic documents."
    )

    st.divider()

    st.caption("🔒 Responses are based on available clinic information.")

# ---------------- MAIN HEADER ----------------
st.markdown(
    '<div class="main-title">🏥 AI Clinical Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your intelligent healthcare information companion</div>',
    unsafe_allow_html=True
)

st.write("")

# ---------------- SAFETY NOTICE ----------------
st.info(
    "⚕️ This assistant provides clinic information only. "
    "It does not replace professional medical advice. "
    "For emergencies, seek immediate medical assistance."
)

# ---------------- ROLE-BASED SUGGESTED QUESTIONS ----------------

st.markdown("### 💡 Suggested questions")

role_questions = {
    "Patient": [
        "How can I manage my appointments?",
        "How can I reschedule an appointment?",
        "What services does the clinic provide?",
        "How can I contact clinic staff?"
    ],

    "Doctor": [
        "What are my responsibilities as a doctor?",
        "How can I view my appointments?",
        "What clinical information is available?",
        "What tasks can doctors perform?"
    ],

    "Staff": [
        "How can I register a patient?",
        "How can I manage appointments?",
        "How can I handle billing queries?",
        "What are the responsibilities of clinic staff?"
    ],

    "Admin": [
        "What are the admin responsibilities?",
        "How can I manage user accounts?",
        "What operational reports are available?",
        "What administrative tasks can I perform?"
    ]
}

suggestions = role_questions[role]

col1, col2 = st.columns(2)

for i, suggestion in enumerate(suggestions):
    target_col = col1 if i % 2 == 0 else col2

    with target_col:
        if st.button(
            suggestion,
            key=f"{role}_suggestion_{i}",
            use_container_width=True
        ):
            st.session_state.pending_question = suggestion
            st.rerun()
            
# ---------------- CHAT HISTORY ----------------
st.markdown("---")
st.markdown("### 💬 Conversation")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------- QUESTION HANDLING ----------------
pending_question = st.session_state.pop("pending_question", None)

chat_question = st.chat_input("Ask anything about clinic services...")

question = pending_question or chat_question

if question:

    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("AI is thinking..."):
            try:
                answer = generate_answer(question, role.lower())
            except Exception:
                answer = (
                    "I'm sorry, I'm unable to process your request right now. "
                    "Please try again in a moment."
                )
                st.warning("AI service temporarily unavailable.")

        st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
