import streamlit as st
import google.generativeai as genai
import random

# ✅ Set full-page layout
st.set_page_config(page_title="RecipeMaster: AI-Powered Blog Generation", layout="wide")

# ✅ Apply CSS styling
st.markdown(
    """
    <style>
    /* Set background to black and text to white */
    html, body, .stApp {
        background-color: black !important;
        color: white !important;
    }

    /* Ensure input labels are white */
    label {
        color: white !important;
        font-weight: bold !important;
    }

    div[data-testid="stTextInputLabel"], 
    div[data-testid="stNumberInputLabel"], 
    div[data-testid="stMarkdownContainer"] p {
        color: white !important;
        font-weight: bold !important;
    }
    /* Match background for text and number inputs */
    input[type="text"], input[type="number"] {
        background-color: #333 !important;  /* Dark gray */
        color: white !important;
        border: 1px solid black !important;
        border-radius: 3px !important;
        padding: 10px !important;
    }

    /* ✅ Make Placeholder Text White */
    ::placeholder {
        color: white !important;
        opacity: 1 !important;
    }

    /* Transparent Button with Red Text */
    .stButton>button {
        background-color: transparent !important;  /* ✅ Transparent Background */
        color: red !important;  /* ✅ Red Text */
        border: 2px solid red !important;  /* ✅ Red Border */
        border-radius: 6px !important;  /* ✅ Rounded Corners */
        font-size: 14px !important;  /* ✅ Small Font */
        font-weight: bold !important;  /* ✅ Bold Text */
        padding: 5px 10px !important;  /* ✅ Small Padding */
        width: auto !important;  /* ✅ Auto Width */
    }

    /* Center container, but keep content left-aligned */
    .block-container {
        max-width: 800px !important;
        margin: auto !important;
        text-align: left !important;
    }

    /* Style the introduction heading */
    .intro-text {
        font-size: 25px;
        font-weight: 500px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Function to fetch jokes
def get_joke():
    jokes = [
        "Why do Java developers wear glasses? Because they don't see sharp.",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
        "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
        "Why was the computer cold? It left its Windows open."
    ]
    return random.choice(jokes)

# Function to generate a recipe using Gemini 1.5 Flash
def generate_recipe(user_input, word_count):
    """Generates a recipe using Google's Gemini AI model."""
    try:
        st.write("### ⏳ Generating your recepie...")
        st.write(f"While I work on creating your blog, here’s a little joke to keep you entertained:\n\n**{get_joke()}**")

        model = genai.GenerativeModel("gemini-1.5-flash")
        chat_session = model.start_chat(history=[
            {"role": "user", "parts": [f"Write a detailed recipe about: {user_input} in {word_count} words."]},
        ])
        response = chat_session.send_message(user_input)
        st.success("🎉 Your recipe is ready!")
        return response.text

    except Exception as e:
        st.error(f"Error generating recipe: {e}")
        return None

# Streamlit UI Design
st.markdown("# 🍽️ RecipeMaster: AI-Powered Blog Generation")

# ✅ Styled Introduction with emoji and bold text
st.markdown(
    '<div class="intro-text">🤖 Hello! I’m RecipeMaster, your friendly robot. Let’s create a fantastic recepie together!</div>',
    unsafe_allow_html=True
)

# Input fields
user_input = st.text_input("Topic", placeholder="Ex:- Chocolate Cake")
word_count = st.number_input("Number of words", min_value=100, max_value=1000, value=500, step=50)

# Generate button
if st.button("Generate Recipe", use_container_width=False):
    if user_input.strip():
        recipe = generate_recipe(user_input, word_count)
        if recipe:
            st.markdown(recipe)
    else:
        st.warning("⚠️ Please enter a valid topic.")
