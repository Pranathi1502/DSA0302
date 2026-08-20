from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

text = input("Enter English text: ")

prompt = "Translate English to French: " + text

inputs = tokenizer(prompt, return_tensors="pt")

outputs = model.generate(
    **inputs,
    max_new_tokens=100
)

translation = tokenizer.decode(
    outputs[0],
    skip_special_tokens=True
)

print("\nFrench Translation:")
print(translation)