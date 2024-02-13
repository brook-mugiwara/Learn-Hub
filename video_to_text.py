import tkinter as tk
from tkinter import ttk
from youtube_transcript_api import YouTubeTranscriptApi

class YouTubeToTextConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube to Text Converter")

        self.create_widgets()

    def create_widgets(self):
        self.label_url = ttk.Label(self.root, text="YouTube Video URL:")
        self.label_url.grid(row=0, column=0, padx=10, pady=10)

        self.entry_url = ttk.Entry(self.root, width=40)
        self.entry_url.grid(row=0, column=1, padx=10, pady=10)

        self.button_convert = ttk.Button(self.root, text="Convert to Text", command=self.convert_to_text)
        self.button_convert.grid(row=1, column=0, columnspan=2, pady=10)

        self.text_result = tk.Text(self.root, height=10, width=50, wrap=tk.WORD)
        self.text_result.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def convert_to_text(self):
        video_url = self.entry_url.get()
        if video_url:
            try:
                transcript = self.get_transcript(video_url)
                self.text_result.delete(1.0, tk.END)
                self.text_result.insert(tk.END, transcript)
            except Exception as e:
                self.text_result.delete(1.0, tk.END)
                self.text_result.insert(tk.END, f"Error: {str(e)}")
        else:
            self.text_result.delete(1.0, tk.END)
            self.text_result.insert(tk.END, "https://www.youtube.com/watch?v=OTuph9pJWU4")

    @staticmethod
    def get_transcript(video_url):
        video_id = video_url.split("v=")[1]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = " ".join([entry['text'] for entry in transcript])
        return text

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeToTextConverter(root)
    root.mainloop()