from google import genai
from google.genai import types  

client = genai.Client(api_key="AIzaSyBGyIZo7g1sjQVHWl7vXg7BsN8wQ6ojSpA")

response = client.models.generate_content(
    model="gemini-2.0-flash-exp", # 或者你使用的模型
    contents="Tell me Albert Einstein's contributions to the field of physics",
    config=types.GenerateContentConfig(
        temperature=0.7,      # 控制随机性：0.0 最确定，越高越发散
        top_p=0.95,           # 核心采样参数
        top_k=40,             # 候选词数量限制
        max_output_tokens=1024, # 最大生成长度
        candidate_count=1,     # 生成候选响应的数量
        stop_sequences=["STOP!"], # 停止字符
    )
)

print(response.text)