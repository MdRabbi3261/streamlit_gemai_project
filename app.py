import streamlit as st
from api_calling import generate_note,audio_transcript,quiz_generator
from PIL import Image

st.title("Note Summary and Quiz Generator ")
st.markdown ("Upload upto 3 images to generate Note summary and Quizzes")
st.divider()
with st.sidebar:
    st.title("Options")
    st.header("Controls Panel")

    # image uploader
    images=st.file_uploader("Upload the Photos of your note",type=["jpg","jpeg","png"],accept_multiple_files=True)

    pil_images=[]
    if images:
     for img in images:
        pil_img=Image.open(img)
        pil_images.append(pil_img)


    if pil_images:
        if len(pil_images)>3:
            st.error("Please upload a maximum of 3 images.")
            pil_images =[]
        else:
            col=st.columns(len(pil_images))

            st.subheader("Uploaded Images")

            for i, img in enumerate(pil_images):
                with col[i]:
                    st.image(img)
    
    #dificaulty level
    selected_option=st.selectbox (
        "Enter the difficulty level of the quiz",
        ("Easy", "Medium", "Hard"),
        index=None
    )
    

    pressed= st.button("click the button to initiate AI",type="primary")

if pressed:
    if not pil_images:
        st.error("Your must upload at least one image")
    if not selected_option:
        st.error("Your must a difficulty level for the quiz.")
    if pil_images and selected_option:
        #note
        with st.container(border=True):
            st.subheader("Your Note")
            #the protion below will be replaced by ApI call
            with st.spinner("AI is writing your note..."):
                note=generate_note(pil_images)
                st.markdown(note)

        #audio transcipt
        with st.container(border=True):
            st.subheader("Audio Transcript")
            #the protion below will be replaced by ApI call
            with st.spinner("AI is writing your note..."):
                 
                clean_note = note.replace("#","").replace("*","").replace("_","")




                audio=audio_transcript(clean_note)
                st.audio(audio)



        #quiz

        with st.container(border=True):
            st.subheader(f"Quiz ({selected_option} ) Difficulty")
            #the protion below will be replaced by ApI call

            with st.spinner("AI is generating quiz..."):
                quiz=quiz_generator(pil_images,selected_option)
                st.markdown(quiz)

