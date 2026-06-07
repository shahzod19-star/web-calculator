import streamlit as st


st.title("📱 Mening birinchi onlayn kalkulyatorim")
st.write("Sonlarni kiriting, amalni tanlang va tugmani bosing.")


son1 = st.number_input("1-sonni kiriting:", value=0.0)
amal = st.selectbox("Amalni tanlang (+, -, *, /):", ["+", "-", "*", "/"])
son2 = st.number_input("2-sonni kiriting:", value=0.0)

if st.button("Hisoblash 🚀"):
    if amal == "+":
        natija = son1 + son2
        st.success(f"Natija: {natija}")
        
    elif amal == "-":
        natija = son1 - son2
        st.success(f"Natija: {natija}")
        
    elif amal == "*":
        natija = son1 * son2
        st.success(f"Natija: {natija}")
        
    elif amal == "/":
        if son2 == 0:
            st.error("Xato! 0 ga bo'lib bo'lmaydi.")
        else:
            natija = son1 / son2
            st.success(f"Natija: {natija}")
