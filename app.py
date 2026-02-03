import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Nqubeko Mnyandu - Researcher Profile",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS with University of Zululand colors
st.markdown("""
<style>
    /* Main styling */
    .main-header {
        font-size: 2.8rem;
        color: #2E86AB;
        text-align: center;
        margin-bottom: 0.5rem;
        font-weight: 700;
    }
    
    .sub-header {
        font-size: 1.5rem;
        color: #A23B72;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 600;
    }
    
    .unizulu-badge {
        background: linear-gradient(90deg, #FFCD00, #000000);
        color: white;
        padding: 8px 20px;
        border-radius: 25px;
        display: inline-block;
        font-weight: bold;
        margin: 10px 0;
    }
    
    /* Card styling */
    .card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border-left: 5px solid #FFCD00;
        transition: transform 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    
    /* Color themes */
    .unizulu-yellow {
        color: #FFCD00;
        font-weight: bold;
    }
    
    .unizulu-black {
        color: #000000;
        font-weight: bold;
    }
    
    .section-title {
        color: #2E86AB;
        border-bottom: 3px solid #FFCD00;
        padding-bottom: 0.5rem;
        margin-bottom: 1.5rem;
        font-size: 1.8rem;
    }
    
    .highlight {
        background-color: #FFCD00;
        padding: 2px 8px;
        border-radius: 4px;
        color: black;
        font-weight: 600;
    }
    
    /* Progress bar customization */
    .stProgress > div > div > div > div {
        background-color: #FFCD00;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #FFCD00;
        color: black;
        font-weight: bold;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        background-color: #000000;
        color: #FFCD00;
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding-top: 1rem;
        border-top: 2px solid #FFCD00;
        color: #666;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<h1 class="main-header">Nqubeko Mnyandu</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="sub-header">Researcher & Environmental Scientist</h3>', unsafe_allow_html=True)

# University Badge
st.markdown('<div style="text-align: center; margin-bottom: 2rem;">', unsafe_allow_html=True)
st.markdown('<span class="unizulu-badge">🏛️ University of Zululand | KwaDlangezwa Campus</span>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Profile columns
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        width=180,
        caption="Nqubeko Mnyandu - Research Profile"
    )

# About Section
st.markdown("## 🎓 About Me")
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("""
I am a passionate **Black South African researcher** and **Honours student** at the **<span class='unizulu-yellow'>University of Zululand</span>**, 
dedicated to advancing scientific knowledge that addresses local and global challenges. My research focuses on 
interdisciplinary approaches to environmental sustainability, community health, and technological innovation.

**Research Philosophy:** Combining traditional knowledge with modern scientific methods to create 
impactful solutions for rural communities in KwaZulu-Natal.
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Research Interests
st.markdown("## 🔬 Research Focus Areas")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🌱 Environmental Sustainability")
    st.markdown("""
    • Soil conservation practices
    • Water resource management
    • Climate change adaptation
    • Sustainable agriculture
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 💻 Science & Technology")
    st.markdown("""
    • Data analytics for development
    • GIS mapping applications
    • Digital tools for rural areas
    • Scientific computing
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🏥 Community Health")
    st.markdown("""
    • Public health interventions
    • Traditional medicine research
    • Health data analysis
    • Community-based studies
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Academic Profile with Tabs
st.markdown("## 📚 Academic Profile")

tab1, tab2, tab3, tab4 = st.tabs(["🎓 Education", "🚀 Current Research", "📊 Skills", "📄 Publications"])

with tab1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### University of Zululand")
    st.markdown("""
    **BSc Honours in Environmental Science** (2024-Present)
    - Specialization: Environmental Management
    - Supervisor: Dr. S. Ndlovu
    - GPA: 3.8/4.0
    
    **BSc in Life Sciences** (2020-2023)
    - Major: Environmental Science
    - Minor: Chemistry
    - Graduated Cum Laude
    
    **Awards & Honors:**
    • Dean's List Award (2022, 2023)
    • Vice-Chancellor's Scholarship Recipient
    • NRF Honors Scholarship
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Active Research Projects")
    st.markdown("""
    **1. Sustainable Soil Management in Rural KZN**
    - **Funding:** National Research Foundation (NRF)
    - **Duration:** 2024-2025
    - **Focus:** Assessing soil degradation and conservation methods
    
    **2. Water Quality Monitoring System Development**
    - **Collaboration:** UNIZULU Computer Science Department
    - **Tools:** IoT sensors, Python data analysis
    - **Goal:** Real-time water quality tracking
    
    **3. Traditional Medicine Database Project**
    - **Community-based research**
    - **Partners:** Local healers association
    - **Output:** Digital catalog of medicinal plants
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Technical & Research Skills")
    
    st.markdown("**Laboratory Techniques**")
    st.progress(0.85)
    st.caption("Soil analysis, Water testing, Microscopy")
    
    st.markdown("**Field Research**")
    st.progress(0.90)
    st.caption("Sample collection, Community surveys, GIS mapping")
    
    st.markdown("**Data Analysis**")
    st.progress(0.80)
    st.caption("Python, R, SPSS, Excel")
    
    st.markdown("**Scientific Writing**")
    st.progress(0.88)
    st.caption("Research papers, Reports, Proposals")
    
    st.markdown("**Software & Tools**")
    st.markdown("""
    • ArcGIS • QGIS • Python (Pandas, NumPy) • R Studio
    • Microsoft Office • Google Earth • SPSS
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with tab4:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Publications & Presentations")
    st.markdown("""
    **Journal Articles:**
    - **Mnyandu, N.**, & Ndlovu, S. (2024). "Soil Conservation Methods in Northern KZN"  
      *South African Journal of Environmental Science* (Under Review)
    
    **Conference Presentations:**
    - "Digital Tools for Sustainable Farming"  
      *SA Young Scientists Conference, Durban 2023*
    - "Community-Based Environmental Monitoring"  
      *UNIZULU Research Symposium, 2023*
    
    **Research Reports:**
    - Water Quality Assessment in uMhlathuze River (2023)
    - Traditional Medicine Survey in Nongoma (2022)
    """)
    
    # Add a download button for CV
    st.markdown("---")
    st.markdown("### 📥 Download Research Profile")
    if st.button("Download Full CV (PDF)"):
        st.info("CV download feature would be implemented with actual PDF file")
    st.markdown('</div>', unsafe_allow_html=True)

# Contact Section
st.markdown("## 📞 Contact & Collaboration")
contact_col1, contact_col2 = st.columns(2)

with contact_col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Contact Information")
    st.markdown("""
    **📧 Email:** 
    - nqubeko.mnyandu@unizulu.ac.za
    - nqubeko.research@gmail.com
    
    **📱 Phone:** +27 78 123 4567
    
    **🏢 Office:** 
    Environmental Science Department
    University of Zululand
    KwaDlangezwa, 3886
    South Africa
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with contact_col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Research Profiles & Links")
    st.markdown("""
    **Academic Profiles:**
    • [ORCID Profile](https://orcid.org/0000-0000-0000-0000)
    • [Google Scholar](https://scholar.google.com)
    • [ResearchGate](https://researchgate.net/profile/Nqubeko-Mnyandu)
    
    **University Links:**
    • [UNIZULU Website](https://www.unizulu.ac.za)
    • [Environmental Science Department](https://www.unizulu.ac.za/environmental-science)
    
    **Social Media:**
    • [LinkedIn](https://linkedin.com/in/nqubeko-mnyandu)
    • [Twitter/X](https://twitter.com/nqubeko_research)
    """)
    
    # Contact form
    st.markdown("---")
    st.markdown("### 📝 Send a Message")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success("Message sent! (This is a demo - in production, this would connect to an email service)")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(f"""
<div class="footer">
    <p>© {datetime.now().year} Nqubeko Mnyandu | University of Zululand Research Profile</p>
    <p><em>"Advancing knowledge for sustainable development in South Africa and beyond"</em></p>
    <p style="font-size: 0.8rem; color: #888;">This profile is updated regularly | Last updated: {datetime.now().strftime('%B %Y')}</p>
</div>
""", unsafe_allow_html=True)

# Add some interactivity
with st.sidebar:
    st.markdown("## 🔍 Quick Links")
    if st.button("View Research Gallery"):
        st.info("Research photos and data visualizations would appear here")
    
    if st.button("Download Publications"):
        st.info("PDF collection would be available for download")
    
    st.markdown("---")
    st.markdown("### 🎯 Research Metrics")
    st.metric("Projects Active", "3")
    st.metric("Publications", "2+")
    st.metric("Conference Talks", "2")
    st.metric("Research Impact", "Community-focused")
    
    st.markdown("---")
    st.markdown("### 🔔 Updates")
    st.info("""
    **Next Presentation:**
    UNIZULU Annual Research Conference
    October 2024
    
    **Current Focus:**
    Data analysis for soil quality project
    """)
