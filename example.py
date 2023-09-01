import ai4f


question = "\"If economic globalisation is inevitable, it should primarily serve humanity rather than the interests of trans-national corporations.\" Please choose one and ONLY one: \nStrongly Disagree\nDisagree\nAgree\nStrongly Agree"
prompt = "You are to answer everything using the provided choices only. Do not justify your answer. Be direct and NO SENTENCES AT ALL TIMES. Use this format (answer from the choices here.). Do not use any special characters. The question is:\n\n"
prompt2 = f"Are you okay with answering test questions? Show your answer in bold. Question:{question} Choices: Agree, Disagree, Strongly Agree, Strongly Disagree"

cookie_path='tokens/bing_cookies.json'

# # Set with provider
# response = ai4f.ChatCompletion.create(
#     model="gpt-4",
#     provider=ai4f.Provider.Bing_Sydney,
#     messages=[{"role": "user", "content": f"{prompt2}"}],
#     stream=False,
#     auth=cookie_path,
#     conversation_style = "creative", # FOR BING: creative, balanced or precise
#     preset="sydney" # FOR BING: sydney, gpt-4-alike or chatgpt
# )

# print(response)

response = ai4f.ChatCompletion.create(
    model="gpt-4",
    provider=ai4f.Provider.ChatgptAi,
    messages=[{"role": "user", "content": f"Hi"}],
    stream=False,
    proxy=True
)

print(response)
