# Installing via. Pip
# pip install --upgrade huggingface_hub

from huggingface_hub import InferenceClient

client = InferenceClient()  #Inference is the process of using a trained model to make predictions on new data.
                            #InferenceClient is a Python client making HTTP calls to our APIs.

# Lines 9-12 are an example of using the inference client with another provider, api_key can be also be set.
replicate_client = InferenceClient(
    provider="replicate",
    api_key="my_replicate_api_key",
)

image = client.text_to_image(# Insert prompt in quotes)
image.save("image.png")

# Notes oon Login
#Login command
#The easiest way to authenticate is to save the token on your machine. You can do that from the terminal using the login() command:
#huggingface-cli login (In terminal)
#The command will tell you if you are already logged in and prompt you for your token. 
#The token is then validated and saved in your HF_HOME directory (defaults to ~/.cache/huggingface/token). 
#Any script or library interacting with the Hub will use this token when sending requests.

#Alternatively, you can programmatically login using login() in a notebook or a script:
from huggingface_hub import login
login()
#You can only be logged in to one account at a time. 
#Logging in to a new account will automatically log you out of the previous one.
#To determine your currently active account, simply run the huggingface-cli whoami command.
#Once logged in, all requests to the Hub - even methods that don’t necessarily require authentication - will use your access token by default. 
#If you want to disable the implicit use of your token, you should set environment variable as below:
HF_HUB_DISABLE_IMPLICIT_TOKEN=1
