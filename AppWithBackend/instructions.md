# This folder contains files of the app with working summarizing backend

The front-end is the same as in the <strong>ScreenManagerWithPositioning</strong> folder, but It has a connected backend with ML Summarizing Model.

To run it, either download this model: https://huggingface.co/sshleifer/distilbart-cnn-6-6?
or change the value of variable <i>model_name</i> in the <strong>landing_page.py</strong> file to "sshleifer/distilbart-cnn-6-6".

The second option will download the model every time you run the app, so it will be heavy for your internet. I recommend downloading the model -- it is also available in google drive (you need to download the whole folder and keep it in that form in the same directory as landing_page.py file): https://drive.google.com/drive/folders/1-tdiEXw6Vrv1PucZ0BXGxdgr6mMaAhwe?usp=sharing
