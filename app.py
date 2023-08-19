from __future__ import annotations

import os

import gradio as gr
import tesserocr


def _language_matcher(language):
    mapping = {
        "English": "en",
        "Spanish": "spa",
        "Portuguese": "por",
    }
    if language in mapping:
        return mapping[language]
    raise ValueError(f"The language {language} is not mapped...")


def image_to_text(image, language):
    image_text = tesserocr.image_to_text(
        image=image,
        lang=_language_matcher(language),
    )
    output_msg = f"Text from Image: {image_text}"
    return output_msg


demo = gr.Interface(
    fn=image_to_text,
    inputs=[
        gr.Image(type="pil"),
        gr.Dropdown(choices=["English", "Spanish", "Portuguese"], label="Language"),
    ],
    outputs=gr.Textbox(label="Text Output", placeholder="Image text will go here:"),
    examples=[
        [
            os.path.join(os.path.dirname(__file__), "docs/example.jpeg"),
            "Spanish",
        ],
    ],
)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860)),
    )
