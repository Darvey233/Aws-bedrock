{"filter":false,"title":"image_search_app.py","tooltip":"/workshop/labs/image_search/image_search_app.py","undoManager":{"mark":7,"position":7,"stack":[[{"start":{"row":0,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["import streamlit as st #all streamlit commands will be available through the \"st\" alias","import image_search_lib as glib #reference to local lib script","","","st.set_page_config(page_title=\"Image Search\", layout=\"wide\") #HTML title","st.title(\"Image Search\") #page title","",""],"id":1}],[{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":8,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["if 'vector_index' not in st.session_state: #see if the vector index hasn't been created yet","    with st.spinner(\"Indexing images...\"): #show a spinner while the code in this with block runs","        st.session_state.vector_index = glib.get_index() #retrieve the index through the supporting library and store in the app's session cache","","","search_images_tab, find_similar_images_tab = st.tabs([\"Image search\", \"Find similar images\"])","",""],"id":3}],[{"start":{"row":15,"column":0},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":16,"column":0},"end":{"row":35,"column":0},"action":"insert","lines":["with search_images_tab:","","    search_col_1, search_col_2 = st.columns(2)","","    with search_col_1:","        input_text = st.text_input(\"Search for:\") #display a multiline text box with no label","        search_button = st.button(\"Search\", type=\"primary\") #display a primary button","","    with search_col_2:","        if search_button: #code in this if block will be run when the button is clicked","            st.subheader(\"Results\")","            with st.spinner(\"Searching...\"): #show a spinner while the code in this with block runs","                response_content = glib.get_similarity_search_results(index=st.session_state.vector_index, search_term=input_text)","                ","                #st.write(response_content) #using table so text will wrap","                ","                for res in response_content:","                    st.image(res, width=250)","",""],"id":5}],[{"start":{"row":35,"column":0},"end":{"row":36,"column":0},"action":"insert","lines":["",""],"id":6}],[{"start":{"row":36,"column":0},"end":{"row":59,"column":0},"action":"insert","lines":["with find_similar_images_tab:","    ","    find_col_1, find_col_2 = st.columns(2)","","    with find_col_1:","    ","        uploaded_file = st.file_uploader(\"Select an image\", type=['png', 'jpg'])","        ","        if uploaded_file:","            uploaded_image_preview = uploaded_file.getvalue()","            st.image(uploaded_image_preview)","    ","        find_button = st.button(\"Find\", type=\"primary\") #display a primary button","","    with find_col_2:","        if find_button: #code in this if block will be run when the button is clicked","            st.subheader(\"Results\")","            with st.spinner(\"Finding...\"): #show a spinner while the code in this with block runs","                response_content = glib.get_similarity_search_results(index=st.session_state.vector_index, search_image=uploaded_file.getvalue())","                ","                for res in response_content:","                    st.image(res, width=250)","",""],"id":7}],[{"start":{"row":59,"column":0},"end":{"row":60,"column":0},"action":"insert","lines":["",""],"id":8}]]},"ace":{"folds":[],"scrolltop":502,"scrollleft":0,"selection":{"start":{"row":60,"column":0},"end":{"row":60,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1716774523853,"hash":"4c9b88ca60eca3021601a812795e2dbb8bc83c98"}