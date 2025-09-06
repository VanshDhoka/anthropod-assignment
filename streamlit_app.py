import streamlit as st
import os
from sentiment_llm import analyze_review
import json 

GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY")

st.set_page_config(
    page_title="Movie Review Sentiment Marker",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Review Sentiment Marker")
st.markdown("Paste a movie review below and click **Analyze** to see its sentiment.")

# Cost Control(using caching to json file)
Cache_File = ".review_cache.json"
if os.path.exists(Cache_File):
    with open(Cache_File, "r") as f:
        review_cache = json.load(f)
else:
    review_cache = {}

def analyze_review_cached(review):
    if review in review_cache:
        return review_cache[review]

    result = analyze_review(review)

    if isinstance(result, list) and "args" in result[0]:
        result = result[0]["args"]

    review_cache[review] = result
    with open(Cache_File, "w") as f:
        json.dump(review_cache, f, indent=2)

    return result

review_text = st.text_area("Enter a movie review:", height=200)

if st.button("Analyze"):
    if review_text.strip():
        try:
            result = analyze_review_cached(review_text)
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
