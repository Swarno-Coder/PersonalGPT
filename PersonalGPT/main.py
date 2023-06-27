#!/usr/bin/env python3
from langchain.chains import RetrievalQA,LLMChain
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import (
    LlamaCpp,
    GPT4All,
    Cohere,
    OpenAI
)
from langchain import PromptTemplate
from .env_vars import *
from .ingest import Ingest
from .engine import takeCommand, speak

class PersonalGPT(Ingest):
    """_summary_

    Args:
        Ingest (_type_): _description_
    """
    def __init__(self):
        super(Ingest,self).__init__()
        # activate/deactivate the streaming StdOut callback for LLMs
        callbacks = [StreamingStdOutCallbackHandler()]
        self.FLAG=False
        # Prepare the LLM
        match MODEL_TYPE:
            case "LlamaCpp":
                self.llm = LlamaCpp(model_path=MODEL_PATH, n_ctx=MODEL_N_CTX, callbacks=callbacks, verbose=False)
            case "GPT4All":
                self.llm = GPT4All(model=MODEL_PATH, n_ctx=MODEL_N_CTX, backend='gptj', callbacks=callbacks, verbose=False)
            case "Cohere":
                self.llm = Cohere(cohere_api_key=API_KEY, max_tokens=2000, callbacks=callbacks, verbose=False)
            case "OpenAI":
                self.llm = OpenAI(openai_api_key=API_KEY, temperature=0.7, max_tokens=256, callbacks=callbacks, verbose=False)
            case _default:
                print(f"Model {MODEL_TYPE} not supported!")
                exit;
    def from_my_docs(self, flag=True):    
        db = super().load()
        retriever = db.as_retriever(search_kwargs={"k": TARGET_SOURCE_CHUNKS})
        self.qa = RetrievalQA.from_chain_type(llm=self.llm, chain_type="stuff", retriever=retriever)
        self.FLAG=flag
    
    def ask_query(self):
    # Interactive questions and answers
        while True:
            query = takeCommand("Ask a query Master,")
            if query == "exit":
                break
            #print(f"{self.llm}")
            # Get the answer from the chain
            if self.FLAG: res = self.qa.run(query)
            else: 
                prompt = PromptTemplate(input_variables=['question'],
                        template='''
                        Question: {question}
                        Answer: ''')
                self.chain = LLMChain(llm=self.llm, prompt=prompt)
                res = self.chain.run(query)
    
            # Speak the result
            speak(f"Question You've asked: {query} and the Answer is: {res}")
    