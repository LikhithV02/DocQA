import torch, re
from PIL import Image
from transformers import DonutProcessor, VisionEncoderDecoderModel

# image_path = '/app/Datasplit/test/1099_Div/filled_form_43.jpg'
# image = Image.open(image_path)
# imgae = image.resize((1864, 1440))

device = "cuda" if torch.cuda.is_available() else "cpu"
device = "cpu"
# Load the processor from the local directory
processor = DonutProcessor.from_pretrained("Henge-navuuu/donut-base-finetuned-forms-v1", cache_dir="./models")

# Load the model from the local directory
model = VisionEncoderDecoderModel.from_pretrained("Henge-navuuu/donut-base-finetuned-forms-v1", cache_dir="./models")
model.to(device)

def inference(image):
    pixel_values = processor(image, return_tensors="pt").pixel_values
    task_prompt = "<s>"
    decoder_input_ids = processor.tokenizer(task_prompt, add_special_tokens=False, return_tensors="pt")["input_ids"]

    # device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)

    outputs = model.generate(pixel_values.to(device),
                                decoder_input_ids=decoder_input_ids.to(device),
                                max_length=model.decoder.config.max_position_embeddings,
                                early_stopping=True,
                                pad_token_id=processor.tokenizer.pad_token_id,
                                eos_token_id=processor.tokenizer.eos_token_id,
                                use_cache=True,
                                num_beams=1,
                                bad_words_ids=[[processor.tokenizer.unk_token_id]],
                                return_dict_in_generate=True,
                                output_scores=True,)
    
    sequence = processor.batch_decode(outputs.sequences)[0]
    sequence = sequence.replace(processor.tokenizer.eos_token, "").replace(processor.tokenizer.pad_token, "")
    sequence = re.sub(r"<.*?>", "", sequence, count=1).strip()  # remove first task start token
    print(processor.token2json(sequence))
    return processor.token2json(sequence)

# data = inference(image)
# print(data)