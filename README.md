# AI 4 FREE
By using this repository or any code related to it, you agree to the [legal notice](./LEGAL_NOTICE.md). The author is not responsible for any copies, forks, or reuploads made by other users. This is the author's only account and repository. To prevent impersonation or irresponsible actions, you may comply with the GNU GPL license this Repository uses.

This (quite censored) New Version of gpt4free, was just released, it may contain bugs, open an issue or contribute a PR when encountering one, some features were disabled.
Docker is for now not available but I would be happy if someone contributes a PR. The g4f GUI will be uploaded soon enough.

### New
- pypi package:
```
pip install -U ai4f
```

## Table of Contents:

- [Getting Started](#getting-started)
    + [Prerequisites](#prerequisites)
    + [Setting up the project](#setting-up-the-project)
- [Usage](#usage)
  * [The `g4f` Package](#the-g4f-package)
  * [interference openai-proxy api](#interference-openai-proxy-api-use-with-openai-python-package)
- [Models](#models)
  * [gpt-3.5 / gpt-4](#gpt-35--gpt-4)
  * [Other Models](#other-models)
- [Related gpt4free projects](#related-gpt4free-projects)
- [Contribute](#contribute)
- [ChatGPT clone](#chatgpt-clone)
- [Copyright](#copyright)
- [Copyright Notice](#copyright-notice)
- [Star History](#star-history)

## Getting Started

#### Prerequisites:
1. [Download and install Python](https://www.python.org/downloads/) (Version 3.x is recommended).

#### Setting up the project:
##### Install using pypi
```
pip install -U ai4f
```

##### or

1. Clone the GitHub repository: 
```
git clone https://github.com/hansfzlorenzana/AI-4-Free.git
```
2. Navigate to the project directory:
```
cd AI-4-Free
```
3. (Recommended) Create a virtual environment to manage Python packages for your project:
```
python3 -m venv venv
```
4. Activate the virtual environment:
   - On Windows:
   ```
   .\venv\Scripts\activate
   ```
   - On macOS and Linux:
   ```
   source venv/bin/activate
   ```
5. Install the required Python packages from `requirements.txt`:
```
pip install -r requirements.txt
```

6. Create a `test.py` file in the root folder and start using the repo, further Instructions are below
```py
import ai4f

...
```

## Usage

### The `ai4f` Package
```py
import ai4f


print(ai4f.Provider.Ails.params) # supported args

# Automatic selection of provider

# streamed completion
response = ai4f.ChatCompletion.create(model='gpt-3.5-turbo', messages=[
                                     {"role": "user", "content": "Hello world"}], stream=True)

for message in response:
    print(message)

# normal response
response = ai4f.ChatCompletion.create(model=ai4f.models.gpt_4, messages=[
                                     {"role": "user", "content": "hi"}]) # alterative model setting

print(response)


# Set with provider
response = ai4f.ChatCompletion.create(model='gpt-3.5-turbo', provider=ai4f.Provider.Forefront, messages=[
                                     {"role": "user", "content": "Hello world"}], stream=True)

for message in response:
    print(message)
```

providers:
```py
from ai4f.Provider import (
    Ails,
    You,
    Bing,
    Yqcloud,
    Theb,
    Aichat,
    Bard,
    Vercel,
    Forefront,
    Lockchat,
    Liaobots,
    H2o,
    ChatgptLogin,
    DeepAi,
    GetGpt,
    AItianhu,
    EasyChat,
    Acytoo,
    DfeHub,
    AiService,
    BingHuan,
    Wewordle,
    ChatgptAi,
    opchatgpts,
    Poe,
)

# usage:
response = ai4f.ChatCompletion.create(..., provider=ProviderName)
```

### interference openai-proxy api (use with openai python package)    

run server:
```sh
python3 -m interference.app
```

```py
import openai

openai.api_key = ''
openai.api_base = 'http://127.0.0.1:1337'

chat_completion = openai.ChatCompletion.create(stream=True,
    model='gpt-3.5-turbo', messages=[{'role': 'user', 'content': 'write a poem about a tree'}])

#print(chat_completion.choices[0].message.content)

for token in chat_completion:
    
    content = token['choices'][0]['delta'].get('content')
    if content != None:
        print(content)
```

## Models    
### gpt-3.5 / gpt-4

| Website| Provider| gpt-3.5 | gpt-4 | others | Stream | Status | Auth |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [ai.ls](https://ai.ls) | `g4f.Provider.Ails` | ✔️ | ❌ | ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [you.com](https://you.com) | `g4f.Provider.You` | ✔️ | ❌ |  ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [bing.com](https://bing.com/chat) | `g4f.Provider.Bing` | ❌ | ✔️ |  ❌ |✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [chat9.yqcloud.top](https://chat9.yqcloud.top/) | `g4f.Provider.Yqcloud` | ✔️ | ❌ | ❌ |✔️ |![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [theb.ai](https://theb.ai) | `g4f.Provider.Theb` | ✔️ | ❌ | ❌ | ✔️ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [chat-gpt.org](https://chat-gpt.org/chat) | `g4f.Provider.Aichat` | ✔️ | ❌ | ❌ |❌ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [bard.google.com](https://bard.google.com) | `g4f.Provider.Bard` | ❌ | ❌ |  ✔️ |❌ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ✔️ |
| [play.vercel.ai](https://play.vercel.ai) | `g4f.Provider.Vercel` | ✔️ | ❌ | ✔️ | ✔️ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [forefront.com](https://forefront.com) | `g4f.Provider.Forefront` | ✔️ | ❌ |  ❌ | ✔️ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [supertest.lockchat.app](http://supertest.lockchat.app) | `g4f.Provider.Lockchat` | ✔️ | ✔️ | ❌ | ✔️ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [liaobots.com](https://liaobots.com) | `g4f.Provider.Liaobots` | ✔️ | ✔️ |  ❌ | ✔️ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ✔️ |
| [gpt-gm.h2o.ai](https://gpt-gm.h2o.ai) | `g4f.Provider.H2o` | ❌ | ❌ | ✔️ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [chatgptlogin.ac](https://chatgptlogin.ac) | `g4f.Provider.ChatgptLogin` | ✔️ | ❌ |  ❌ | ❌ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [deepai.org](https://deepai.org) | `g4f.Provider.DeepAi` | ✔️ | ❌ |  ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [chat.getgpt.world](https://chat.getgpt.world/) | `g4f.Provider.GetGpt` | ✔️ | ❌ |  ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [www.aitianhu.com](https://www.aitianhu.com/api/chat-process) | `g4f.Provider.AItianhu` | ✔️ | ❌ | ❌ | ❌ |![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [free.easychat.work](https://free.easychat.work) | `g4f.Provider.EasyChat` | ✔️ | ❌ |  ❌ |✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [chat.acytoo.com](https://chat.acytoo.com/api/completions) | `g4f.Provider.Acytoo` | ✔️ | ❌ |  ❌ |❌ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [chat.dfehub.com](https://chat.dfehub.com/api/chat) | `g4f.Provider.DfeHub` | ✔️ | ❌ | ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [aiservice.vercel.app](https://aiservice.vercel.app/api/chat/answer) | `g4f.Provider.AiService` | ✔️ | ❌ | ❌ | ❌ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [b.ai-huan.xyz](https://b.ai-huan.xyz) | `g4f.Provider.BingHuan` | ✔️ | ✔️ |  ❌ |✔️ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [wewordle.org](https://wewordle.org/gptapi/v1/android/turbo) | `g4f.Provider.Wewordle` | ✔️ | ❌ | ❌ | ❌ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [chatgpt.ai](https://chatgpt.ai/gpt-4/) | `g4f.Provider.ChatgptAi` | ❌ | ✔️ |  ❌ |❌ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [opchatgpts.net](https://opchatgpts.net) | `g4f.Provider.opchatgpts` | ✔️ | ❌ | ❌ | ❌ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [poe.com](https://poe.com) | `g4f.Provider.Poe` |  ✔️  |   ✔️  | ✔️ |  ✔️ |  ![Active](https://img.shields.io/badge/Active-brightgreen) |  ✔️  |


### Other Models

| Model| Base Provider | Provider | Website |
| ------- | ----------- | ---- |---- |
| palm2 | Google | `g4f.Provider.Bard` | [Google Bard](https://bard.google.com/) |
| sage-assistant | Quora | `g4f.Provider.Poe` | [Quora Poe](https://poe.com/) |
| claude-instant-v1-100k | Anthropic | `g4f.Provider.Poe` | [Quora Poe](https://poe.com/) |
| claude-v2-100k | Anthropic | `g4f.Provider.Poe` | [Quora Poe](https://poe.com/) |
| claude-instant-v1 | Anthropic | `g4f.Provider.Poe` | [Quora Poe](https://poe.com/) |
| gpt-3.5-turbo-16k | OpenAI | `g4f.Provider.Poe` | [Quora Poe](https://poe.com/) |
| gpt-4-32k | OpenAI | `g4f.Provider.Poe` | [Quora Poe](https://poe.com/) |
| llama-2-7b | Meta AI | `g4f.Provider.Poe` | [Quora Poe](https://poe.com/) |
| llama-2-13b | Meta AI | `g4f.Provider.Poe` | [Quora Poe](https://poe.com/) |
| llama-2-70b | Meta AI | `g4f.Provider.Poe` | [Quora Poe](https://poe.com/) |
| falcon-40b | Huggingface | `g4f.Provider.H2o` | [H2o](https://www.h2o.ai/) |
| falcon-7b | Huggingface |`g4f.Provider.H2o` | [H2o](https://www.h2o.ai/) |
| llama-13b | Huggingface | `g4f.Provider.H2o`| [H2o](https://www.h2o.ai/) |
| claude-instant-v1-100k | Anthropic | `g4f.Provider.Vercel` | [sdk.vercel.ai](https://sdk.vercel.ai/) |
| claude-instant-v1 | Anthropic | `g4f.Provider.Vercel` | [sdk.vercel.ai](https://sdk.vercel.ai/) |
| claude-v1-100k | Anthropic | `g4f.Provider.Vercel` | [sdk.vercel.ai](https://sdk.vercel.ai/) |
| claude-v1 | Anthropic | `g4f.Provider.Vercel` | [sdk.vercel.ai](https://sdk.vercel.ai/) |
| alpaca-7b | Replicate | `g4f.Provider.Vercel` | [sdk.vercel.ai](https://sdk.vercel.ai/) |
| stablelm-tuned-alpha-7b | Replicate | `g4f.Provider.Vercel` | [sdk.vercel.ai](https://sdk.vercel.ai/) |
| bloom | Huggingface | `g4f.Provider.Vercel` | [sdk.vercel.ai](https://sdk.vercel.ai/) |
| bloomz | Huggingface | `g4f.Provider.Vercel` | [sdk.vercel.ai](https://sdk.vercel.ai/) |
| flan-t5-xxl | Huggingface | `g4f.Provider.Vercel` | [sdk.vercel.ai](https://sdk.vercel.ai/) |
| flan-ul2 | Huggingface | `g4f.Provider.Vercel` | [sdk.vercel.ai](https://sdk.vercel.ai/) |
| gpt-neox-20b | Huggingface | `g4f.Provider.Vercel` | [sdk.vercel.ai](https://sdk.vercel.ai/) |
| oasst-sft-4-pythia-12b-epoch-3.5 |Huggingface | `g4f.Provider.Vercel` | [sdk.vercel.ai](https://sdk.vercel.ai/) |
| santacoder | Huggingface | `g4f.Provider.Vercel` | [sdk.vercel.ai](https://sdk.vercel.ai/) |
| command-medium-nightly | Cohere | `g4f.Provider.Vercel` | [sdk.vercel.ai](https://sdk.vercel.ai/) |
| command-xlarge-nightly | Cohere | `g4f.Provider.Vercel` | [sdk.vercel.ai](https://sdk.vercel.ai/) |
| code-cushman-001 | OpenAI | `g4f.Provider.Vercel` | [sdk.vercel.ai](https://sdk.vercel.ai/) |
| code-davinci-002 | OpenAI | `g4f.Provider.Vercel` | [sdk.vercel.ai](https://sdk.vercel.ai/) |
| text-ada-001 | OpenAI | `g4f.Provider.Vercel` | [sdk.vercel.ai](https://sdk.vercel.ai/) |
| text-babbage-001 | OpenAI | `g4f.Provider.Vercel` | [sdk.vercel.ai](https://sdk.vercel.ai/) |
| text-curie-001 | OpenAI | `g4f.Provider.Vercel` | [sdk.vercel.ai](https://sdk.vercel.ai/) |
| text-davinci-002 | OpenAI | `g4f.Provider.Vercel` | [sdk.vercel.ai](https://sdk.vercel.ai/) |
| text-davinci-003 | OpenAI | `g4f.Provider.Vercel` | [sdk.vercel.ai](https://sdk.vercel.ai/) |

## Related AI-4Free projects

<table>
  <thead align="center">
    <tr border: none;>
      <td><b>🎁 Projects</b></td>
      <td><b>⭐ Stars</b></td>
      <td><b>📚 Forks</b></td>
      <td><b>🛎 Issues</b></td>
      <td><b>📬 Pull requests</b></td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="https://github.com/xtekky/gpt4free"><b>gpt4free</b></a></td>
      <td><a href="https://github.com/xtekky/gpt4free/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/xtekky/gpt4free?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/xtekky/gpt4free/network/members"><img alt="Forks" src="https://img.shields.io/github/forks/xtekky/gpt4free?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/xtekky/gpt4free/issues"><img alt="Issues" src="https://img.shields.io/github/issues/xtekky/gpt4free?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/xtekky/gpt4free/pulls"><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/xtekky/gpt4free?style=flat-square&labelColor=343b41"/></a></td>
    </tr>
    <tr>
      <td><a href="https://github.com/Ruu3f/freeGPT"><b>freeGPT</b></a></td>
      <td><a href="https://github.com/Ruu3f/freeGPT/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/Ruu3f/freeGPT?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/Ruu3f/freeGPT/network/members"><img alt="Forks" src="https://img.shields.io/github/forks/Ruu3f/freeGPT?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/Ruu3f/freeGPT/issues"><img alt="Issues" src="https://img.shields.io/github/issues/Ruu3f/freeGPT?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/Ruu3f/freeGPT/pulls"><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/Ruu3f/freeGPT?style=flat-square&labelColor=343b41"/></a></td>
    </tr>
    <tr>
      <td><a href="https://github.com/snowby666/poe-api-wrapper"><b>Poe API Wrapper</b></a></td>
      <td><a href="https://github.com/snowby666/poe-api-wrapper/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/snowby666/poe-api-wrapper?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/snowby666/poe-api-wrapper/network/members"><img alt="Forks" src="https://img.shields.io/github/forks/snowby666/poe-api-wrapper?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/snowby666/poe-api-wrapper/issues"><img alt="Issues" src="https://img.shields.io/github/issues/snowby666/poe-api-wrapper?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/snowby666/poe-api-wrapper/pulls"><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/snowby666/poe-api-wrapper?style=flat-square&labelColor=343b41"/></a></td>
    </tr>
    <tr>
      <td><a href="https://github.com/acheong08/EdgeGPT"><b>Edge GPT</b></a></td>
      <td><a href="https://github.com/acheong08/EdgeGPT/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/acheong08/EdgeGPT?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/acheong08/EdgeGPT/network/members"><img alt="Forks" src="https://img.shields.io/github/forks/acheong08/EdgeGPT?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/acheong08/EdgeGPT/issues"><img alt="Issues" src="https://img.shields.io/github/issues/acheong08/EdgeGPT?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/acheong08/EdgeGPT/pulls"><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/acheong08/EdgeGPT?style=flat-square&labelColor=343b41"/></a></td>
    </tr>
    <tr>
      <td><a href="https://github.com/acheong08/Bard"><b>Bard Reversed</b></a></td>
      <td><a href="https://github.com/acheong08/Bard/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/acheong08/Bard?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/acheong08/Bard/network/members"><img alt="Forks" src="https://img.shields.io/github/forks/acheong08/Bard?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/acheong08/Bard/issues"><img alt="Issues" src="https://img.shields.io/github/issues/acheong08/Bard?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/acheong08/Bard/pulls"><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/acheong08/Bard?style=flat-square&labelColor=343b41"/></a></td>
    </tr>
    <tr>
      <td><a href="https://github.com/acheong08/ChatGPT"><b>ChatGPT Reversed</b></a></td>
      <td><a href="https://github.com/acheong08/ChatGPT/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/acheong08/ChatGPT?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/acheong08/ChatGPT/network/members"><img alt="Forks" src="https://img.shields.io/github/forks/acheong08/ChatGPT?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/acheong08/ChatGPT/issues"><img alt="Issues" src="https://img.shields.io/github/issues/acheong08/ChatGPT?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/acheong08/ChatGPT/pulls"><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/acheong08/ChatGPT?style=flat-square&labelColor=343b41"/></a></td>
    </tr>
    <tr>
      <td><a href="https://github.com/ading2210/poe-api"><b>Python Poe API</b></a></td>
      <td><a href="https://github.com/ading2210/poe-api/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/ading2210/poe-api?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/ading2210/poe-api/network/members"><img alt="Forks" src="https://img.shields.io/github/forks/ading2210/poe-api?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/ading2210/poe-api/issues"><img alt="Issues" src="https://img.shields.io/github/issues/ading2210/poe-api?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/ading2210/poe-api/pulls"><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/ading2210/poe-api?style=flat-square&labelColor=343b41"/></a></td>
    </tr>
  </tbody>
</table>

## Contribute

to add another provider, its very simple:
1. create a new file in [ai4f/Provider/Providers](./ai4f/Provider/Providers) with the name of the Provider
2. in the file, paste the *Boilerplate* you can find in [ai4f/Provider/Provider.py](./ai4f/Provider/Provider.py): 

```py
import os
from ..typing import sha256, Dict, get_type_hints

url = None
model = None
supports_stream = False
needs_auth = False

def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    return


params = f'ai4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join(
        [f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])

```

3. Here, you can adjust the settings, for example if the website does support streaming, set `supports_stream` to `True`...
4. Write code to request the provider in `_create_completion` and `yield` the response, *even if* its a one-time response, do not hesitate to look at other providers for inspiration
5. Add the Provider Name in [ai4f/Provider/__init__.py](./ai4f/Provider/__init__.py)

```py
from . import Provider
from .Providers import (
    ...,
    ProviderNameHere
)
```

6. You are done !, test the provider by calling it:
```py
import ai4f

response = ai4f.ChatCompletion.create(model='gpt-3.5-turbo', provider=ai4f.Provider.PROVIDERNAME,
                                    messages=[{"role": "user", "content": "test"}], stream=g4f.Provider.PROVIDERNAME.supports_stream)

for message in response:
    print(message, flush=True, end='')
```

## Copyright:

This program is licensed under the [GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.txt)

## Copyright Notice:

```
hansfzlorenzana/AI-4-Free: Copyright (C) 2023 hansfzlorenzana

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```


## Star History

<a href="https://github.com/hansfzlorenzana/AI-4-Free/stargazers">
        <img width="500" alt="Star History Chart" src="https://api.star-history.com/svg?repos=hansfzlorenzana/AI-4-Free&type=Date">
      </a> 
