import streamlit as st
import requests
import os


st.set_page_config(
    page_title="AI Resume Matcher",
    layout="centered"
)

st.title("AI Resume Matcher")

st.write(
    "Upload your resume and paste the job description."
)

# Resume Upload
uploaded_resume = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# JD Input
job_description = st.text_area(
    "Paste Job Description",
    height=250
)

# Submit Button
if st.button("Analyze Resume"):

    if uploaded_resume is None:

        st.error("Please upload a resume.")

    elif not job_description.strip():

        st.error(
            "Please paste job description."
        )

    else:

        with st.spinner(
            "Analyzing resume..."
        ):

            files = {
                "resume": (
                    uploaded_resume.name,
                    uploaded_resume,
                    "application/pdf"
                )
            }

            data = {
                "job_description":
                    job_description
            }

            try:

                response = requests.post(
                    f"{BACKEND_URL}/run-workflow",
                    files=files,
                    data=data
                )

                if response.status_code == 200:

                    result = response.json()

                    st.success(
                        "Analysis Complete!"
                    )

                    st.subheader(
                        "Semantic Match Score"
                    )

                    st.metric(
                        label="Match Score",
                        value=f"{result['semantic_match_score']}%"
                    )

                    analysis = result[
                        "analysis"
                    ]

                    st.subheader(
                        "Strengths"
                    )

                    for item in analysis[
                        "strengths"
                    ]:
                        st.write(f"• {item}")

                    st.subheader(
                        "Weaknesses"
                    )

                    for item in analysis[
                        "weaknesses"
                    ]:
                        st.write(f"• {item}")

                    st.subheader(
                        "Recommendations"
                    )

                    for item in analysis[
                        "recommendations"
                    ]:
                        st.write(f"• {item}")

                else:

                    st.error(response.text)

            except Exception as e:

                st.error(str(e))