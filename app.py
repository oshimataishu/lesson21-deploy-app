from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from streamlit import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
# LLMからの回答を取得する関数
def get_response(input_text, expert):
  llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5, api_key=os.environ["OPENAI_API_KEY"])
  if expert == "trainer":
    system_message = "あなたは運動の知識に精通したパーソナルトレーナーです．以下の質問について，あなたの専門知識をもとに回答してください．"
  elif expert == "nutritionist":
    system_message = "あなたは食生活について詳しい管理栄養士です．以下の質問について，あなたの専門知識をもとに回答してください．"

  human_message = input_text
  messages = [SystemMessage(system_message), HumanMessage(human_message)]

  response = llm(messages)
  return response


st.title("AI専門家と築く健康習慣")

st.write("#### 専門家A: 運動やスポーツについて詳しいパーソナルトレーナー")
st.write("#### 専門家B: 食生活について詳しい管理栄養士")

selected_expert = st.radio(
  "相談したい専門家を選択してください",
  ["運動のパーソナルトレーナー", "食生活の管理栄養士"]
)

st.divider()

if selected_expert == "運動のパーソナルトレーナー":
  input_text = st.text_area("質問内容を入力してください", height=200)
elif selected_expert == "食生活の管理栄養士":
  input_text = st.text_area("質問内容を入力してください", height=200)

if st.button("送信"):
  if selected_expert == "運動のパーソナルトレーナー":
    expert = "trainer"
    response = get_response(input_text, expert)
  elif selected_expert == "食生活の管理栄養士":
    expert = "nutritionist"
    response = get_response(input_text, expert)

  st.write(response.content)