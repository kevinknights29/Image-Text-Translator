from __future__ import annotations

import os

import gradio as gr
import tesserocr


def image_to_text(image):
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
    fn=image_to_text,
    inputs=gr.Image(type="pil"),
    outputs=gr.Textbox(label="Text Output", placeholder="Image text will go here:"),
    examples=[
        os.path.join(os.path.dirname(__file__), "docs/example.jpeg"),
    ],
)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860)),
    )
