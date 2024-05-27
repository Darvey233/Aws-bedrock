{"filter":false,"title":"bedrock_api.py","tooltip":"/workshop/labs/api/bedrock_api.py","undoManager":{"mark":4,"position":4,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["import json","import boto3","",""],"id":1}],[{"start":{"row":3,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["session = boto3.Session()","","bedrock = session.client(service_name='bedrock-runtime') #creates a Bedrock client","",""],"id":2}],[{"start":{"row":7,"column":0},"end":{"row":22,"column":0},"action":"insert","lines":["bedrock_model_id = \"ai21.j2-ultra-v1\" #set the foundation model","","prompt = \"What is the largest city in New Hampshire?\" #the prompt to send to the model","","body = json.dumps({","    \"prompt\": prompt, #AI21","    \"maxTokens\": 1024, ","    \"temperature\": 0, ","    \"topP\": 0.5, ","    \"stopSequences\": [], ","    \"countPenalty\": {\"scale\": 0 }, ","    \"presencePenalty\": {\"scale\": 0 }, ","    \"frequencyPenalty\": {\"scale\": 0 }","}) #build the request payload","",""],"id":3}],[{"start":{"row":22,"column":0},"end":{"row":25,"column":0},"action":"insert","lines":["","response = bedrock.invoke_model(body=body, modelId=bedrock_model_id, accept='application/json', contentType='application/json') #send the payload to Bedrock","",""],"id":4}],[{"start":{"row":25,"column":0},"end":{"row":31,"column":0},"action":"insert","lines":["response_body = json.loads(response.get('body').read()) # read the response","","response_text = response_body.get(\"completions\")[0].get(\"data\").get(\"text\") #extract the text from the JSON response","","print(response_text)","",""],"id":5}],[{"start":{"row":31,"column":0},"end":{"row":32,"column":0},"action":"insert","lines":["cd ~/environment/workshop/labs/api",""],"id":6}]]},"ace":{"folds":[],"scrolltop":74.4,"scrollleft":0,"selection":{"start":{"row":30,"column":0},"end":{"row":30,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":4,"state":"start","mode":"ace/mode/python"}},"timestamp":1716762196334,"hash":"5dd8476c3baf2bcefc970d0dca309507f76ea050"}