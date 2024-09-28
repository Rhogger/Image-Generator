from langflow.custom import Component
from langflow.inputs import MessageTextInput, IntInput
from langflow.template import Output
from langflow.schema.message import Message  # Retorno padrão do Langflow
from diffusers import StableDiffusionPipeline
import torch
from io import BytesIO
import base64

class ImageGeneratorComponent(Component):
    display_name = "Image Generator"
    description = "Generate image from text."
    icon = "image"

    inputs = [
        MessageTextInput(
            name="prompt",
            display_name="Prompt",
            info="Text input for generate image.",
        ),
        IntInput(
            name="width",
            display_name="Image Width",
            info="Defaults = 512",
        ),
        IntInput(
            name="height",
            display_name="Image Height",
            info="Defaults = 512",
        ),
    ]

    outputs = [
        Output(display_name="Base64 Image", name="base64_image", method="generate_image"),
    ]

    def load_model(self):
        if not hasattr(self, 'pipe'):
            model_id = "CompVis/stable-diffusion-v1-4"
            self.pipe = StableDiffusionPipeline.from_pretrained(
                model_id,
                torch_dtype=torch.float16
            )
            device = "cuda" if torch.cuda.is_available() else "cpu"
            self.pipe.to(device)
            self.device = device

    def generate_image(self) -> Message:
        prompt = self.prompt
        width = self.width or 512
        height = self.height or 512

        self.load_model()

        with torch.autocast(self.device):
            image = self.pipe(prompt, height=height, width=width).images[0]

        buffered = BytesIO()
        image.save(buffered, format="PNG")

        image_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

        return Message(text=image_base64)
