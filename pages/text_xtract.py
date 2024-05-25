import os
from google.cloud import vision
import io
from PIL import Image
# import numpy as np
import streamlit as st

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service_token.json"


def detect_text(image_content):
    """Detects text in the file located in Google Cloud Storage or on the Web."""

    client = vision.ImageAnnotatorClient()
    image = vision.Image(content=image_content)
    # image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations
    # html_content = "<html><body>"
    extracted_text = [text.description for text in texts]

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )
    return extracted_text


def html_page(extracted_text):
    # html_content = "<html><body>"
    html_content = ""
    html_content += "<h2>Text Extraction</h2>"
    html_content += "<hr>"
    for text in extracted_text:
        html_content += f"<p>{text}</p>"
    html_content += "</body></html>"
    return html_content


def main():
    st.title("Text Extraction")

    image_file = st.file_uploader("Upload the file: ")

    if image_file is not None:
        image = Image.open(image_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.markdown("---")

        image_byte_array = io.BytesIO()
        image.save(image_byte_array, format=image.format)
        image_content = image_byte_array.getvalue()
        extracted_text = detect_text(image_content)
        html_content = html_page(extracted_text)
        # Detect properties
        # detect_text(image_content)
        with open("result.html", "w") as html_file:
            html_file.write(html_content)
        with open("result.html", "r") as html_file:
            st.markdown(html_file.read(), unsafe_allow_html=True)

        with open("final_result.html", "a") as html_file:
            html_file.write(html_content)


if __name__ == "__main__":
    main()
