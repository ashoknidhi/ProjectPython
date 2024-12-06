import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

from langchain.chat_models import ChatOpenAI
from langchain.schema import(
    AIMessage,
    HumanMessage,
    SystemMessage
)


text= """
Read information about loan offerings from Mahindra Finance India by accessing https://www.mahindrafinance.com/
"""

messages = [
    SystemMessage(content='You are an expert Vehicle loan consultant from Mahindra Finance with expertize in articulating loan offers'),
    HumanMessage(content=f'Please provide detailed information about vehicle loans:\n TEXT: {text}')
]