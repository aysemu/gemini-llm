import os
from dotenv import load_dotenv
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from tools imporrt general_question_tool,mil_std_rag_tool

load_dotenv()

model= ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
memory InMemorySaver()
tools = [general_question_tool,mil_std_rag_tool]
agent = create_agent(model=model,tools=tools,system_prompt="""
sen tool kullanabilen bir yapay zeka asistanısın.
kullanıcının isteğini değerlendir veu uygun yöntemi seç
RKT-MIL-STD-001 dokümanıyla ilgili teknik sorular için mil_std_rag_tool toolunu kullan
genel bilgi veya dökümanla ilgisi olmayan bir soru sorulursa general_question_tool toolunu kullan
kullanıcının sorusu önceki konuşmada verilen bir bilgi kullanılarak cevaplanabiliyorsa konuşma geçmişini kullan.
türkçe cevap ver,
cevapları açık ve anlaşılır oluştur.
""",cheachpointer=memory)