# Text Summarization App

## By: Jan Galinski, Thomas Elbert, Kamil Kinastowski, Kuba Białczyk

This app takes user input (plain text or URL) and summarizes it. Summary is based on the output of sshleifer/distilbart-cnn-6-6 model accessed via HuggingFace transformers library. The user can write a title of the text that will be uploaded. Then the text or URL can be pasted. After that the model will summarize given text and present the output. Then user can copy the text or save it. In the "Files" section the saved texts will be presented. User also can read the "About us" page.

The needed libraries for this project are: kivy, pyperclip, newspaper3k and transformers. 

To run it, either download this model: https://huggingface.co/sshleifer/distilbart-cnn-6-6? or change the value of variable model_name in the landing_page.py file to "sshleifer/distilbart-cnn-6-6".

The second option will download the model every time you run the app, so it will be heavy for your internet. I recommend downloading the model -- it is also available in google drive (you need to download the whole folder and keep it in that form in the same directory as landing_page.py file): https://drive.google.com/drive/folders/1-tdiEXw6Vrv1PucZ0BXGxdgr6mMaAhwe?usp=sharing


