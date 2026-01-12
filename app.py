import streamlit as st
from scam_classifier import build_scam_classifier_chain
from internet_search import internet_search


st.set_page_config(
    page_title="ScamGuard AI",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ ScamGuard AI")
st.subheader("Detect scam messages using Generative AI")

st.write(
    "Paste a message below to check whether it is a scam, not a scam, or uncertain."
)

user_input = st.text_area(
    "Enter message",
    height=150,
    placeholder="Example: Your bank account will be suspended. Click this link immediately."
)

if st.button("Analyze Message"):
    if not user_input.strip():
        st.warning("Please enter a message.")
    else:
        with st.spinner("Analyzing..."):
            chain = build_scam_classifier_chain()
            result = chain.invoke(
                {"user_message": user_input}
            )

        st.success("Analysis Complete")

        st.markdown("### 🔍 Classification")
        st.write(result.classification)

        st.markdown("### intent")
        st.write(result.intent_type)

        st.markdown("### 🧠 Reasoning")
        st.write(result.reasoning)


        news_limit = st.slider(
          "Number of related scam news articles",
          min_value=1,
          max_value=10,
          value=3
        )

        st.markdown("### 📰 Ongoing Scam Alerts")

        with st.spinner("Fetching latest scam news..."):
            news_response = internet_search(max_results=news_limit)
            news_items = news_response.get("results", [])

        if not news_items:
            st.write("No recent scam news found.")
        else:
            for item in news_items:
                st.markdown(
                    f"- **{item.get('title', 'No title')}**  \n"
                    f"{item.get('url', '')}"
                )



        