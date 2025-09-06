import streamlit as st
import os
from sentiment_llm import analyze_review  

st.set_page_config(
    page_title="Movie Review Sentiment Marker",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Review Sentiment Marker")
st.markdown("Paste a movie review below and click **Analyze** to see its sentiment.")

# Input box
review_text = st.text_area("Enter a movie review:", height=200)

if st.button("Analyze"):
    if review_text.strip():
        try:
            result = analyze_review(review_text)

            if isinstance(result, list) and "args" in result[0]:
                result = result[0]["args"]

            st.subheader("Result")

            st.markdown(f"**Label:** {result['label']}")
            st.markdown(f"**Confidence:** {result['confidence']:.2f}")
            st.markdown(f"**Explanation:** {result['explanation']}")

            if result.get("evident_phrases"):
                st.markdown("**Key Phrases:**")
                evident_phrases = result["evident_phrases"]
                for i in range(len(evident_phrases)):
                    evident_phrases[i]= str(i+1)+' '+evident_phrases[i]
                st.write("<br>".join(evident_phrases), unsafe_allow_html=True)

        except Exception as e:
            st.error(f"⚠️ Error analyzing review: {e}")
    else:
        st.warning("Please enter a review before clicking Analyze.")
