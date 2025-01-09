import os 
from transformers import (
    GPT2LMHeadModel,
    GPT2Tokenizer,
    pipeline,
    PreTrainedModel,
    PretrainedConfig,
    AutoTokenizer,
    AutoModel,
    AutoConfig
)

tokenku = AutoTokenizer.from_pretrained('optimized-gpt2-2b')
configkun = AutoConfig.from_pretrained(pretrained_model_name_or_path='./optimized-gpt2-2b/',
                                       trust_remote_code=True,
                                       )

rizal = PreTrainedModel(config=configkun)
# print(help(pipeline))

pipeku = pipeline(task='text-generation',model=rizal,device="cpu")
print(pipeku)
# # print(help(pipeline))
# pl_text = pipeline(model='distributed/optimized-gpt2-2b',trust_remote_code=True,
#                    model_kwargs={"cache_dir":"./model_machine_learning"}
#                   )
# Load tokenizer and model
# tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
# model = GPT2LMHeadModel.from_pretrained(
#     "gpt2",
#     cache_dir="./model_machine_learning"
# )
# # Example usage
# text = "Hello, how are you?"
# inputs = tokenizer(text, return_tensors="pt")
# outputs = model(**inputs)
# print(outputs)
