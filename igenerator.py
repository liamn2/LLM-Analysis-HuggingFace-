from huggingface_hub import InferenceClient
client = InferenceClient()

image = client.text_to_image("Dragon")
image.save("dragon.png")
