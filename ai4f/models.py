from dataclasses import dataclass

from .Provider import Bard, BaseProvider, GetGpt, H2o, Liaobots, Vercel, Equing, Poe


@dataclass
class Model:
    name: str
    base_provider: str
    best_provider: type[BaseProvider]


# GPT-3.5 / GPT-4
gpt_35_turbo = Model(
    name="gpt-3.5-turbo",
    base_provider="openai",
    best_provider=GetGpt,
)

gpt_4 = Model(
    name="gpt-4",
    base_provider="openai",
    best_provider=Liaobots,
)

# Bard
palm = Model(
    name="palm",
    base_provider="google",
    best_provider=Bard,
)

# H2o
falcon_7b = Model(
    name="h2oai/h2ogpt-gm-oasst1-en-2048-falcon-7b-v3",
    base_provider="huggingface",
    best_provider=H2o,
)

falcon_40b = Model(
    name="h2oai/h2ogpt-gm-oasst1-en-2048-falcon-40b-v1",
    base_provider="huggingface",
    best_provider=H2o,
)

llama_13b = Model(
    name="h2oai/h2ogpt-gm-oasst1-en-2048-open-llama-13b",
    base_provider="huggingface",
    best_provider=H2o,
)

# Vercel
claude_instant_v1 = Model(
    name="anthropic:claude-instant-v1",
    base_provider="anthropic",
    best_provider=Vercel,
)

claude_v1 = Model(
    name="anthropic:claude-v1",
    base_provider="anthropic",
    best_provider=Vercel,
)

claude_v2 = Model(
    name="anthropic:claude-v2",
    base_provider="anthropic",
    best_provider=Vercel,
)

command_light_nightly = Model(
    name="cohere:command-light-nightly",
    base_provider="cohere",
    best_provider=Vercel,
)

command_nightly = Model(
    name="cohere:command-nightly",
    base_provider="cohere",
    best_provider=Vercel,
)

gpt_neox_20b = Model(
    name="huggingface:EleutherAI/gpt-neox-20b",
    base_provider="huggingface",
    best_provider=Vercel,
)

oasst_sft_1_pythia_12b = Model(
    name="huggingface:OpenAssistant/oasst-sft-1-pythia-12b",
    base_provider="huggingface",
    best_provider=Vercel,
)

oasst_sft_4_pythia_12b_epoch_35 = Model(
    name="huggingface:OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5",
    base_provider="huggingface",
    best_provider=Vercel,
)

santacoder = Model(
    name="huggingface:bigcode/santacoder",
    base_provider="huggingface",
    best_provider=Vercel,
)

bloom = Model(
    name="huggingface:bigscience/bloom",
    base_provider="huggingface",
    best_provider=Vercel,
)

flan_t5_xxl = Model(
    name="huggingface:google/flan-t5-xxl",
    base_provider="huggingface",
    best_provider=Vercel,
)

code_davinci_002 = Model(
    name="openai:code-davinci-002",
    base_provider="openai",
    best_provider=Vercel,
)

gpt_35_turbo_16k = Model(
    name="openai:gpt-3.5-turbo-16k",
    base_provider="openai",
    best_provider=Vercel,
)

gpt_35_turbo_16k_0613 = Model(
    name="openai:gpt-3.5-turbo-16k-0613",
    base_provider="openai",
    best_provider=Equing,
)

gpt_4_0613 = Model(
    name="openai:gpt-4-0613",
    base_provider="openai",
    best_provider=Vercel,
)

text_ada_001 = Model(
    name="openai:text-ada-001",
    base_provider="openai",
    best_provider=Vercel,
)

text_babbage_001 = Model(
    name="openai:text-babbage-001",
    base_provider="openai",
    best_provider=Vercel,
)

text_curie_001 = Model(
    name="openai:text-curie-001",
    base_provider="openai",
    best_provider=Vercel,
)

text_davinci_002 = Model(
    name="openai:text-davinci-002",
    base_provider="openai",
    best_provider=Vercel,
)

text_davinci_003 = Model(
    name="openai:text-davinci-003",
    base_provider="openai",
    best_provider=Vercel,
)

llama13b_v2_chat = Model(
    name="replicate:a16z-infra/llama13b-v2-chat",
    base_provider="replicate",
    best_provider=Vercel,
)

llama7b_v2_chat = Model(
    name="replicate:a16z-infra/llama7b-v2-chat",
    base_provider="replicate",
    best_provider=Vercel,
)

# Quora Poe
models = {
    'sage-assistant': 'capybara',
    'claude-instant-v1-100k': 'a2_100k',
    'claude-v2-100k': 'a2_2',
    'claude-instant-v1': 'a2',
    'gpt-3.5-turbo':'chinchilla',
    'gpt-3.5-turbo-16k': 'agouti',
    'gpt-4': 'beaver',
    'gpt-4-32k': 'vizcacha',
    'palm': 'acouchy',
    'llama-2-7b': 'llama_2_7b_chat',
    'llama-2-13b': 'llama_2_13b_chat',
    'llama-2-70b': 'llama_2_70b_chat',
}

sage_assistant = Model(
    name="sage-assistant",
    base_provider="openai",
    best_provider=Poe,
)

llama_2_7b = Model(
    name="llama-2-7b",
    base_provider="meta",
    best_provider=Poe,
)


class ModelUtils:
    convert: dict[str, Model] = {
        # GPT-3.5 / GPT-4
        "gpt-3.5-turbo": gpt_35_turbo,
        "gpt-4": gpt_4,
        # Bard
        "palm2": palm,
        "palm": palm,
        "google": palm,
        "google-bard": palm,
        "google-palm": palm,
        "bard": palm,
        # H2o
        "falcon-40b": falcon_40b,
        "falcon-7b": falcon_7b,
        "llama-13b": llama_13b,
        # Vercel
        "claude-instant-v1": claude_instant_v1,
        "claude-v1": claude_v1,
        "claude-v2": claude_v2,
        "command-light-nightly": command_light_nightly,
        "command-nightly": command_nightly,
        "gpt-neox-20b": gpt_neox_20b,
        "oasst-sft-1-pythia-12b": oasst_sft_1_pythia_12b,
        "oasst-sft-4-pythia-12b-epoch-3.5": oasst_sft_4_pythia_12b_epoch_35,
        "santacoder": santacoder,
        "bloom": bloom,
        "flan-t5-xxl": flan_t5_xxl,
        "code-davinci-002": code_davinci_002,
        "gpt-3.5-turbo-16k": gpt_35_turbo_16k,
        "gpt-3.5-turbo-16k-0613": gpt_35_turbo_16k_0613,
        "gpt-4-0613": gpt_4_0613,
        "text-ada-001": text_ada_001,
        "text-babbage-001": text_babbage_001,
        "text-curie-001": text_curie_001,
        "text-davinci-002": text_davinci_002,
        "text-davinci-003": text_davinci_003,
        "llama13b-v2-chat": llama13b_v2_chat,
        "llama7b-v2-chat": llama7b_v2_chat,
        # Quora Poe
        "llama-2-7b": llama_2_7b,
    }
