# Extracted JWST Metadata Displayed on a UI
This is a website that I developed using Streamlit. It pipelines AI-extracted data from JWST NGC 3324 (star-forming region) FITS file metadata, which can be found in /web_assets. Information, such as target name, intrument type, filter, etc., is stored as a JSON file. Images were constructed using matplotlib from the metadata features. 


| Category | Technology / Library|
|------|------|
| UI | Streamlit |
| Data Processing	|  Python 3.11+, Astropy, NumPy |
| Visualizations |	Matplotlib |
| AI Infrastructure	| Google GenAI SDK (Gemini 2.5 Flash / Pro) |
| Data Archive	| MAST (Mikulski Archive for Space Telescopes) |
