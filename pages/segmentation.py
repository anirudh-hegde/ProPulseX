import os
from google.cloud import vision
import io
import cv2
from PIL import Image
import numpy as np
import streamlit as st
import base64


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service_token.json"


def segment_image(image_content):
    # Read the image using OpenCV
    np_arr = np.frombuffer(image_content, np.uint8)
    image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    # Find contours to segment the image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    segments = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        segment = image[y:y + h, x:x + w]
        segments.append(segment)

    return segments

def create_html(segments):
    html_content = ""
    html_content += "<h2>Segmentations</h2>"
    html_content += "<hr>"
    # Add extracted text in paragraphs

    # Add visual elements as images
    for i, segment in enumerate(segments):
        _, buffer = cv2.imencode('.jpg', segment)
        segment_base64 = base64.b64encode(buffer).decode('utf-8')


        html_content += f'<img src="data:image/jpeg;base64,{segment_base64}" alt="Visual Element">'


    html_content += "<hr>"
    return html_content


def main():
    # Analyze the image to extract text
    # extracted_text, image_content = analyze_image(image_path)

    # Segment the image to extract visual elements
    # segments = segment_image(image_path)
    st.title("Image Segementation")
    # image_path = "images/google.png"
    image_file = st.file_uploader("Upload the file: ")
    if image_file is not None:
        image = Image.open(image_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        image_byte_array = io.BytesIO()
        image.save(image_byte_array, format=image.format)
        image_content = image_byte_array.getvalue()
        # main(image_content)
        segments = segment_image(image_content)
        html_content = create_html(segments)

        # segment_image(image_content)

        with open("result.html", "w") as html_file:
            html_file.write(html_content)
        with open("result.html", "r") as html_file:
            st.markdown(html_file.read(), unsafe_allow_html=True)

        with open("final_result.html", "a") as html_file:
            html_file.write(html_content)

if __name__ == "__main__":
    main()
