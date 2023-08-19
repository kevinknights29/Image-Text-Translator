from __future__ import annotations

import os

import gradio as gr
import tesserocr
from PIL import Image


def image_to_text(image):
    image = Image.open("sample.jpg")
    package_version = tesserocr.tesseract_version()
    languages = tesserocr.get_languages()
    image_text = tesserocr.image_to_text(image)
    output_msg = (
        f"Tesseract OCR version: {package_version}\n"
        f"Languages Available: {languages}\n"
        f"Text from Image: {image_text}"
    )
    return output_msg


demo = gr.Interface(
    image_to_text,
    gr.Image(type="pil"),
    "image",
    examples=[
        os.path.join(os.path.dirname(__file__), "docs/example.jpeg"),
    ],
)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860)),
    )
