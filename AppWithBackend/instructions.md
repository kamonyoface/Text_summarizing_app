# This folder contains files of the app with working summarizing backend

The front-end is the same as in the <strong>ScreenManagerWithPositioning</strong> folder, but It has a connected backend with ML Summarizing Model.

To run it, either download this model: https://huggingface.co/sshleifer/distilbart-cnn-6-6?
or change the value of variable <i>model_name</i> in the <strong>landing_page.py</strong> file to "sshleifer/distilbart-cnn-6-6".

The second option will download the model every time you run the app, so it will be heavy for your internet. I recommend downloading the model -- it will be also available in google drive soon:
