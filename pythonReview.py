def create_youtube_video(title, description, hashtags):
	video_info = {"title": title, "description": description, "likes": 0, "dislikes": 0, "comments": {}, "hashtags": hashtags}

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



def similarity_algo(vid1, vid2):
	matches = 0
	for i in vid1["hashtags"]:
		if i in vid2["hashtags"]:
			matches += 1
	match_precent = matches/len(vid1["hashtags"])
	return "{}%".format(round(match_precent*100))



def print_vid_info(video):
	print("""
Title: {}
Description: {}
Hashtags: {}

{} Likes :)
{} Dislikes :(

Comments:
+++++++++
		""".format(video["title"], video["description"], video["hashtags"], video["likes"], video["dislikes"]))
	
	for i in video["comments"].keys():
		print("{}:	{}".format(i, video["comments"][i]))
	print("")



def main():
	video1 = create_youtube_video("Hi", "Hello World!", ["Vid", "Nice", "FIFA", "CS", "HI"])
	for i in range(495):
		like(video1)
	for i in range(124):
		dislike(video1)
	add_comment(video1,"Yahli", "This video is good!")

	video2 = create_youtube_video("Hello", "World!", ["Vid", "Nice", "FIFA", "Good", "Great"])
	for i in range(7454):
		like(video2)
	for i in range(245):
		dislike(video2)
	add_comment(video2,"Yahli", "Cool!")


	print_vid_info(video1)
	print_vid_info(video2)
	print("{} Similarity Between Both Videos".format(similarity_algo(video1, video2)))
	


if __name__ == "__main__":
    main()