FROM python:3.7-alpine3.8
MAINTAINER TeskaLabs Ltd (support@teskalabs.com)

# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG C.UTF-8

RUN set -ex \
  && apk update \
  && apk upgrade \
  && apk add git

# Create build environment
RUN set -ex \
  && apk add --virtual buildenv python3-dev \
  && apk add --virtual buildenv libffi-dev \
  && apk add --virtual buildenv gcc \
  && apk add --virtual buildenv g++ \
  && apk add --virtual buildenv musl-dev

RUN apk --no-cache add jpeg-dev \
                       zlib-dev \
                       freetype-dev \
                       lcms2-dev \
                       openjpeg-dev \
                       tiff-dev \
                       tk-dev \
                       tcl-dev \
                       harfbuzz-dev \
                       fribidi-dev




RUN pip install --upgrade pip

RUN set -ex \
  && pip install requests \
  && pip install discord.py \
  && pip install python-dotenv \
  && pip install Pillow==7.0.0

RUN apk del buildenv

COPY ./api_calls /opt/killbot/api_calls
COPY misc/CollegiateBlackFLF.ttf /opt/killbot
COPY discord_bot.py /opt/killbot
COPY ./.env /opt/killbot

WORKDIR /opt/killbot

CMD python3 ./test.py
