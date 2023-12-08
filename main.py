import os 
from apikey import apikey
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from website import create_app

# ingredients = input("Insert your ingredients here")
# cuisine = input("What kind of cuisine would you like ?")

# #Prompt templates
# title_template = PromptTemplate(
#         input_variables= ['ingredients', 'cuisine'],
#         template = 'Give me a name of dish made out from {ingredients} in {cuisine} cuisine'
#     )

# instructions_template = PromptTemplate(
#         input_variables= ['title'],
#         template = 'Give me instructions how to make this title TITLE:{title}'
#     )
# #LLMS
# llm = OpenAI(temperature=0.9)
# title_chain = LLMChain(llm=llm, prompt=title_template, output_key='title')
# instructions_chain = LLMChain(llm=llm, prompt=instructions_template, output_key='instructions')
# sequential_chain = SequentialChain(chains=[title_chain,instructions_chain], input_variables=['ingredients','cuisine'], output_variables=['title','instructions'], verbose=True)

# '"give response if there is an input"'
# if ingredients: 
#     response = sequential_chain({'ingredients':ingredients, 'cuisine':cuisine})
#     print(response['title'])
#     print(response['instructions'])
    
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
   
    
   