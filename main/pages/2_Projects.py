import streamlit as st 
import base64
from constant import info
from streamlit import container

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("main/style/style.css")

st.sidebar.markdown(info['Photo'],unsafe_allow_html=True)

st.title("🧑‍💻 Projects")


# Sample project data
projects = [
    {
        "title": "Movie Recommendation System",
        "image_url": "https://me.kribaat.com/project1_image.jpg",
        "description": "Description of Project 1",
        "project_link": "https://example.com/project1",
    },
    {
        "title": "Fake Face Detection",
        "image_url": "https://example.com/project2_image.jpg",
        "description": "Description of Project 2",
        "project_link": "https://example.com/project2",
    },
    {
        "title": "Project 3",
        "image_url": "https://example.com/project3_image.jpg",
        "description": "Description of Project 3",
        "project_link": "https://example.com/project3",
    },
    # Add more projects as needed
]

# Create a dynamic grid layout of cards
container = container()

# Define the number of columns per row
columns_per_row = 2

# Calculate the number of rows required
num_rows = len(projects) // columns_per_row + (len(projects) % columns_per_row > 0)

# Loop through each project and create a card for it
for row in range(num_rows):
    row_columns = st.columns(columns_per_row)
    for col, project_index in enumerate(range(row * columns_per_row, (row + 1) * columns_per_row)):
        if project_index < len(projects):
            project = projects[project_index]
            with row_columns[col]:
                st.write(f"## {project['title']}")
                st.image(project["image_url"], use_column_width=True)
                st.write(project["description"])
                if st.button(f"View Project {project['title']}"):
                    st.write(f"You clicked the 'View Project' button for {project['title']}")
