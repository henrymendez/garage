from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9)

text = "What would be a good name for an american football team?"

print(llm(text))
