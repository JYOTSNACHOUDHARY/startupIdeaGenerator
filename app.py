import streamlit as st
from orchestrator.graph import graph
from typing import List

st.set_page_config(page_title="Startup Idea Validator", layout="centered")
st.title("🚀 Startup Idea Validator")
st.markdown("Generate and validate startup ideas using LangGraph workflows powered by OpenAI LLM.")


with st.form(key="idea_form"):
    domain = st.text_input("Example domains: education, healthcare, fitness, etc.", placeholder="Type a domain here...")
    submit = st.form_submit_button("💡 Generate & Validate Ideas")

if submit:
    if not domain.strip():
        st.warning("Please enter a domain to proceed.")
    else:
        with st.spinner("🔄 Running LLM validation process..."):
            st.markdown("---")
            st.markdown(f"### ✅ Startup Ideas for domain: `{domain}`")
            for event in graph.stream({"user_input": domain}):
                for value in event.values():
                    msg = value["messages"]
                    if hasattr(msg, "content"):
                        st.markdown("**🛠 Tool Output**")
                        st.write(msg.content)
                    else:
                        st.write(msg)
            st.success("✅ Idea generation and validation complete.")

