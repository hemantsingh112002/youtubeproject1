import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error reading the file. The file might be corrupted.")
        return []

def save_data_helper(videos):
    try:
        with open('youtube.txt', 'w') as file:
            json.dump(videos, file)
    except Exception as e:
        print(f"Error saving data: {e}")

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    if videos:
        for index, video in enumerate(videos, start=1):
            print(f"{index}. {video['name']}, Duration: {video['time']}")
    else:
        print("No videos available.")
    print("\n")
    print("*" * 70)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time (format: HH:MM:SS or just a number): ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    try:
        index = int(input("Enter the video number to update: "))
        if 1 <= index <= len(videos):
            name = input("Enter the new video name: ")
            time = input("Enter the new video time (format: HH:MM:SS or just a number): ")
            videos[index - 1] = {'name': name, 'time': time}
            save_data_helper(videos)
        else:
            print("Invalid index selected")
    except ValueError:
        print("Please enter a valid number for video index")

def delete_video(videos):
    list_all_videos(videos)
    try:
        index = int(input("Enter the video number to be deleted: "))
        if 1 <= index <= len(videos):
            del videos[index - 1]
            save_data_helper(videos)
        else:
            print("Invalid video index selected")
    except ValueError:
        print("Please enter a valid number for video index")

def main():
    videos = load_data()

    while True:
        print("\nYoutube Manager")
        print("1. List all favourite videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice, please select a valid option.")

if __name__ == "__main__":
    main()
