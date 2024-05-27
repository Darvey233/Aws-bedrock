{"filter":false,"title":"params.py","tooltip":"/workshop/labs/params/params.py","undoManager":{"mark":4,"position":4,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["import sys","from langchain_community.llms import Bedrock","",""],"id":1}],[{"start":{"row":3,"column":0},"end":{"row":62,"column":0},"action":"insert","lines":["def get_inference_parameters(model): #return a default set of parameters based on the model's provider","    bedrock_model_provider = model.split('.')[0] #grab the model provider from the first part of the model id","    ","    if (bedrock_model_provider == 'anthropic'): #Anthropic model","        return { #anthropic","            \"max_tokens\": 512,","            \"temperature\": 0, ","            \"top_k\": 250, ","            \"top_p\": 1, ","            \"stop_sequences\": [\"\\n\\nHuman:\"] ","           }","    ","    elif (bedrock_model_provider == 'ai21'): #AI21","        return { #AI21","            \"maxTokens\": 512, ","            \"temperature\": 0, ","            \"topP\": 0.5, ","            \"stopSequences\": [], ","            \"countPenalty\": {\"scale\": 0 }, ","            \"presencePenalty\": {\"scale\": 0 }, ","            \"frequencyPenalty\": {\"scale\": 0 } ","           }","    ","    elif (bedrock_model_provider == 'cohere'): #COHERE","        return {","            \"max_tokens\": 512,","            \"temperature\": 0,","            \"p\": 0.01,","            \"k\": 0,","            \"stop_sequences\": [],","            \"return_likelihoods\": \"NONE\"","        }","    ","    elif (bedrock_model_provider == 'meta'): #META","        return {","            \"temperature\": 0,","            \"top_p\": 0.9,","            \"max_gen_len\": 512","        }","    ","    elif (bedrock_model_provider == 'mistral'): #MISTRAL","        return {","            \"max_tokens\" : 512,","            \"stop\" : [],    ","            \"temperature\": 0,","            \"top_p\": 0.9,","            \"top_k\": 50","        } ","","    else: #Amazon","        #For the LangChain Bedrock implementation, these parameters will be added to the ","        #textGenerationConfig item that LangChain creates for us","        return { ","            \"maxTokenCount\": 512, ","            \"stopSequences\": [], ","            \"temperature\": 0, ","            \"topP\": 0.9 ","        }","    ",""],"id":2}],[{"start":{"row":62,"column":0},"end":{"row":73,"column":0},"action":"insert","lines":["def get_text_response(model, input_content): #text-to-text client function","    ","    model_kwargs = get_inference_parameters(model) #get the default parameters based on the selected model","    ","    llm = Bedrock( #create a Bedrock llm client","        model_id=model, #use the requested model","        model_kwargs = model_kwargs","    )","    ","    return llm.invoke(input_content) #return a response to the prompt","",""],"id":3}],[{"start":{"row":73,"column":0},"end":{"row":75,"column":0},"action":"insert","lines":["response = get_text_response(sys.argv[1], sys.argv[2])","",""],"id":4}],[{"start":{"row":75,"column":0},"end":{"row":76,"column":0},"action":"insert","lines":["print(response)",""],"id":5}]]},"ace":{"folds":[],"scrolltop":862.1999999999999,"scrollleft":0,"selection":{"start":{"row":76,"column":0},"end":{"row":76,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1716763294078,"hash":"3c828e213eba7276904aad7e8bad07a06820557b"}