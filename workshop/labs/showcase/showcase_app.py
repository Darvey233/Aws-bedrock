import streamlit as st
import showcase_lib as glib
import showcase_examples as examples

#Add the page title and column layout. Here we are setting the page title on the actual page and the title shown in the browser tab.
#We are creating three columns, for the prompt templates, user inputs, and results.

st.set_page_config(page_title="Demo Showcase", layout="wide")

st.title("Demo Showcase")

col1, col2, col3 = st.columns(3)

#Add the prompt elements.
#We are creating a selectbox control to allow the user to choose from various prompt examples.
#We use the expander control to optionally hide the prompt details in the demo application.
#The user can customize the prompt in the user interface (changes won't be saved, though).
with col1:
    st.subheader("Prompt template")
    
    prompts_keys = list(examples.prompts)

    prompt_selection = st.selectbox("Select a prompt template:", prompts_keys)
    
    with st.expander("View prompt"):

        selected_prompt_template_text = examples.prompts[prompt_selection]

        prompt_text = st.text_area("Prompt template text:", value=selected_prompt_template_text, height=350)

#Add the input elements.
#Similar to above, we use a selectbox control to allow the user to select various input examples.
#The user can customize the input in the user interface (changes won't be saved, though).
with col2:
    st.subheader("User input")
    inputs_keys = list(examples.inputs)
    
    input_selection = st.selectbox("Select an input example:", inputs_keys)
    
    selected_input_template_text = examples.inputs[input_selection]

    input_text = st.text_area("Input text:", value=selected_input_template_text, height=350)
    
    process_button = st.button("Run", type="primary")

#Add the output elements.
#We use the if block below to handle the button click. We display a spinner while the backing function is called, then write the output to the web page.
with col3:
    st.subheader("Result")
    
    if process_button:
        with st.spinner("Running..."):
            response_content = glib.get_text_response(user_input=input_text, template=prompt_text)

            st.write(response_content)
