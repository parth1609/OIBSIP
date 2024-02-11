from setuptools import setup, find_packages

setup(
    name='speech_program',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pyttsx3',
        'SpeechRecognition',
        'pyaudio',
    ],
    entry_points={
        'console_scripts': [
            'your_script_name = your_package_name.module:main_function',
        ],
    },
    # Other metadata options like author, description, license, etc.
)
