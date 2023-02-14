import streamlit as st
import pandas

st.set_page_config(layout="wide")
st.header("The best company")

description = """
Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam 
eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo. Nemo enim ipsam 
voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos, qui ratione 
voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum, quia dolor sit, amet, consectetur, adipisci 
velit, sed quia non numquam eius modi tempora incidunt, ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim 
ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi 
consequatur? Quis autem vel eum iure reprehenderit, qui in ea voluptate velit esse, quam nihil molestiae consequatur, 
vel illum, qui dolorem eum fugiat, quo voluptas nulla pariatur?
"""

st.text(description)
st.subheader("Our team")

left_column, empty_column1, middle_column, empty_column2, right_column = st.columns([3, 1, 3, 1, 3])

data_file = pandas.read_csv("data.csv")

for index, row in data_file.iterrows():
    row["first name"] = row["first name"].title()
    row["last name"] = row["last name"].title()

with left_column:
    for index, row in data_file[:4].iterrows():
        st.subheader(f"{row['first name']} {row['last name']}")
        st.write(row["role"])
        st.image(f"images/{row['image']}")

with middle_column:
    for index, row in data_file[4:8].iterrows():
        st.subheader(f"{row['first name']} {row['last name']}")
        st.write(row["role"])
        st.image(f"images/{row['image']}")

with right_column:
    for index, row in data_file[8:].iterrows():
        st.subheader(f"{row['first name']} {row['last name']}")
        st.write(row["role"])
        st.image(f"images/{row['image']}")
