#!/usr/bin/env python3
from langchain.chains import RetrievalQA
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import (
    LlamaCpp,
    GPT4All,
    Cohere,
    OpenAI
)
from env_vars import *
from ingest import Ingest
from Jarvis import takeCommand, speak

class PersonalGPT(Ingest):
    """_summary_

    Args:
        Ingest (_type_): _description_
    """
    def __init__(self):
        super(self).__init__()
        db = super().load()
        retriever = db.as_retriever(search_kwargs={"k": TARGET_SOURCE_CHUNKS})
        # activate/deactivate the streaming StdOut callback for LLMs
        callbacks = [StreamingStdOutCallbackHandler()]
        # Prepare the LLM
        match MODEL_TYPE:
            case "LlamaCpp":
                llm = LlamaCpp(model_path=MODEL_PATH, n_ctx=MODEL_N_CTX, callbacks=callbacks, verbose=False)
            case "GPT4All":
                llm = GPT4All(model=MODEL_PATH, n_ctx=MODEL_N_CTX, backend='gptj', callbacks=callbacks, verbose=False)
            case "Cohere":
                llm = Cohere(cohere_api_key=API_KEY, max_tokens=2000, callbacks=callbacks, verbose=False)
            case "OpenAI":
                llm = OpenAI(openai_api_key=API_KEY, temperature=0.7, max_tokens=256, callbacks=callbacks, verbose=False)
            case _default:
                print(f"Model {MODEL_TYPE} not supported!")
                exit;
        self.qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
    
    def ask_query(self):
    # Interactive questions and answers
        while True:
            query = takeCommand("Ask a query Master,")
            if query == "exit":
                break
    
            # Get the answer from the chain
            res = self.qa.run(query)
    
            # Speak the result
            speak(f"Question You've asked: {query} and the Answer is: {res}")
    