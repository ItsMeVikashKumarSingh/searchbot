import os
from setuptools import setup, find_packages

requires = [
	"requests",
	"telepot",
	"flask",
]

setup(name = "google-search-telegram-bot",
		version = "1",
		description = "Google Search Bot for Telegram",
		long_description = "Telegram bot (support both inline/chat) that return search results from Google",
		url = "https://github.com/ItsMeVikashKumarSingh/searchbot.git",
		author = "Ming",
		license = "Apache",
		classifiers = [
			"License :: OSI Approved :: Apache Software License",
			"Programming Language :: Python :: 3",
			"Topic :: Communications :: Chat",
		],
		keywords = "google search telegram chat bot",
		packages = find_packages(),
		install_requires = requires)
