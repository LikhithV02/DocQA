import torch, re
from PIL import Image
from transformers import DonutProcessor, VisionEncoderDecoderModel

# image_path = '/app/Datasplit/test/1099_Div/filled_form_43.jpg'
# image = Image.open(image_path)
# imgae = image.resize((1864, 1440))

device = "cuda" if torch.cuda.is_available() else "cpu"
processor = DonutProcessor.from_pretrained("Henge-navuuu/donut-base-finetuned-forms-v1" , token="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")
model = VisionEncoderDecoderModel.from_pretrained("Henge-navuuu/donut-base-finetuned-forms-v1" , token = "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" )

model.save_pretrained("/home/chethan/Documents/MONISH/final year project/our_project/DocQA/models/donut_finetuned")
processor.save_pretrained("/home/chethan/Documents/MONISH/final year project/our_project/DocQA/models/donut_finetuned")


