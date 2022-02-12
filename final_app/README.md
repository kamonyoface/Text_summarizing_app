# Text Summarization App

This app takes user input (plain text or URL) and summarizes it. Summary is based on the output of sshleifer/distilbart-cnn-6-6 model accessed via HuggingFace transformers library.

To run it, either download this model: https://huggingface.co/sshleifer/distilbart-cnn-6-6? or change the value of variable model_name in the landing_page.py file to "sshleifer/distilbart-cnn-6-6".

The second option will download the model every time you run the app, so it will be heavy for your internet. I recommend downloading the model -- it is also available in google drive (you need to download the whole folder and keep it in that form in the same directory as landing_page.py file): https://drive.google.com/drive/folders/1-tdiEXw6Vrv1PucZ0BXGxdgr6mMaAhwe?usp=sharing
