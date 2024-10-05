import pandas as pd
import json
import os
from dotenv import load_dotenv

import langchain
from langchain.chat_models import ChatOpenAI
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
from langchain.chains import LLMChain

from src.pred_code.utils import read_file

load_dotenv()

key = os.getenv("API_KEY")

llm = ChatOpenAI(openai_api_key=key,model_name="gpt-3.5-turbo", temperature=0.3)

TEMPLATE = ""

predictor_prompt = PromptTemplate(
    input_variables=[],
    template=TEMPLATE
)

predictor_chain=LLMChain(llm=llm,prompts=predictor_prompt,output_key="Predictor_variables",verbose=True)

TEMPLATE2 = ""

predictor_prompt2 = PromptTemplate(
    input_variables=[],
    template=TEMPLATE
)

predictor_chain2=LLMChain(llm=llm,prompts=predictor_prompt2,output_key="accuracy",verbose=True)

generate_evaluate_chain=SequentialChain(chains=[predictor_chain, predictor_chain2], input_variables=[],
                                        output_variables=["Predictor_variables", "accuracy"], verbose=True,)