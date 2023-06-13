import os

#import streamlit as st

from langchain import PromptTemplate, LLMChain
from langchain.llms import GPT4All

from langchain.agents.agent_toolkits import create_python_agent
from langchain.tools.python.tool import PythonREPLTool

#st.title('PersonalGPT 🎯🔏')

PATH = 'E:/GPT4ALL_Datasets/ggml-gpt4all-j-v1.3-groovy.bin'

llm = GPT4All(model=PATH, verbose=True)

#python_agent = create_python_agent(llm=llm, tool=PythonREPLTool(), verbose=True)

prompt = PromptTemplate(input_variables=['question'],
                        template='''
                        Question: {question}
                        Answer: Let me think ...''')

chain = LLMChain(prompt=prompt, llm=llm)

prompt = input('Write your prompt here ... ')

if prompt:
    response = chain.run(prompt)
    print(response)

