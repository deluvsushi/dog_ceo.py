from requests import get


class DogCeo:
	def __init__(self):
		self.api = "https://dog.ceo/api"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
		}
	
	def get_all_breeds(self):
		return get(
			f"{self.api}/breeds/list/all",
			headers=self.headers).json()
	
	def get_random_image(self, count: int = 1):
		return get(
			f"{self.api}/breeds/image/random/{count}",
			headers=self.headers).json()
	
	def get_images_from_breed(self):
		return get(
			f"{self.api}/breed/hound/images",
			headers=self.headers).json()
	
	def get_random_breed_image(self, count: int = 1):
		return get(
			f"{self.api}/breed/hound/images/random/{count}",
			headers=self.headers).json()
	
	def get_all_sub_breeds(self):
		return get(
			f"{self.api}/breed/hound/list",
			headers=self.headers).json()
	
	def get_all_sub_breed_images(self):
		return get(
			f"{self.api}/breed/hound/afghan/images",
			headers=self.headers).json()
	
	def get_random_sub_breed_image(self, count: int = 1):
		return get(
			f"{self.api}/breed/hound/afghan/images/random/{count}",
			headers=self.headers).json()
	
