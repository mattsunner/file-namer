"""
  File Renamer

  Author: Matthew Sunner
"""
# imports
import os


# Renamer
def main():
    # Update this to change the base name of all files
    nameBase = "Presentation"
    fileType = ".pptx"  # Update to reflect needed file type extension

    for count, filename in enumerate(os.listdir("xyz")):
        # Use any extension needed here
        dst = nameBase + str(count) + fileType
        src = 'xyz' + filename
        dst = 'xyz' + dst

        os.rename(src, dst)


# Calling Function
if __name__ == '__main__':
    main()
