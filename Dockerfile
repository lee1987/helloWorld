FROM python:3.9

# envs
ENV PORT=8080

# install
RUN mkdir /app
RUN chown -R nobody /app
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

USER nobody

# run
CMD exec python hello_world/main.py

EXPOSE $PORT