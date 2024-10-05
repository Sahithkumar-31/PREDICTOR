import pandas as pd
import json
import os

#langchain import
import langchain
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
from langchain.chains import LLMChain

def read_file():
    df = pd.read_csv(r"D:\Bro's\dataset.csv")
    df_input = df.drop(columns="Exam_Score")
    df_output = df["Exam_Score"]
    df_input_json = df_input.to_json()
    df_output_json = df_output.to_json()
    
    return [df_input_json,df_output_json]


