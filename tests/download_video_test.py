import unittest
import os
from src.video_util import download_video

class TestDownloadVideo(unittest.TestCase):
    def test_download_video(self):
        url = 'https://www.tiktok.com/@user/video/1234567890'  # Replace with a valid TikTok video URL
        save_path = 'media/videos/'
        expected_filename = save_path + 'user_video_1234567890.mp4'  # Replace with the expected filename

        result_filename = download_video(url, save_path)

        self.assertEqual(result_filename, expected_filename)
        self.assertTrue(os.path.exists(result_filename))

if __name__ == '__main__':
    unittest.main()