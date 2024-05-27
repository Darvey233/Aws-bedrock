from langchain_community.llms import Bedrock
from langchain.prompts import PromptTemplate

def get_llm():
    #Add a function to create a Bedrock LangChain client. This includes the inference parameters we want to use.
    
    model_kwargs = { #AI21
        "maxTokens": 1024, 
        "temperature": 0, 
        "topP": 0.5, 
        "stopSequences": [], 
        "countPenalty": {"scale": 0 }, 
        "presencePenalty": {"scale": 0 }, 
        "frequencyPenalty": {"scale": 0 } 
    }
    
    llm = Bedrock(
        model_id="ai21.j2-ultra-v1", #set the foundation model
        model_kwargs=model_kwargs) #configure the inference parameters
    
    return llm

def get_prompt(user_input, template):
    #Add the function to create the custom prompt. This code builds a custom prompt from the template and user input parameters.
    
    prompt_template = PromptTemplate.from_template(template) #this will automatically identify the input variables for the template

    prompt = prompt_template.format(user_input=user_input)
    
    return prompt

def get_text_response(user_input, template):
    #Add this function to call Bedrock. This function passes the custom prompt to Bedrock.
    #text-to-text client function
    llm = get_llm()
    
    prompt = get_prompt(user_input, template)
    
    return llm.invoke(prompt) #return a response to the prompt
