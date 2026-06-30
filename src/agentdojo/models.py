from agentdojo.strenum import StrEnum


class ModelsEnum(StrEnum):
    """Currently supported models."""
    GPT_4O_2024_05_13 = "gpt-4o-2024-05-13"
    GPT_5_4_MINI = "gpt-5.4-mini-2026-03-17"
    """GPT-5.4 Mini — Azure Foundry"""
    CLAUDE_SONNET_4_6 = "claude-sonnet-4-6"
    """Claude Sonnet 4.6 — Azure Foundry"""
    DEEPSEEK_V3_2 = "DeepSeek-V3.2"
    """DeepSeek V3.2 — Azure Foundry"""
    GROK_4 = "grok-4-20-non-reasoning"
    """Grok 4 — Azure Foundry"""
    GPT_4_1_MINI = "gpt-4.1-mini-2025-04-14"
    """GPT-4.1 Mini — Azure Foundry"""
    GPT_5_5 = "gpt-5.5-2026-04-24"
    """GPT-5.5 — Azure Foundry"""
    """GPT-4o"""
    GPT_4O_MINI_2024_07_18 = "gpt-4o-mini-2024-07-18"
    """GPT-4o Mini"""
    GPT_4_0125_PREVIEW = "gpt-4-0125-preview"
    """GPT-4 Turbo Preview 0125"""
    GPT_3_5_TURBO_0125 = "gpt-3.5-turbo-0125"
    """GPT-3.5 Turbo 0125"""
    GPT_4_TURBO_2024_04_09 = "gpt-4-turbo-2024-04-09"
    """GPT-4 Turbo"""
    CLAUDE_3_OPUS_20240229 = "claude-3-opus-20240229"
    """Claude 3 Opus"""
    CLAUDE_3_SONNET_20240229 = "claude-3-sonnet-20240229"
    """Claude 3 Sonnet"""
    CLAUDE_3_5_SONNET_20240620 = "claude-3-5-sonnet-20240620"
    """Claude 3.5 Sonnet"""
    CLAUDE_3_5_SONNET_20241022 = "claude-3-5-sonnet-20241022"
    """Claude 3.5 Sonnet October"""
    CLAUDE_3_7_SONNET_20250219 = "claude-3-7-sonnet-20250219"
    """Claude 3.7 Sonnet"""
    CLAUDE_3_7_SONNET_20250219_THINKING_16000 = "claude-3-7-sonnet-20250219-thinking-16000"
    """Claude 3.7 Sonnet"""
    CLAUDE_3_HAIKU_20240307 = "claude-3-haiku-20240307"
    """Claude 3 Haiku"""
    COMMAND_R_PLUS = "command-r-plus"
    """Command R Plus"""
    COMMAND_R = "command-r"
    """Command R"""
    MISTRALAI_MIXTRAL_8X7B_INSTRUCT_V0_1 = "mistralai/Mixtral-8x7B-Instruct-v0.1"
    """MistralAI Mixtral 8x7B Instruct v0.1"""
    LLAMA_3 = "meta-llama/Llama-3-70b-chat-hf"
    """Llama 3"""
    GEMINI_1_5_PRO_002 = "gemini-1.5-pro-002"
    """Gemini 1.5 Pro 002"""
    GEMINI_1_5_PRO_001 = "gemini-1.5-pro-001"
    """Gemini 1.5 Pro 001"""
    GEMINI_1_5_FLASH_002 = "gemini-1.5-flash-002"
    """Gemini 1.5 Flash 002"""
    GEMINI_1_5_FLASH_001 = "gemini-1.5-flash-001"
    """Gemini 1.5 Flash 001"""
    GEMINI_2_0_FLASH_EXP = "gemini-2.0-flash-exp"
    """Gemini 2.0 Flash Exp"""
    GEMINI_2_0_FLASH_001 = "gemini-2.0-flash-001"
    """Gemini 2.0 Flash 001"""
    GEMINI_2_5_FLASH_PREVIEW_04_17 = "gemini-2.5-flash-preview-04-17"
    """Gemini 2.5 Flash Preview 04/17"""
    GEMINI_2_5_PRO_PREVIEW_05_06 = "gemini-2.5-pro-preview-05-06"
    """Gemini 2.5 Pro Preview 05/06"""
    LOCAL = "local"
    """Local model"""
    VLLM_PARSED = "vllm_parsed"
    """VLLM parsed model"""
    OPENAI_COMPATIBLE = "openai-compatible"
    CLAUDE_OPUS_4_8 = "claude-opus-4-8"
    GROK_4_3 = "grok-4.3"
    """Grok 4.3 — Azure Foundry"""
    """Claude Opus 4.8 — Azure Foundry"""
    """OpenAI-compatible endpoint (set OPENAI_COMPATIBLE_BASE_URL and OPENAI_COMPATIBLE_API_KEY)"""


MODEL_PROVIDERS = {
    ModelsEnum.GPT_4O_2024_05_13: "openai",
    ModelsEnum.GPT_4O_MINI_2024_07_18: "openai",
    ModelsEnum.GPT_3_5_TURBO_0125: "openai",
    ModelsEnum.GPT_4_0125_PREVIEW: "openai",
    ModelsEnum.GPT_4_TURBO_2024_04_09: "openai",
    ModelsEnum.CLAUDE_3_OPUS_20240229: "anthropic",
    ModelsEnum.CLAUDE_3_SONNET_20240229: "anthropic",
    ModelsEnum.CLAUDE_3_5_SONNET_20240620: "anthropic",
    ModelsEnum.CLAUDE_3_5_SONNET_20241022: "anthropic",
    ModelsEnum.CLAUDE_3_7_SONNET_20250219: "anthropic",
    ModelsEnum.CLAUDE_3_7_SONNET_20250219_THINKING_16000: "anthropic",
    ModelsEnum.CLAUDE_3_HAIKU_20240307: "anthropic",
    ModelsEnum.COMMAND_R_PLUS: "cohere",
    ModelsEnum.COMMAND_R: "cohere",
    ModelsEnum.MISTRALAI_MIXTRAL_8X7B_INSTRUCT_V0_1: "together",
    ModelsEnum.LLAMA_3: "together-prompting",
    ModelsEnum.GEMINI_1_5_PRO_001: "google",
    ModelsEnum.GEMINI_1_5_PRO_002: "google",
    ModelsEnum.GEMINI_1_5_FLASH_001: "google",
    ModelsEnum.GEMINI_1_5_FLASH_002: "google",
    ModelsEnum.GEMINI_2_0_FLASH_EXP: "google",
    ModelsEnum.GEMINI_2_0_FLASH_001: "google",
    ModelsEnum.GEMINI_2_5_FLASH_PREVIEW_04_17: "google",
    ModelsEnum.GEMINI_2_5_PRO_PREVIEW_05_06: "google",
    ModelsEnum.LOCAL: "local",
    ModelsEnum.VLLM_PARSED: "vllm_parsed",
    ModelsEnum.OPENAI_COMPATIBLE: "openai-compatible",
    ModelsEnum.CLAUDE_OPUS_4_8: "anthropic",
    ModelsEnum.GROK_4_3: "openai-compatible",
    ModelsEnum.GPT_5_4_MINI:    "openai-compatible",
    ModelsEnum.CLAUDE_SONNET_4_6: "openai-compatible",
    ModelsEnum.DEEPSEEK_V3_2:   "openai-compatible",
    ModelsEnum.GROK_4:          "openai-compatible",
    ModelsEnum.GPT_4_1_MINI:    "openai-compatible",
    ModelsEnum.GPT_5_5:         "openai-compatible",
}


MODEL_NAMES = {
    "gpt-4o-2024-05-13": "GPT-4",
    "gpt-4o-mini-2024-07-18": "GPT-4",
    "gpt-3.5-turbo-0125": "GPT-3.5",
    "gpt-4-turbo-2024-04-09": "GPT-4",
    "gpt-4-0125-preview": "GPT-4",
    "claude-3-opus-20240229": "Claude",
    "claude-3-sonnet-20240229": "Claude",
    "claude-3-5-sonnet-20240620": "Claude",
    "claude-3-5-sonnet-20241022": "Claude",
    "claude-3-7-sonnet-20250219": "Claude",
    "claude-3-7-sonnet-20250219-thinking-16000": "Claude",
    "claude-3-haiku-20240307": "Claude",
    "command-r-plus": "Command R+",
    "command-r": "Command R",
    "mistralai/Mixtral-8x7B-Instruct-v0.1": "Mixtral",
    "meta-llama/Llama-3-70b-chat-hf": "AI assistant",
    "gemini-1.5-pro-002": "AI model developed by Google",
    "gemini-1.5-pro-001": "AI model developed by Google",
    "gemini-1.5-flash-002": "AI model developed by Google",
    "gemini-1.5-flash-001": "AI model developed by Google",
    "gemini-2.0-flash-exp": "AI model developed by Google",
    "gemini-2.0-flash-001": "AI model developed by Google",
    "gemini-2.5-flash-preview-04-17": "AI model developed by Google",
    "gemini-2.5-pro-preview-05-06": "AI model developed by Google",
    "local": "Local model",
    "vllm_parsed": "Local model",
    "openai-compatible": "AI assistant",
    "claude-opus-4-8": "Claude",
    "grok-4.3": "Grok",
    "gpt-5.4-mini-2026-03-17":     "GPT-5.4-mini",
    "claude-sonnet-4-6":            "Claude Sonnet 4.6",
    "DeepSeek-V3.2":               "DeepSeek",
    "grok-4-20-non-reasoning":      "Grok 4",
    "gpt-4.1-mini-2025-04-14":     "GPT-4.1-mini",
    "gpt-5.5-2026-04-24":          "GPT-5.5",
}
