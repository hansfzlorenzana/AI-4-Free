import re
from httpx import Client
import requests
from time import sleep
from ..typing import Any, CreateResult
from ..proxies import fetch_proxy, fetch_free_proxy
from .base_provider import BaseProvider

class ChatgptAi(BaseProvider):
    url = "https://chatgpt.ai/gpt-4/"
    working = True
    supports_gpt_4 = True
    supports_proxy = True

    @staticmethod
    def create_completion(
        model: str,
        messages: list[dict[str, str]],
        stream: bool,
        **kwargs: Any,
    ) -> CreateResult:
        chat = ""
        for message in messages:
            chat += "%s: %s\n" % (message["role"], message["content"])
        chat += "assistant: "

        proxy = kwargs.get("proxy")

        if proxy == True:
            proxies = fetch_proxy()
            if type(proxies) is not str:
                for p in range(len(proxies)):
                    try:
                        client = Client(timeout=180, proxies= {"http://": f"{proxies[p]}"})
                        print(f"Connection established with {proxies[p]}")
                        proxy = proxies[p]
                        break
                    except:
                        print(f"Connection failed with {proxies[p]}. Trying {p+1}/{len(proxies)} ...")
                        sleep(1)
            else:
                try:
                    client = Client(timeout=180, proxies= {"http://": f"{proxies}"})
                    print(f"Connection established with {proxies}")
                    proxy = proxies
                except:
                    print(f"Connection failed with {proxies}")
                    sleep(1)
        else:
            client = Client(timeout=180)
        
        try:
            response = client.get("https://chatgpt.ai/login/")
            response.raise_for_status()
            # nonce, post_id, _, bot_id = re.findall(
            #     r'data-nonce="(.*)"\n     data-post-id="(.*)"\n     data-url="(.*)"\n     data-bot-id="(.*)"\n     data-width',
            #     response.text,
            # )[0]
            nonce = re.findall(r'"search_nonce":"([^"]*)"', response.text)[0]
            post_id = re.findall(r'"post_id":"([^"]*)"', response.text)[0]  

            headers = {
                "authority": "chatgpt.ai",
                "accept": "*/*",
                "accept-language": "en,fr-FR;q=0.9,fr;q=0.8,es-ES;q=0.7,es;q=0.6,en-US;q=0.5,am;q=0.4,de;q=0.3",
                "cache-control": "no-cache",
                "origin": "https://chatgpt.ai",
                "pragma": "no-cache",
                "referer": "https://chatgpt.ai/gpt-4/",
                "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            }
            data = {
                "_wpnonce": nonce,
                "post_id": post_id,
                "url": "https://chatgpt.ai/gpt-4",
                "action": "wpaicg_chat_shortcode_message",
                "message":chat,
                "bot_id": "",
            }

            response = client.post(
                "https://chatgpt.ai/wp-admin/admin-ajax.php", headers=headers, data=data
            )
            response.raise_for_status()
            yield response.json()["data"]
        except Exception as e:
            print(e)
            return e


