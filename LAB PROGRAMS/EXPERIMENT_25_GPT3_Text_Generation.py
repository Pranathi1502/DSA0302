from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

prompt = input("Enter a prompt: ")

result = generator(
    prompt,
    max_new_tokens=100,
    num_return_sequences=1,
    do_sample=True
)

print("\nGenerated Text:\n")
print(result[0]["generated_text"])