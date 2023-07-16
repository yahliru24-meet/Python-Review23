

def create_youtube_video(title, description):
	video_info = {"title": title, "description": description, "likes": 0, "dislikes": 0, "comments": {}}

	return video_info


def like(youtubevideo):
	if "likes" in youtubevideo.keys():
		youtubevideo["likes"] += 1

	return youtubevideo


def dislike(youtubevideo):
	if "dislikes" in youtubevideo.keys():
		youtubevideo["dislikes"] += 1

	return youtubevideo


def add_comment(youtubevideo, username, comment_text):
	youtubevideo["comments"][username] = comment_text

	return youtubevideo


def main():
	video = create_youtube_video("Hi", "Hello World!")
	for i in range(495):
		like(video)
	for i in range(124):
		dislike(video)
	add_comment(video,"Yahli", "This video is good!")

	print("""
		Title: {}
		Description: {}

		{} Likes :)
		{} Dislikes :(

		Comments:
		+++++++++
		{}
		""".format(video["title"], video["description"], video["likes"], video["dislikes"], video["comments"]))

main()