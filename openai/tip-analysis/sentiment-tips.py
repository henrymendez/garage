import csv
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.chains import LLMChain


llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
#llm = OpenAI(temperature=0, model_name="text-curie-001")
prompt = PromptTemplate(
    input_variables=["tip"],
    template="Respond with either helpful, negative, or vulgar. Determine if the following comment is helpful, negative, or vulgar: {tip}",
    )
chain = LLMChain(llm=llm, prompt=prompt)

with open('tips-take2.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    data = []
    for row in csv_reader:
        data.append(row)


with open('output.csv', 'a') as csvfile:
    for row in data:
        #print(prompt.format(tip=row[3]))
        result = chain.run(row[3])
        print(row[0], result)
        row.append(result)
        writer = csv.writer(csvfile, dialect='excel')
        writer.writerow(row) 

#for row in data:
#    result = chain.run(row[3])
#    print(row[0], result)
#    row.append(result)
#    print(row)
