import streamlit as st
import pandas as pd

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("cosmetic_p.csv")
    return df

df = load_data()

# App title
st.title("SkinCare Genie")
st.subheader("Personalized Skin Care Routine for All Ages")

# User inputs
age = st.slider("Select your age", 10, 70, 25)
skin_type = st.selectbox("Select your skin type", ["Dry", "Oily", "Combination", "Normal"])
goal = st.multiselect("Select your skincare goals", 
                      ["Glow", "Anti-aging", "Hydration", "Acne control", "Even tone", "Sun protection"])

# Button to get recommendations
if st.button("Get My Routine 💅"):
    st.write("### 👩 Based on your inputs, here's your recommended routine:")

    # Basic logic for recommendations
    if "Glow" in goal:
        st.write("- Use Vitamin C Serum every morning.")
    if "Hydration" in goal:
        st.write("- Apply Hyaluronic Acid moisturizer day and night.")
    if "Anti-aging" in goal and age >= 30:
        st.write("- Use Retinol at night (start with mild %).")
    if "Acne control" in goal and skin_type in ["Oily", "Combination"]:
        st.write("- Use Salicylic Acid face wash and Niacinamide serum.")
    if "Sun protection" in goal:
        st.write("- Wear broad-spectrum SPF 50 sunscreen daily.")

    st.success("Always patch test and consult a dermatologist if unsure.")

    # Filter moisturizers based on skin type column in CSV
    st.write("### 💧 Recommended Moisturizers for Your Skin Type:")
    recommended = df[df[skin_type] == 1]  # Filters where the skin type column has value 1

    if not recommended.empty:
        st.dataframe(recommended[["brand", "name", "price", "rank", "ingredients"]].sort_values("rank").head(5))
    else:
        st.warning("Sorry! No moisturizers found for your skin type in the database.")

# Footer
st.write("---")
st.caption("Made with ❤️ for every woman who cares for her skin.")
