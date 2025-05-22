from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

reflaction_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a viral twitter influencer grading a tweet. Generate critique and recommendations for the user's tweet."
        "Always provide detailed recommendations, including requests for length, virality, style, etc.",
    ),
    MessagesPlaceholder(variable_name="messages"),
])

genration_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a twitter techie influencer assistant tasked with writing excellent twitter posts."
        " Generate the best twitter post possible for the user's request."
        " If the user provides critique, respond with a revised version of your previous attempts.",
    ),
    MessagesPlaceholder(variable_name="messages"),
])

from llm_utils import get_llm
from langchain_core.messages import BaseMessage
from typing import Sequence
llm = get_llm()
genration_chain = genration_prompt | llm
reflaction_chain = reflaction_prompt | llm
