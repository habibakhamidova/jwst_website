# Extracted JWST Metadata Displayed on a UI
I built a a project featuring an interactive Streamlit website along with an algorithm that processes, extracts, and visualizes astronomical metadata and image telemetry from James Wenn Space Telescope (JWST) FITS files targeting NGC 3324 (The Cosmic Cliffs area in the Carina Nebula).

This project benchmarks Large Language Models (Google Gemini 2.5) as automated astrophysics data processing agents to extract key FITS header parameters, renders 2D image matricies using matplotlib, pipelines the extracted parameters and images to a collective folder, and displays the resulting data in an interactive dashboard. 

## Overview
| Category | Technology / Library|
|------|------|
| UI | Streamlit |
| Data Processing	|  Python 3.11+, Astropy, NumPy |
| Visualizations |	Matplotlib |
| AI Infrastructure	| Google GenAI SDK (Gemini 2.5 Flash / Pro) |
| Data Archive	| MAST (Mikulski Archive for Space Telescopes) |

## Running this project
1. Prerequisites
   Python 3.10+ version alongisde a Google Gemini API Key
2. Installation
   Clone the repository and install required dependencies:
   `git clone https://github.com/your-username/jwst_website.git
    cd jwst_website
    pip install -r requirements.txt`
   In addition to the requirements file, install processing tools if running the notebook locally:
   `pip install astropy matplotlib google-genai`
3. Running the Pipeline
   Execute `data_analysis.ipynb` in Jupyter Notebook or VS Code to process raw FITS files
   `client = genai.Client(api_keys = "YOUR_GEMINI_API_KEY")`
   Then, run all cells in the notebook to generate a `web_assets/data.json` and processed images
4. Launch the Website
   Run the Streamlit dashboard
   `streamlit run app.py`
## Dataset Information
- Target Name: NGC 3324 (star-forming region)
- Program ID: JWST ERS 02731
- Instrument: NIRCam (Near-Infrared Camera)
- Detectors: SW (`nrca1-nrca4, nrcb1-nrcb4`) and LW (`nrcalong, nrcblong`)
- File Format: Flexible Image Transport Sustemm (FITS) `.fits/.crf`
