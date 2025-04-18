
import streamlit as st
from generator.rag_pipeline import get_fact_check_response

st.set_page_config(page_title="AI Fact Checker (Live Mode)", layout="centered")

st.title("🔍 AI Fact Checker using RAG (Live Mode)")
st.markdown("Enter a claim below. The app will fetch live data from Wikipedia and News sources, then generate a verdict.")

query = st.text_area("✍️ Enter your claim here:")

if st.button("Check This Claim"):
    if query.strip():
        with st.spinner("Fetching evidence & analyzing..."):
            result = get_fact_check_response(query)

        st.success("✅ Analysis Complete!")

        st.subheader("📘 Verdict:")
        st.markdown(f"### {result['verdict']}")
        
        st.subheader("🧠 Summary:")
        st.write(result['summary'])

        st.subheader("🔗 Sources:")
        for src in result['sources']:
            st.markdown(f"- {src}")

        st.subheader("📊 Confidence:")
        st.progress(result['confidence'])

st.markdown("---")
st.markdown("<div style='text-align:center; color: grey;'>Built by LP and VR</div>", unsafe_allow_html=True)
