import streamlit as st
import random
import json
import torch
from model import NeuralNet
from nltk_utils import tokenize, bag_of_words

# Streamlit app
st.set_page_config(page_title="BankMan", page_icon=":🤖:")
st.title("BankMan: The Banking Chatbot")



bank_name = st.selectbox("Select Bank:", ["icici", "Axis", "Hdfc"])
user_input = st.text_input("You:")


custom_css ="""
<style>
[data-testid="stAppViewContainer"]{
    height: 680px;
    width: 800px;
    margin-top: 50px;    
    margin-left: 350px;
    text-align: center;
    border: 3px solid white;
    border-radius: 50px;
    position: fixed;
    scroll-behaviour: unset;
    background-image: url('https://e0.pxfuel.com/wallpapers/875/426/desktop-wallpaper-i-whatsapp-background-chat-whatsapp-graffiti.jpg');
    background-color: rgb(255, 255, 255, 0.1);
}
[data-testid="StyledLinkIconContainer"]{    
    scroll-behaviour: unset;
}
[data-testid="stVerticalBlockBorderWrapper"]{    
    position: fixed;
    scroll-behaviour: unset;
    margin-bottom: 200px;
}
[data-testid="element-container"]{    
    scroll-behaviour: unset;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)



for responses in st.session_state:
        # with st.responses["role"]:
            st.markdown ["content"]



    # Load data
with open('icici.json', 'r', encoding="utf-8") as i:
        icici = json.load(i)
with open('Axis.json', 'r', encoding="utf-8") as a:
        Axis = json.load(a)
with open('Hdfc.json', 'r', encoding="utf-8") as h:
        Hdfc = json.load(h)

    # Load model
FILE = "data.pth"
data = torch.load(FILE)
input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "BankMan"

    # Function to get bot response
def get_bot_response(sentence, bank):
        sentence = tokenize(sentence)
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)
        _, predicted = torch.max(output, dim=1)
        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]

        if bank == "icici":
            data = icici
        elif bank == "Axis":
            data = Axis
        elif bank == "Hdfc":
            data = Hdfc

        if prob.item() > 0.75:
            for responses in data[bank]:
                if tag == responses["tag"]:
                    return random.choice(responses['responses'])
        else:
            return "I do not understand..."



if st.button("Send"): 
    if user_input:
            bot_response = get_bot_response(user_input, bank_name)
            st.text_area("BankMan:", value=bot_response, height=100)

