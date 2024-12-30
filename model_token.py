from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5")
model = AutoModelForCausalLM.from_pretrained("OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5")

prompt = """
Bonjour, je veux me motiver aujourd'hui. Quels conseils as-tu pour que je reste concentré sur mes objectifs ?
"""
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(inputs.input_ids, max_length=200, temperature=0.7)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
