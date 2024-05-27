{"filter":false,"title":"rag_chatbot_app.py","tooltip":"/workshop/labs/rag_chatbot/rag_chatbot_app.py","undoManager":{"mark":6,"position":6,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["import streamlit as st #all streamlit commands will be available through the \"st\" alias","import rag_chatbot_lib as glib #reference to local lib script","",""],"id":1}],[{"start":{"row":3,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["st.set_page_config(page_title=\"RAG Chatbot\") #HTML title","st.title(\"RAG Chatbot\") #page title","",""],"id":2}],[{"start":{"row":6,"column":0},"end":{"row":9,"column":0},"action":"insert","lines":["if 'memory' not in st.session_state: #see if the memory hasn't been created yet","    st.session_state.memory = glib.get_memory() #initialize the memory","",""],"id":3}],[{"start":{"row":9,"column":0},"end":{"row":12,"column":0},"action":"insert","lines":["if 'chat_history' not in st.session_state: #see if the chat history hasn't been created yet","    st.session_state.chat_history = [] #initialize the chat history","",""],"id":4}],[{"start":{"row":12,"column":0},"end":{"row":16,"column":0},"action":"insert","lines":["if 'vector_index' not in st.session_state: #see if the vector index hasn't been created yet","    with st.spinner(\"Indexing document...\"): #show a spinner while the code in this with block runs","        st.session_state.vector_index = glib.get_index() #retrieve the index through the supporting library and store in the app's session cache","",""],"id":5}],[{"start":{"row":16,"column":0},"end":{"row":21,"column":0},"action":"insert","lines":["#Re-render the chat history (Streamlit re-runs this script, so need this to preserve previous chat messages)","for message in st.session_state.chat_history: #loop through the chat history","    with st.chat_message(message[\"role\"]): #renders a chat line for the given role, containing everything in the with block","        st.markdown(message[\"text\"]) #display the chat content","",""],"id":6}],[{"start":{"row":21,"column":0},"end":{"row":37,"column":0},"action":"insert","lines":["input_text = st.chat_input(\"Chat with your bot here\") #display a chat input box","","if input_text: #run the code in this if block after the user submits a chat message","    ","    with st.chat_message(\"user\"): #display a user chat message","        st.markdown(input_text) #renders the user's latest message","    ","    st.session_state.chat_history.append({\"role\":\"user\", \"text\":input_text}) #append the user's latest message to the chat history","    ","    chat_response = glib.get_rag_chat_response(input_text=input_text, memory=st.session_state.memory, index=st.session_state.vector_index,) #call the model through the supporting library","    ","    with st.chat_message(\"assistant\"): #display a bot chat message","        st.markdown(chat_response) #display bot's latest response","    ","    st.session_state.chat_history.append({\"role\":\"assistant\", \"text\":chat_response}) #append the bot's latest message to the chat history","",""],"id":7}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":37,"column":0},"end":{"row":37,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":14,"state":"start","mode":"ace/mode/python"}},"timestamp":1716766646575,"hash":"e3e4401bfdae4cd80ac7269b070afcea09d3a083"}