{"filter":false,"title":"image_insertion_lib.py","tooltip":"/workshop/labs/image_insertion/image_insertion_lib.py","undoManager":{"mark":13,"position":13,"stack":[[{"start":{"row":0,"column":0},"end":{"row":31,"column":0},"action":"insert","lines":["import boto3","import json","import base64","from PIL import Image","from io import BytesIO","from random import randint","","","#get a BytesIO object from file bytes","def get_bytesio_from_bytes(image_bytes):","    image_io = BytesIO(image_bytes)","    return image_io","","","#get a base64-encoded PNG image from an Image object","def get_png_base64(image):","    png_io = BytesIO()","    image.save(png_io, format=\"PNG\")","    img_str = base64.b64encode(png_io.getvalue()).decode(\"utf-8\")","    return img_str","","","#get an Image object from file bytes","def get_image_from_bytes(image_bytes):","    ","    image_io = BytesIO(image_bytes)","    ","    image = Image.open(image_io)","    ","    return image","",""],"id":1}],[{"start":{"row":31,"column":0},"end":{"row":32,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":32,"column":0},"end":{"row":49,"column":0},"action":"insert","lines":["#Get an inpainting or outpainting mask for the provided dimensions","def get_mask_image_base64(target_width, target_height, position, inside_width, inside_height):","    ","    inside_color_value = (0, 0, 0) #inside is black - this is the masked area","    outside_color_value = (255, 255, 255)","    ","    mask_image = Image.new(\"RGB\", (target_width, target_height), outside_color_value)","    original_image_shape = Image.new(","        \"RGB\", (inside_width, inside_height), inside_color_value","    )","    mask_image.paste(original_image_shape, position)","    mask_image_base64 = get_png_base64(mask_image)","    ","    #mask_image.save(\"mask.png\") #uncomment this to see what the mask looks like","","    return mask_image_base64","",""],"id":3}],[{"start":{"row":49,"column":0},"end":{"row":50,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":50,"column":0},"end":{"row":82,"column":0},"action":"insert","lines":["#get the stringified request body for the InvokeModel API call","def get_titan_image_insertion_request_body(prompt_content, input_image_bytes, insertion_position, insertion_dimensions):","","    original_image = get_image_from_bytes(input_image_bytes)","    ","    input_image_base64 = get_png_base64(original_image)","    ","    target_width, target_height = original_image.size","    ","    inside_width, inside_height = insertion_dimensions","    ","    mask_image_base64 = get_mask_image_base64(target_width, target_height, insertion_position, inside_width, inside_height)","    ","    body = { #create the JSON payload to pass to the InvokeModel API","        \"taskType\": \"INPAINTING\",","        \"inPaintingParams\": {","            \"image\": input_image_base64,","            \"maskImage\": mask_image_base64,","            \"text\": prompt_content,  # What to add to the image","        },","        \"imageGenerationConfig\": {","            \"numberOfImages\": 1,  # Number of variations to generate","            \"quality\": \"premium\",  # Allowed values are \"standard\" and \"premium\"","            \"height\": target_height,","            \"width\": target_width,","            \"cfgScale\": 8.0,","            \"seed\": randint(0, 100000),  # Change the seed to generate different content","        },","    }","    ","    return json.dumps(body)","",""],"id":5}],[{"start":{"row":82,"column":0},"end":{"row":83,"column":0},"action":"insert","lines":["",""],"id":6}],[{"start":{"row":83,"column":0},"end":{"row":120,"column":0},"action":"insert","lines":["#get a BytesIO object from the Titan Image Generator response","def get_titan_response_image(response):","","    response = json.loads(response.get('body').read())","    ","    images = response.get('images')","    ","    image_data = base64.b64decode(images[0])","","    return BytesIO(image_data)","","","#load the bytes from a file on disk","def get_bytes_from_file(file_path):","    with open(file_path, \"rb\") as image_file:","        file_bytes = image_file.read()","    return file_bytes","","","#generate an image using Amazon Titan Image Generator","def get_image_from_model(prompt_content, image_bytes, mask_prompt=None, negative_prompt=None, insertion_position=None, insertion_dimensions=None):","    session = boto3.Session()","","    bedrock = session.client(service_name='bedrock-runtime') #creates a Bedrock client","    ","    if image_bytes == None:","        image_bytes = get_bytes_from_file(\"images/desk.jpg\") #use desk.jpg if no file uploaded","    ","   ","    body = get_titan_image_insertion_request_body(prompt_content, image_bytes, insertion_position, insertion_dimensions) #preload desk.jpg","    ","    response = bedrock.invoke_model(body=body, modelId=\"amazon.titan-image-generator-v1\", contentType=\"application/json\", accept=\"application/json\")","    ","    output = get_titan_response_image(response)","    ","    return output","",""],"id":7}],[{"start":{"row":0,"column":0},"end":{"row":120,"column":0},"action":"remove","lines":["import boto3","import json","import base64","from PIL import Image","from io import BytesIO","from random import randint","","","#get a BytesIO object from file bytes","def get_bytesio_from_bytes(image_bytes):","    image_io = BytesIO(image_bytes)","    return image_io","","","#get a base64-encoded PNG image from an Image object","def get_png_base64(image):","    png_io = BytesIO()","    image.save(png_io, format=\"PNG\")","    img_str = base64.b64encode(png_io.getvalue()).decode(\"utf-8\")","    return img_str","","","#get an Image object from file bytes","def get_image_from_bytes(image_bytes):","    ","    image_io = BytesIO(image_bytes)","    ","    image = Image.open(image_io)","    ","    return image","","","#Get an inpainting or outpainting mask for the provided dimensions","def get_mask_image_base64(target_width, target_height, position, inside_width, inside_height):","    ","    inside_color_value = (0, 0, 0) #inside is black - this is the masked area","    outside_color_value = (255, 255, 255)","    ","    mask_image = Image.new(\"RGB\", (target_width, target_height), outside_color_value)","    original_image_shape = Image.new(","        \"RGB\", (inside_width, inside_height), inside_color_value","    )","    mask_image.paste(original_image_shape, position)","    mask_image_base64 = get_png_base64(mask_image)","    ","    #mask_image.save(\"mask.png\") #uncomment this to see what the mask looks like","","    return mask_image_base64","","","#get the stringified request body for the InvokeModel API call","def get_titan_image_insertion_request_body(prompt_content, input_image_bytes, insertion_position, insertion_dimensions):","","    original_image = get_image_from_bytes(input_image_bytes)","    ","    input_image_base64 = get_png_base64(original_image)","    ","    target_width, target_height = original_image.size","    ","    inside_width, inside_height = insertion_dimensions","    ","    mask_image_base64 = get_mask_image_base64(target_width, target_height, insertion_position, inside_width, inside_height)","    ","    body = { #create the JSON payload to pass to the InvokeModel API","        \"taskType\": \"INPAINTING\",","        \"inPaintingParams\": {","            \"image\": input_image_base64,","            \"maskImage\": mask_image_base64,","            \"text\": prompt_content,  # What to add to the image","        },","        \"imageGenerationConfig\": {","            \"numberOfImages\": 1,  # Number of variations to generate","            \"quality\": \"premium\",  # Allowed values are \"standard\" and \"premium\"","            \"height\": target_height,","            \"width\": target_width,","            \"cfgScale\": 8.0,","            \"seed\": randint(0, 100000),  # Change the seed to generate different content","        },","    }","    ","    return json.dumps(body)","","","#get a BytesIO object from the Titan Image Generator response","def get_titan_response_image(response):","","    response = json.loads(response.get('body').read())","    ","    images = response.get('images')","    ","    image_data = base64.b64decode(images[0])","","    return BytesIO(image_data)","","","#load the bytes from a file on disk","def get_bytes_from_file(file_path):","    with open(file_path, \"rb\") as image_file:","        file_bytes = image_file.read()","    return file_bytes","","","#generate an image using Amazon Titan Image Generator","def get_image_from_model(prompt_content, image_bytes, mask_prompt=None, negative_prompt=None, insertion_position=None, insertion_dimensions=None):","    session = boto3.Session()","","    bedrock = session.client(service_name='bedrock-runtime') #creates a Bedrock client","    ","    if image_bytes == None:","        image_bytes = get_bytes_from_file(\"images/desk.jpg\") #use desk.jpg if no file uploaded","    ","   ","    body = get_titan_image_insertion_request_body(prompt_content, image_bytes, insertion_position, insertion_dimensions) #preload desk.jpg","    ","    response = bedrock.invoke_model(body=body, modelId=\"amazon.titan-image-generator-v1\", contentType=\"application/json\", accept=\"application/json\")","    ","    output = get_titan_response_image(response)","    ","    return output","",""],"id":8},{"start":{"row":0,"column":0},"end":{"row":31,"column":0},"action":"insert","lines":["import boto3","import json","import base64","from PIL import Image","from io import BytesIO","from random import randint","","","#get a BytesIO object from file bytes","def get_bytesio_from_bytes(image_bytes):","    image_io = BytesIO(image_bytes)","    return image_io","","","#get a base64-encoded PNG image from an Image object","def get_png_base64(image):","    png_io = BytesIO()","    image.save(png_io, format=\"PNG\")","    img_str = base64.b64encode(png_io.getvalue()).decode(\"utf-8\")","    return img_str","","","#get an Image object from file bytes","def get_image_from_bytes(image_bytes):","    ","    image_io = BytesIO(image_bytes)","    ","    image = Image.open(image_io)","    ","    return image","",""]}],[{"start":{"row":31,"column":0},"end":{"row":32,"column":0},"action":"insert","lines":["",""],"id":9}],[{"start":{"row":32,"column":0},"end":{"row":49,"column":0},"action":"insert","lines":["#Get an inpainting or outpainting mask for the provided dimensions","def get_mask_image_base64(target_width, target_height, position, inside_width, inside_height):","    ","    inside_color_value = (0, 0, 0) #inside is black - this is the masked area","    outside_color_value = (255, 255, 255)","    ","    mask_image = Image.new(\"RGB\", (target_width, target_height), outside_color_value)","    original_image_shape = Image.new(","        \"RGB\", (inside_width, inside_height), inside_color_value","    )","    mask_image.paste(original_image_shape, position)","    mask_image_base64 = get_png_base64(mask_image)","    ","    #mask_image.save(\"mask.png\") #uncomment this to see what the mask looks like","","    return mask_image_base64","",""],"id":10}],[{"start":{"row":49,"column":0},"end":{"row":50,"column":0},"action":"insert","lines":["",""],"id":11}],[{"start":{"row":50,"column":0},"end":{"row":82,"column":0},"action":"insert","lines":["#get the stringified request body for the InvokeModel API call","def get_titan_image_insertion_request_body(prompt_content, input_image_bytes, insertion_position, insertion_dimensions):","","    original_image = get_image_from_bytes(input_image_bytes)","    ","    input_image_base64 = get_png_base64(original_image)","    ","    target_width, target_height = original_image.size","    ","    inside_width, inside_height = insertion_dimensions","    ","    mask_image_base64 = get_mask_image_base64(target_width, target_height, insertion_position, inside_width, inside_height)","    ","    body = { #create the JSON payload to pass to the InvokeModel API","        \"taskType\": \"INPAINTING\",","        \"inPaintingParams\": {","            \"image\": input_image_base64,","            \"maskImage\": mask_image_base64,","            \"text\": prompt_content,  # What to add to the image","        },","        \"imageGenerationConfig\": {","            \"numberOfImages\": 1,  # Number of variations to generate","            \"quality\": \"premium\",  # Allowed values are \"standard\" and \"premium\"","            \"height\": target_height,","            \"width\": target_width,","            \"cfgScale\": 8.0,","            \"seed\": randint(0, 100000),  # Change the seed to generate different content","        },","    }","    ","    return json.dumps(body)","",""],"id":12}],[{"start":{"row":82,"column":0},"end":{"row":83,"column":0},"action":"insert","lines":["",""],"id":13}],[{"start":{"row":83,"column":0},"end":{"row":120,"column":0},"action":"insert","lines":["#get a BytesIO object from the Titan Image Generator response","def get_titan_response_image(response):","","    response = json.loads(response.get('body').read())","    ","    images = response.get('images')","    ","    image_data = base64.b64decode(images[0])","","    return BytesIO(image_data)","","","#load the bytes from a file on disk","def get_bytes_from_file(file_path):","    with open(file_path, \"rb\") as image_file:","        file_bytes = image_file.read()","    return file_bytes","","","#generate an image using Amazon Titan Image Generator","def get_image_from_model(prompt_content, image_bytes, mask_prompt=None, negative_prompt=None, insertion_position=None, insertion_dimensions=None):","    session = boto3.Session()","","    bedrock = session.client(service_name='bedrock-runtime') #creates a Bedrock client","    ","    if image_bytes == None:","        image_bytes = get_bytes_from_file(\"images/desk.jpg\") #use desk.jpg if no file uploaded","    ","   ","    body = get_titan_image_insertion_request_body(prompt_content, image_bytes, insertion_position, insertion_dimensions) #preload desk.jpg","    ","    response = bedrock.invoke_model(body=body, modelId=\"amazon.titan-image-generator-v1\", contentType=\"application/json\", accept=\"application/json\")","    ","    output = get_titan_response_image(response)","    ","    return output","",""],"id":14}]]},"ace":{"folds":[],"scrolltop":1342,"scrollleft":0,"selection":{"start":{"row":120,"column":0},"end":{"row":120,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":109,"state":"start","mode":"ace/mode/python"}},"timestamp":1716776907143,"hash":"792abbdbcff31ba9d6f71b90e2f4b8cb0a452a05"}