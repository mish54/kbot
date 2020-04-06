from json import JSONDecodeError
import requests


class Members:

	def __init__(self):
		members = []
		resp = requests.get('https://gameinfo.albiononline.com/api/gameinfo/guilds/uatVVzFyQjqf_H_Bfl8i2A/members').json()
		try:
			for i in resp:
				members.append(i["Id"])
		except JSONDecodeError:
			pass
		self.members = members

