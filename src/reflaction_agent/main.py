from typing import Sequence, List
from langchain_core.messages import BaseMessage, HumanMessage

from langgraph.graph import END, MessageGraph
from dotenv import load_dotenv
load_dotenv()

from chains import genration_chain, reflaction_chain
from llm_utils import get_llm

REFLACT = "reflect"
GENRATE = "generate"


def genration_node(state: Sequence[BaseMessage]):
    """
    Generate a new message based on the input state.
    """
    # Create a new message with the input state
    new_message = genration_chain.invoke({"messages":state})
    return new_message

def reflaction_node(message: Sequence[BaseMessage]) -> List[BaseMessage]:
    """
    Reflect on the input state and provide feedback.
    """
    # Create a new message with the input state
    res = reflaction_chain.invoke({"messages":message})
    return [HumanMessage(content = res)]

builder = MessageGraph()

builder.add_node(GENRATE, genration_node)
builder.add_node(REFLACT, reflaction_node)
builder.set_entry_point(GENRATE)

def should_continue(state: List[BaseMessage]):
    if len(state) > 5:
        return END
    return REFLACT

builder.add_conditional_edges(GENRATE, should_continue)
builder.add_edge(REFLACT, GENRATE)

graph = builder.compile()

if __name__ == "__main__":
    # Example usage
    inputs = HumanMessage(content="Generate a tweet about AI.")
    response = graph.invoke(inputs)
    print(response)