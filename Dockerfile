FROM debian:buster

EXPOSE  6767

VOLUME /tv

# Update
RUN apt-get update
RUN apt-get install -y build-essential python-dev python-pip python-setuptools libjpeg-dev zlib1g-dev git libgit2-dev libffi-dev

# Get application source from Github
RUN git clone -b master --single-branch https://github.com/morpheus65535/bazarr.git /bazarr
RNU git config --global user.name "Bazarr" && git config --global user.email "bazarr@fake.email"

VOLUME /bazarr/data

# Install app dependencies
RUN pip install -r /bazarr/requirements.txt

CMD ["python", "/bazarr/bazarr.py"]