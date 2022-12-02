# import streamlit as st
# import torch
# from torch import autocast
# from diffusers import LMSDiscreteScheduler
# from japanese_stable_diffusion import JapaneseStableDiffusionPipeline

# YOUR_TOKEN = "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"
# model_id = "rinna/japanese-stable-diffusion"
# device = "cuda"
# # Use the K-LMS scheduler here instead
# scheduler = LMSDiscreteScheduler(beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear", num_train_timesteps=1000)
# pipe = JapaneseStableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, use_auth_token=True)
# pipe = pipe.to(device)


# prompt = "油絵のたこ焼き"
# with autocast("cuda"):
#     image = pipe(prompt, guidance_scale=7.5).images[0]
# st.image(image)
# image.save("output.png")