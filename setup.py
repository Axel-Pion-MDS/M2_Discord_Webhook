from setuptools import setup, find_packages

setup(
    name='discordWebhookEasyMessage',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        "discord-webhook"
    ],
    author='Maengdok',
    author_email='maengdok@outlook.com',
    description='A Python package for easily sending messages through Discord webhooks',
    long_description='This package provides a simple interface for sending messages through Discord webhooks. It includes a Webhook class with methods to define the content, mentions, and easily send messages with embedded content.',
    url='https://github.com/Axel-Pion-MDS/M2_Discord_Webhook',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)