import asyncio
import aiofiles
import json


class Config:
	def __init__(self, config_path: str = 'config.json'):
		self._config_path = config_path

	async def get_config(self, *args) -> dict | str:
		try:
			async with aiofiles.open(self._config_path, mode='r') as config:
				config_content = await config.read()
		except FileNotFoundError:
			async with aiofiles.open(self._config_path, mode='w') as f:
				await f.write('{}')
				config_content = await config.read()

		config = json.loads(config_content)

		for name in args:
			try:
				config = config[name]
			except KeyError:
				raise KeyError('Неверный ключ словаря')
			except TypeError:
				raise TypeError('Лишние аргументы')

		return config

	def get_config_sync(self, *args) -> dict | str:
		try:
			with open(self._config_path, mode='r') as config:
				config_content = config.read()
		except FileNotFoundError:
			with open(self._config_path, mode='w') as f:
				f.write('{}')
				config_content = config.read()

		config = json.loads(config_content)

		for name in args:
			try:
				config = config[name]
			except KeyError:
				raise KeyError('Неверный ключ словаря')
			except TypeError:
				raise TypeError('Лишние аргументы')

		return config


async def main():
	cf = Config()
	cf_data = await cf.get_config()
	print(cf_data)


if __name__ == '__main__':
	asyncio.run(main())
