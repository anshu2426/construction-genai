import streamlit as st
from vector_db import build_vector_db, search_vector_db
from llm_engine import generate_report

from fpdf import FPDF
from io import BytesIO
from datetime import datetime

# ------------------ Load Knowledge Base ------------------

with open("data/construction_docs.txt") as f:
    texts = f.readlines()

tfidf_matrix = build_vector_db(texts)

# ------------------ Streamlit UI ------------------

st.set_page_config(
    page_title="Construction Content Generator",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
    }
    .stTextInput > div > div > input {
        border-radius: 8px;
        padding: 12px;
        border: 2px solid #e0e0e0;
    }
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
    }
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 8px;
        padding: 12px 24px;
        font-weight: 600;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }
    .info-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
        color: #333;
    }
    .info-card strong {
        color: #667eea;
    }
    .success-box {
        background: #d4edda;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #28a745;
    }
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
<div class="main-header">
    <h1 style="margin: 0; font-size: 2.5rem;">🏗️ Construction Content Generator</h1>
    <p style="margin: 0.5rem 0 0 0; font-size: 1.1rem; opacity: 0.9;">
        Generate professional construction site reports using AI-powered technology
    </p>
</div>
""", unsafe_allow_html=True)

# Main Content
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 📝 Project Details")
    topic = st.text_input(
        "Enter construction topic",
        placeholder="e.g., Foundation work, Electrical installation, Safety inspection...",
        help="Describe the construction activity or topic for the report"
    )

with col2:
    st.markdown("### ℹ️ Quick Info")
    st.markdown("""
    <div class="info-card">
        <strong>Features:</strong>
        <ul style="margin: 0.5rem 0 0 1.5rem;">
            <li>AI-powered content generation</li>
            <li>Professional PDF reports</li>
            <li>Instant download</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ------------------ PDF Builder (fpdf2) ------------------

def create_pdf(report_text, topic):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=10)
    pdf.set_margins(10, 10, 10)
    pdf.add_page()

    # Main Title
    pdf.set_font("Helvetica", "B", 18)
    pdf.cell(190, 12, "Construction Site Report", ln=True, align="C")

    pdf.ln(4)

    # Project + Date
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(190, 8, f"Project Name: {topic}", ln=True)
    pdf.cell(190, 8, f"Date: {datetime.now().strftime('%d %B %Y')}", ln=True)

    pdf.ln(6)

    # Known subheadings to bold
    headings = [
        "Project Overview",
        "Work Executed",
        "Manpower & Machinery",
        "Safety Observations",
        "Issues & Remarks"
    ]

    # Clean markdown **
    report_text = report_text.replace("**", "")

    for line in report_text.split("\n"):

        clean_line = line.strip()

        if not clean_line:
            pdf.ln(2)
            continue

        # If line is a heading
        if clean_line in headings:
            pdf.set_font("Helvetica", "B", 13)
            pdf.cell(190, 9, clean_line, ln=True)
            pdf.ln(1)

        else:
            pdf.set_font("Helvetica", size=11)
            pdf.multi_cell(190, 7, clean_line)

    buffer = BytesIO()
    pdf_output = pdf.output(dest="S")
    if isinstance(pdf_output, str):
        buffer.write(pdf_output.encode('latin1'))
    else:
        buffer.write(pdf_output)
    buffer.seek(0)

    return buffer

# ------------------ Generate & Download ------------------

st.markdown("---")

if st.button("🚀 Generate Site Report", use_container_width=True, type="primary"):

    if not topic:
        st.error("⚠️ Please enter a construction topic first!")
    else:
        # Show progress
        with st.spinner("🔄 Analyzing topic and searching knowledge base..."):
            context = " ".join(search_vector_db(topic, texts, tfidf_matrix))

        with st.spinner("🤖 Generating AI-powered report..."):
            report = generate_report(topic, context)

        # Success message
        st.markdown("""
        <div class="success-box">
            <strong>✅ Report generated successfully!</strong>
        </div>
        """, unsafe_allow_html=True)

        # Generate PDF
        pdf_file = create_pdf(report, topic)

        # Download section
        st.markdown("### 📥 Download Your Report")
        st.download_button(
            label="📄 Download PDF Report",
            data=pdf_file,
            file_name=f"site_report_{datetime.now().strftime('%Y%m%d')}.pdf",
            mime="application/pdf",
            use_container_width=True
        )

        # Preview section
        with st.expander("👁️ Preview Report Content"):
            st.markdown(report)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem 0;">
    <p>💡 <strong>Tip:</strong> Be specific with your topic for better results</p>
    <p style="font-size: 0.9rem; margin-top: 0.5rem;">Powered by AI | Built with Streamlit</p>
</div>
""", unsafe_allow_html=True)
