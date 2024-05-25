import os
from google.cloud import vision
import io
from PIL import Image
# import numpy as np
import streamlit as st

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service_token.json"

def detect_properties(image_content):
    """detects the image properties of the file."""
    client = vision.ImageAnnotatorClient()
    image = vision.Image(content=image_content)

    response = client.image_properties(image=image)
    props = response.image_properties_annotation

    dominant_colors = props.dominant_colors.colors

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )
    return dominant_colors


def html_page(dominant_colors):
    html_content = "<html><body>"
    html_content += "<h2>Dominant Colors: </h2>"
    html_content += "<style>p {font-size: 19px;} </style>"
    html_content += "<hr>"
    for color in dominant_colors:

        html_content += f"<p>Fraction: {color.pixel_fraction}<br>"
        html_content += f"\tR: {color.color.red}"
        html_content += f"\tG: {color.color.green}"
        html_content += f"\tB: {color.color.blue}"
        html_content += f"\tA: {color.color.alpha}</p>"

    html_content += "</h2>"
    html_content += "<hr>"
    return html_content


def main():
    st.title("Image Detection")

    image_file = st.file_uploader("Upload the file: ")
    if image_file is not None:
        image = Image.open(image_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        image_byte_array = io.BytesIO()
        image.save(image_byte_array, format=image.format)
        image_content = image_byte_array.getvalue()
        dominant_colors = detect_properties(image_content)
        html_content = html_page(dominant_colors)
        # Detect properties
        detect_properties(image_content)
        with open("result.html", "w") as html_file:
            html_file.write(html_content)
        with open("result.html","r") as html_file:
            st.markdown(html_file.read(),unsafe_allow_html=True)
        with open("final_result.html", "a") as html_file:
            html_file.write(html_content)


if __name__ == "__main__":
    main()
