Steps to Run the code.

1) Install the latest version of Ollama for Windows.
2) Setup Ollama in your system
3) Open terminal and check the version of Ollama installed by running ollama --version.
4) Now run the Ollama server by running ollama serve in the terminal.
5) Keep this server running and open another terminal
6) Run the Qwen2 0.5B model in the terminal by running ollama run qwen2:0.5b in the new terminal and keep the model running.
7) Now open another terminal and run the python script. User will have 2 options :- 1) Summarizing a text file. 2) Summarizing the text.
8) For text file run python summarize.py -t filename.txt. For just a text name python summarize.py The quick brown fox jumped over the lazy dog.
