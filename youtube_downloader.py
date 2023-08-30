import streamlit as st
from pytube import YouTube
from tqdm import tqdm

def main():
    st.title("YouTube Video Downloader")
    
    # Input field for the YouTube video URL
    video_url = st.text_input("Enter YouTube Video URL:", "")

    if video_url:
        try:
            yt = YouTube(video_url)
            video_title = yt.title

            st.write(f"Video Title: {video_title}")

            # Display video thumbnail
            st.image(yt.thumbnail_url)

            # Choose an MP4 resolution to download
            resolutions = {stream.resolution: stream for stream in yt.streams.filter(file_extension="mp4", mime_type="video/mp4")}
            selected_resolution = st.selectbox("Select MP4 Resolution:", list(resolutions.keys()))

            download_button = st.button("Download Video")

            if download_button:
                selected_stream = resolutions[selected_resolution]
                st.write("Downloading...")
                
                # Prepare tqdm to show progress
                progress_bar = st.progress(0)
                
                # Download the video using tqdm to show progress
                with open(f"{video_title}.mp4", "wb") as f:
                    for chunk in tqdm(selected_stream.iter_content(chunk_size), total=video_size // chunk_size, unit="KB"):
                        f.write(chunk)
                        progress_bar.progress(f.tell() / video_size)
                        
                st.success("Video downloaded successfully!")

        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
