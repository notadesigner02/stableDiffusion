# did not have the script to hand so writing a quick example that may or may not work
import sys
import random

#not sure if this path append is needed for relative files
sys.path.append(".models/ldm/text2img256")

#C:\sd\waifu-diffusion-main\models\ldm\text2img256
from ldm.text2img256 import text2img256

model = text2img256()
# in my script its in a different file but, same difference ##so you can import the yaml.conf, name it whatever. ok.

keywords1 = """ugly
beautiful
magnificent""".split("\n")

keywords2 = """dog
cat
human
chicken
chair
desk
lamp""".split("\n")

# i only used one very specific prompt and it wasnt any of these bc you should fine tune that with a bunch of trial and error to find the best match first
prompts = """{0} {1} 4k unreal engine
{0} {1} stylized octane render artstaiton
{0} {1} photo 31mm""".split("\n")
image_count = int(sys.argv[1])
outdir = sys.argv[2]

for i in range(10000):
prompt = prompts[random.randrange(0, len(prompts))].format(keywords1[random.randrange(0, len(keywords1)], keywords2[random.randrange(0, len(keywords1)])
outputs = model.txt2img(prompt=prompt, outdir=outdir)


-------------

# can also use t2i.img2img with init_img arg
python autoimg.py

for i in range(10000):
prompt = prompts[random.randrange(0, len(prompts))].format(keywords1[random.randrange(0, len(keywords1)], keywords2[random.randrange(0, len(keywords1)])
outputs = model.img2img(prompt=prompt, outdir=outdir)


#python autoimg2img.py --init-img /input/input.jpg --strength 0.8 --n_iter 6 --n_samples 2 --H 512 --W 512

#could the script be the above then and you pass parameters when calling to specify the inititial image and other parameters?