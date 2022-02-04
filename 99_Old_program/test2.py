from mathpix.mathpix import MathPix
from IPython.display import display,Math,YouTubeVideo,clear_output,HTML,Markdown

mathpix = MathPix(\
            app_id="shuji-watanabe_neptune_kanazawa-it_ac_jp_ca0617_d97334",\
            app_key="a70cf9905f4fe412224af9fb25bed51c09d4fa522e53362828a25c512dd6c077")
ocr = mathpix.process_image(image_path="/Users/s-wat/02_Python/00_Web-App-KIT-/limit.jpg")

display( ocr.latex )
