import os
import json
import streamlit as st
from PIL import Image

# set webpage title and layout
st.set_page_config(
    page_title = "JWST Telemetry and Image Dashboard",
    page_icon = "✰",
    layout = "wide"
)
# custom CSS styling 
st.markdown("""
    <style>
    /* Main Background and Text Colors */
    .stApp {
        background-color: #0B0E14;
        color: #E6EDF3;
    }
    /* Metric Card Styling */
    [data-testid="stMetric"] {
        background-color: #161B22;
        padding: 15px;
        border-radius: 1px;
        border: 1px solid #30363D;
    }
    [data-testid="stMetricValue"] {
        color: #58A6FF;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)
# paths to generated assets
json_path = "web_assets/data.json"
# image_path = "web_assets/target_image.png"

# check if web assets exist
if not os.path.exists(json_path):
    st.error("Web Assets not found. Please run 'data_analysis.ipynb' first.")
else:
    # load JSON metadata
    with open(json_path, "r") as f:
        all_metadata = json.load(f)
    if isinstance(all_metadata, dict):
        all_metadata = [all_metadata]
    if "image_index" not in st.session_state:
        st.session_state.image_index = 0
    if st.session_state.image_index >= len(all_metadata):
        st.session_state,image_index = 0
    # sidebar with target selection dropdown
    st.sidebar.title("Target Selection")
    # options for dropdown
    options = [
        f"{item.get('TARGNAME', 'Unknown Target')} | ({item.get('FILE_NAME', 'Unknown File')})" 
        for item in all_metadata
    ]    

    # callback when user changes dropdown manually
    def on_dropdown_change():
        st.session_state.image_index = options.index(st.session_state.selected_option_key)

    # sidebar selectbox sunced with session state
    st.sidebar.selectbox("Choose Observation:", options, index = st.session_state.image_index, key = "selected_option_key", on_change = on_dropdown_change)
    
    # selected_option = st.sidebar.selectbox("Choose Observation:", options)
    # selected_index = options.index(selected_option)
    
    metadata = all_metadata[st.session_state.image_index]

    # sidebar with raw JSON view
    st.sidebar.subheader("Raw JSON Metadata")
    st.sidebar.json(metadata)

    # main dashboard UI
    st.title("🔭 JWST Automated Main Dashboard")
    st.caption("AI-Powered Metadata Extraction and Image Visualization using Gemini 2.5 Flash Model")
    st.markdown("---")
    # creating two columns, left for celestial images, right for the metadata (instrument type, filter, etc)
    col1, col2 = st.columns([1, 1], gap = "large")

    with col1:
        st.subheader("Observation Target")
        img_path = metadata.get("IMAGE_PATH")
        # load and display rendered FITS image
        if img_path and os.path.exists(img_path):
            img = Image.open(img_path)
            st.image(img, caption = f"Target: {metadata.get('TARGNAME', 'Unknown')} | File: {metadata.get('FILE_NAME', 'Unknown')}", width = "stretch")
        else:
            st.warning(f"Image file not found at path: {img_path}")

        # interactive navigation buttons
        st.markdown("<br>", unsafe_allow_html = True)
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            if st.button("⬅️Previous Target", width = "stretch"):
                st.session_state.image_index = (st.session_state.image_index - 1) % len(all_metadata)
                st.rerun()
        with btn_col2:
            if st.button("Next Target➡️", width = "stretch"):
                st.session_state.image_index = (st.session_state.image_index + 1) % len(all_metadata)
        st.caption(f"Shwoing observation {st.session_state.image_index + 1} of {len(all_metadata)}")
    with col2:
        st.subheader("Extracted Telemetry")
        st.write("Parameters extracted automatically from raw FITS header by Gemini 2.5 Flash")

        # # extract values 
        target = metadata.get("TARGNAME", "Unknown")
        instrument = metadata.get("INSTRUME", "Unknown")
        filter_used = metadata.get("FILTER", "Unknown")
        # render style metric boxes
        st.metric(label = "Target Name (TARGNAME)", value = target)
        st.metric(label = "Instrument Type (INTSRUME)", value = instrument)
        st.metric(label = "Filter Used (FILTER)", value = filter_used)

        # show raw JSON payload in a collapsible drawer
        with st.expander("View raw JSON Payload"):
            st.json(metadata)
st.markdown("---")
st.caption("JWST Data Processing Pipeline")