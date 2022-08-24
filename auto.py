# did not have the script to hand so writing a quick example that may or may not work
import sys
import random
from ldm.simplet2i import T2I
model = T2I()
# in my script its in a different file but, same difference

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
# can also use t2i.img2img with init_img arg