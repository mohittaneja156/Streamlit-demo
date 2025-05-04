# Import python packages
import streamlit as st
import snowflake.snowpark as snowpark
from snowflake.snowpark.context import get_active_session

# Write directly to the app
st.title(f"Example Streamlit App ")
st.write(
  """Importing Dataset
  """
)

# Get the current credentials
session = get_active_session()
session1 = snowpark.Session.builder.getOrCreate()
df = session.table("Demo").to_pandas()
st.title("Dataset from Snowflake")
st.dataframe(df)

