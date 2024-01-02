


================ This project is to test Microsoft Autogen Agents and create useful agents ============

Will be using the autogen library to create useful agents.



Requirements.txt file includes all the requirements and their rational.


=========== Docker image =========

export OPENAI_API_KEY=""

docker pull yuandongtian/autogen:latest
docker run -it -e OPENAI_API_KEY=$OPENAI_API_KEY -p 8081:8081 docker.io/yuandongtian/autogen:latest

