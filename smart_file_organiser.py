print("=====================================")
print("      SMART FILE ORGANISER")
print("=====================================")

total_files = 0
image_count = 0
document_count = 0
audio_count = 0
video_count = 0
other_count = 0

n = int(input("Enter number of files: "))

for i in range(n):

    print("\nFile", i + 1)
    filename = input("Enter file name: ")

    total_files = total_files + 1

    if ".jpg" in filename:
        print(filename, "-> Images Folder")
        image_count = image_count + 1

    elif ".png" in filename:
        print(filename, "-> Images Folder")
        image_count = image_count + 1

    elif ".jpeg" in filename:
        print(filename, "-> Images Folder")
        image_count = image_count + 1

    elif ".pdf" in filename:
        print(filename, "-> Documents Folder")
        document_count = document_count + 1

    elif ".txt" in filename:
        print(filename, "-> Documents Folder")
        document_count = document_count + 1

    elif ".docx" in filename:
        print(filename, "-> Documents Folder")
        document_count = document_count + 1

    elif ".mp3" in filename:
        print(filename, "-> Audio Folder")
        audio_count = audio_count + 1

    elif ".wav" in filename:
        print(filename, "-> Audio Folder")
        audio_count = audio_count + 1

    elif ".mp4" in filename:
        print(filename, "-> Videos Folder")
        video_count = video_count + 1

    elif ".avi" in filename:
        print(filename, "-> Videos Folder")
        video_count = video_count + 1

    elif ".py" in filename:
        print(filename, "-> Programming Folder")

    else:
        print(filename, "-> Others Folder")
        other_count = other_count + 1

print("\n=====================================")
print("          ORGANISATION REPORT")
print("=====================================")

print("Total Files Entered :", total_files)
print("Image Files         :", image_count)
print("Document Files      :", document_count)
print("Audio Files         :", audio_count)
print("Video Files         :", video_count)
print("Other Files         :", other_count)

print("\nThank You For Using Smart File Organiser")
