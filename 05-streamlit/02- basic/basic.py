import streamlit as st
"Title"
st.title("this is title")
'Header'
st.header("this is header")
'subheader'
st.subheader("this is subheader")

'text'
st.text("this is text")
'Markdown'
st.markdown('###this is a markdown')

'success'
st.success("success")
'info'
st.info("information")

'error'
st.error("error")
'warning'
st.warning("warning")

# Exception

exp = ZeroDivisionError("trying divide by zero")
st.exception(exp)

'Text with write'
st.write('this text is with write')
# range function
st.write(range(12))

# display Image

from PIL import Image
imag = Image.open("streamlit.png")
st.image(imag, width=100)

# checkbox

if st.checkbox("Show/Hide"):
    st.write("This is widget")



# radio button
status = st.radio("Choose One: ", ("Male", "Female"))
if status == "Male":
    st.success("Male")

else:
    st.success("Female")


# Selection Box
    
sel_box = st.selectbox("Hobby", ["dancing", "reading", "Writing"])

st.write("Your hobby is ", sel_box)

# Multi selection Box

mult_select = st.multiselect("Multi hobbies :", ["Dancing", "singing", "reading", "writing", "knowing"])
st.write("Your hobbies are : ", len(mult_select), "which are :", mult_select)


# simple button
st.button("click me for nothing")


# create button 

if st.button("About"):
    st.text("Welcom to generative AI")


# Input
    
name = st.text_input("Enter your name : ", "type here")
if st.button("submit"):
    result = name.title()
    st.success(result)

# slider
    
level = st.slider("select: ", 1, 10)

st.text('select : {}'.format(level))