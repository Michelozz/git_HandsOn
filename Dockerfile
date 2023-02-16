# Start from debian linux image
FROM debian:stable

# Add custom label
LABEL maintainer "IlariaMichelozzi ilariamarina.michelozzi@uvic.cat" \
      version "0.1" \
      description "Docker image for seqClass.py"

# Install needed tools
RUN apt-get update \
    &&  apt-get install -y --no-install-recommends \
         python-is-python3

# Make the folder '/scripts' in the container
RUN mkdir /scripts

# Copy 'seqClass.py' to the folder '/scripts' in the container
ADD seqClass.py /scripts
