import os
from PIL import Image

class SplitGif:

    def get_gif_path(self):
        self.gif = input("Image path: ")
        try:
            self.open_gif = Image.open(self.gif)
        except Exception as e:
            print(e)
            return self.get_gif_path()
        
    def get_frames_path(self):
        self.frames_path = input("Path to store the frames: ")
        if not os.path.isdir(self.frames_path):
            print('Path not found')
            return self.get_frames_path()
    
    def split(self):
        try:
            frame_number = 0
            for i in range(self.open_gif.n_frames):
                frame_number += 1
                self.open_gif.seek(i)
                gif_rgb = self.open_gif.convert("RGB")
                print(self.gif)
                gif_rgb.save(f"{self.frames_path}/{frame_number}_{self.gif}.png")

        except Exception as e:
            print('Not a gif')
            print(e)

if __name__ == '__main__':
    split_gif = SplitGif()
    split_gif.get_gif_path()
    split_gif.get_frames_path()
    split_gif.split()
