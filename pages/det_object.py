import os
from google.cloud import vision
import io
from PIL import Image, ImageDraw
import streamlit as st

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service_token.json"

def localize_objects(image_content):
    client = vision.ImageAnnotatorClient()
    image = vision.Image(content=image_content)

    objects = client.object_localization(image=image).localized_object_annotations
    return objects


def html_page(objects):
    html_content = ""
    html_content += "<hr>"

    html_content += f"<h3>Number of objects found: {len(objects)}</h3>"
    for object_ in objects:
        html_content += f"\n<p>{object_.name} (confidence: {object_.score}) </p>"
        html_content += f"<h4>Normalized bounding vertices: </h4>"
        for vertex in object_.bounding_poly.normalized_vertices:
            html_content += f"<p> - ({vertex.x}, {vertex.y})</p>"
    html_content += "<hr>"

    return html_content


def main():
    st.title("Object localization")
    image_file = st.file_uploader("upload the file: ")
    if image_file is not None:
        image = Image.open(image_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        image_byte_array = io.BytesIO()
        image.save(image_byte_array, format=image.format)
        image_content = image_byte_array.getvalue()
        objects = localize_objects(image_content)
        html_content = html_page(objects)

        with open("result.html", "w") as html_file:
            html_file.write(html_content)
        with open("result.html", "r") as html_file:
            st.markdown(html_file.read(), unsafe_allow_html=True)
        with open("final_result.html", "a") as html_file:
            html_file.write(html_content)


if __name__ == "__main__":
    main()
