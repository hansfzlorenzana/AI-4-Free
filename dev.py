import requests, re, json
from Provider.proxies import proxies

response = requests.get("https://chatgpt.ai/gpt-4/")
print(response.text)

nonce = re.findall(r'"search_nonce":"([^"]*)"', response.text)[0]
post_id = re.findall(r'"post_id":"([^"]*)"', response.text)[0]
# bot_id = re.findall(r'"search_nonce":"([^"]*)"', response.text)

# print(nonce, post_id)

# headers = {
#     "authority": "chatgpt.ai",
#     "accept": "*/*",
#     "accept-language": "en,fr-FR;q=0.9,fr;q=0.8,es-ES;q=0.7,es;q=0.6,en-US;q=0.5,am;q=0.4,de;q=0.3",
#     "cache-control": "no-cache",
#     "origin": "https://chatgpt.ai",
#     "pragma": "no-cache",
#     "referer": "https://chatgpt.ai/gpt-4/",
#     "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": '"Windows"',
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-origin",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
# }
# data = {
#     "_wpnonce": nonce,
#     "post_id": post_id,
#     "url": "https://chatgpt.ai/gpt-4",
#     "action": "wpaicg_chat_shortcode_message",
#     "message":"What ai model are you based on?",
#     "bot_id": "gpt4",
# }

# response = requests.post(
#     "https://chatgpt.ai/wp-admin/admin-ajax.php", headers=headers, data=data
# )

# print(response.json()["data"])