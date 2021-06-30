FROM python:3.9
WORKDIR /
RUN apt-get update && apt-get install -y libgl1-mesa-glx libgl1-mesa-dri
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && apt-get update -qqy && apt-get -qqy install ${CHROME_VERSION:-google-chrome-stable} && rm /etc/apt/sources.list.d/google-chrome.list && rm -rf /var/lib/apt/lists/* /var/cache/apt/*
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
