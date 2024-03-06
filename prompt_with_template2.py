from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import gradio as gr

openai = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    openai_api_key="....."
)

def chatbot(step_by_step):

    template = """Question: {question}
    please provide step by step Answer:
    """
    prompt = PromptTemplate(template=template, input_variables=["question"])
    formated_prompt =prompt.format(question=str(step_by_step))
    return openai.invoke(formated_prompt).content

demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")

demo.launch(share=True)