from pathlib import Path
import streamlit as st
from PIL import Image

# --general directory settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "cv.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --site settings (https://digital-cv-marko-hentschel.onrender.com/)

PAGE_TITLE = "Digital CV | Marko Hentschel"
PAGE_ICON = ":page_facing_up:"
NAME = "Marko Hentschel"
DESCRIPTION = """
Senior Data Analyst
"""
EMAIL = "haufemarko@gmail.com"
EXTERNAL_LINKS = {
    "GitHub":"https://github.com/MarkoHentschel",
    "Linkedin":"https://www.linkedin.com/in/marko-hentschel-20785494/"
}
PROJECTS = {

}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --open assets

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, encoding="utf8", errors='ignore') as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)

# --page overview

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("", EMAIL)

# -- administrating external links

st.write("#") #-- "#" used to create space on the website
cols = st.columns(len(EXTERNAL_LINKS))
for index, (platform, link) in enumerate(EXTERNAL_LINKS.items()):
    cols[index].write(f"[{platform}]({link})")

# -- administrating experience

st.write("#") #-- "#" used to create space on the website
st.subheader("Experience and Qualifications")
st.write(
    """
    :arrow_forward: Multi-talented and data driven professional with an excellent reputation for resolving problems, improving stakeholder satisfaction and driving overall operational improvements. 
    :arrow_forward: Experienced in staff management and business intelligence development.
    """
)

# -- administrating skills

st.write("#") #-- "#" used to create space on the website
st.subheader("Hard skills")
st.write(
    """
    - :computer: Programming languages: Python, VBA, SQL (MySQL, MS, Exasol, Postgres) 
    - :bar_chart: Data visualization: Tableau, Power BI, MS Excel
    - :speaking_head_in_silhouette: Languages: German (native speaker), English (fluent)

    """
)

# -- administrating previous job experience

st.write("#") #-- "#" used to create space on the website
st.subheader("Work History")
st.write("---")


# --- current job

st.write("Senior Expert Entity Controlling | DHL Hub Leipzig GmbH")
st.write("05/2019 - Present")

st.write(
    """
    - Assisted in upper-level decision by creating comprehensive financial and operational performance reports.
    - Worked with executives as business partner to create the annual budget and tracked actual expenses against projected expenses.
    - Prepared financial reports and statements in accurate and timely manner.
    - Built library of models and reusable knowledge-base assets to produce consistent and streamlined business intelligence results.
    - Developed database objects, including tables, views and dynamic dashboards using SQL and MS-Office VBA.
    - Transformed project data requirements into project data models.

    """
)

# --- current job -1

st.write("Senior Business Manager | Tourini GmbH")
st.write("02/2018 - 04/2019")

st.write(
    """
    - Interfaced with a cross-functional team of business stakeholders (e.g. leadership, developers, inhouse users) to design a comprehensive list of required specifications for new products or services.
    - Assessed impact of current business processes on clients and internal stakeholders (e.g. customer support) to evaluate potential areas for improvement and driving results.
    - Performed competitor bench-marking analysis to identify potential product enhancements.
    - Mapped and documented process activities to identify shortfalls and options to rectify operational inefficiencies and offered recommendations for improvement.
    - Applied performance data to evaluate and improve operations, target to current business conditions and forecast needs.

    """
)

# --- current job -2

st.write("Head Of Performance Controlling | Invia Travel Germany")
st.write("07/2015 - 01/2018")

st.write(
    """
    - Monitored over 200 customer agents day-to-day activities.
    - Planned, designed and implemented diverse business intelligence solutions with the purpose of applying performance data to evaluate and improve operations.
    - Developed and managed dashboards using based on MS-SQL Server 2012 and MS-Office applications.
    - Created and implemented database designs and data models.
    - Mentored junior team members on workflows and procedures to maximize their contributions.

    """
)

