from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
import os 
from apikey import apikey
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from .models import Recipe, User
from . import db 

views = Blueprint('views', __name__)

@views.route('/')
def welcome():
    return render_template('welcome.html')



@views.route('/create', methods = ['POST', 'GET'])
@login_required
def create():
    if request.method == 'POST':
        ingredients= request.form.get('ingredients')
        cuisine = request.form.get('cuisine')
                   
        title_template = PromptTemplate(
                input_variables= ['ingredients', 'cuisine'],
                template = 'Give me a name of dish made out from {ingredients} in {cuisine} cuisine'
            )

        instructions_template = PromptTemplate(
                        input_variables= ['title'],
                        template = 'Give me instructions how to make this title TITLE:{title}'
            )
        #LLMS
        llm = OpenAI(temperature=0.9)
        title_chain = LLMChain(llm=llm, prompt=title_template, output_key='title')
        instructions_chain = LLMChain(llm=llm, prompt=instructions_template, output_key='instructions')
        sequential_chain = SequentialChain(chains=[title_chain,instructions_chain], input_variables=['ingredients','cuisine'], output_variables=['title','instructions'], verbose=True)

        #give response if there is an input
        
        response = sequential_chain({'ingredients':ingredients, 'cuisine':cuisine})
        new_recipe = Recipe(title= response['title'], instructions= response['instructions'], user_id=current_user.id )
        db.session.add(new_recipe)
        db.session.commit()
        
        
    
    return render_template('create.html', user=current_user)
