from huggingface_hub import login

# login()

import os
os.environ["CUDA_VISIBLE_DEVICES"]="0"
import torch
import torch.nn as nn
import bitsandbytes as bnb
from transformers import AutoTokenizer, AutoConfig, AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained(
    "TheBloke/wizardLM-7B-HF"
)

tokenizer = AutoTokenizer.from_pretrained("TheBloke/wizardLM-7B-HF")

print("done")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               