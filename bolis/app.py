import streamlit as st
st.title("Video File Chooser")

# Create a button to open the file uploader
uploaded_video = st.file_uploader("Choose a video file", type=["mp4", "avi", "mov", "mkv"])

# Display the video if it's uploaded
if uploaded_video is not None:
    # Display a message with the file name
    st.success(f"Uploaded file: {uploaded_video.name}")

    # Display the video on the page
    st.video(uploaded_video)
else:
    st.write("Please upload a video file.")

