import pickle
from transformers import pipeline, set_seed

generator = pipeline('text-generation', model='gpt2')
set_seed(42)

with open("flaskr/generator.bin", "wb") as f_out:
    pickle.dump(generator, f_out)
    f_out.close()

"""
with open("flaskr/generator.bin", "rb") as f_in:
    model = pickle.load(f_in)


print(model("Scientists believe that unicorns", max_length=100))

"""

