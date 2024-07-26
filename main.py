"""
main.py

This module sets up the Streamlit application for uploading a PDF and inputting a query.
"""

import streamlit as st

from src.app import process_query


def main():
    st.title("Retrieval-Augmented Generation (RAG) Agent")

    if "pdf_file" not in st.session_state:
        st.session_state.pdf_file = None
    if "query" not in st.session_state:
        st.session_state.query = ""

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        st.session_state.pdf_file = uploaded_file

    query = st.text_input("Enter your query", value=st.session_state.query)

    if query:
        st.session_state.query = query

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Submit"):
            if st.session_state.pdf_file or st.session_state.query:
                response = process_query(
                    st.session_state.pdf_file, st.session_state.query
                )
                st.write("Response:", response)
            else:
                st.write("Please upload a PDF file and enter a query.")

    with col2:
        if st.button("Clear"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.session_state.pdf_file = None
            st.session_state.query = ""
            st.cache_data.clear()
            st.rerun()


if __name__ == "__main__":
    main()
