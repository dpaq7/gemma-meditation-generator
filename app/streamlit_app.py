from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from meditation_ai.app import build_response

st.set_page_config(page_title="Gemma Meditation Generator", layout="centered")
st.title("Guided Meditation Generator")

prompt = st.text_area("Prompt", value="Write a grounding meditation for pre-meeting focus.")
language = st.selectbox("Language", ["English", "French", "Spanish"])
style = st.selectbox("Style", ["grounding", "sleep", "breathing", "gratitude"])
duration = st.slider("Duration", min_value=1, max_value=10, value=3)

if st.button("Generate"):
    st.write(build_response(prompt, language, style, duration))
