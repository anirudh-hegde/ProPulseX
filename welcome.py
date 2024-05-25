import streamlit as st


def main():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to ImageOps Web App! 👋")

    st.sidebar.success("Select a web page above ☝️")

    st.markdown(
        """
        The ImgOps application leverages the Google Cloud Vision API to analyze and detect 
        properties of uploaded images, specifically focusing on identifying dominant colors. 
        The application is built using Streamlit, a popular framework for creating interactive 
        web applications with Python. Users can upload an image file through a simple user interface. 
        Once the image is uploaded, the application processes the image to extract its content and 
        sends it to the Google Cloud Vision API.

        The application also handles the generation and management of an HTML file named result.html. 
        Before writing new content to this file, the application ensures that any existing content is 
        cleared, thereby avoiding conflicts or outdated data. The generated HTML content, which visually 
        represents the dominant colors of the uploaded image, is written to this file. Users can download 
        this HTML file or open it directly within a new browser tab.

        An important aspect of the application is its interactive elements. Users can click a button to open 
        the HTML file in a new tab, facilitated by embedded JavaScript. This makes the application user-friendly 
        and ensures a seamless experience from image upload to viewing the analysis results. The use of Streamlit 
        ensures that the interface is intuitive and easy to navigate, making the ImageOps application a robust tool 
        for color analysis of images.
        
        ### Want to know about project's gitHub repository?
        - Check out [imgops](https://github.com/imgops)

    """
    )
    st.snow()


if __name__ == "__main__":
    main()