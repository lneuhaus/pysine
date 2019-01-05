# define base image
FROM ubuntu:latest
# FROM node:7-onbuild

# set maintainer
LABEL maintainer "pyrpl.readthedocs.io@gmail.com"

USER root

ARG CONDA_DIR="/opt/conda"

# setup ubuntu
RUN apt update --yes
RUN apt upgrade --yes
RUN apt-get install wget --yes

# install miniconda
RUN mkdir /tmp/miniconda
WORKDIR /tmp/miniconda
RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN chmod +x Miniconda3-latest-Linux-x86_64.sh
RUN ./Miniconda3-latest-Linux-x86_64.sh -b -p $CONDA_DIR

# set path environment variable to refer to conda dir
ENV PATH="$CONDA_DIR/bin:$PATH"

# Add conda-forge as systemwide channels
#RUN $CONDA_DIR/bin/conda config --add channels conda-forge --system

# Clean up miniconda installation files
WORKDIR /
RUN rm -rf /tmp/miniconda

# print a message
RUN echo "Docker image is up and running...."
RUN echo $PATH

# activate conda base environment
RUN source activate

# print some python diagnostics information
RUN python -V
RUN conda env export
