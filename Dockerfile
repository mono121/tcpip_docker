FROM ubuntu:20.04
LABEL maintainer="mono"

# 環境変数
ENV USER hoge
ENV HOME /home/${USER}
ENV SHELL /bin/bash

# アカウント作成
RUN useradd -m ${USER}
RUN gpasswd -a ${USER} sudo
RUN echo "${USER}:hogehoge" | chpasswd

# ログインシェルの指定
# -i.bakは.bakをつけてバックアップを作成
RUN sed -i.bak "s#${HOME}:#${HOME}:${SHELL}#" /etc/passwd 

# コマンドラインの設定
RUN echo -n '\n\
export PS1="\\n"$PS1 \n\
if [ $UID -eq 0 ]; then \n\
    PS1="\\n\[\\e[36m\]\w\\n\[\\e[00m\]\$ " \n\
else \n\
    PS1="\\n\[\\e[36m\]\w\\n\[\\e[00m\]\$ " \n\
fi \n\
' >> ${HOME}/.bashrc

# pkg install
RUN apt-get update 
RUN apt-get -y install \
    sudo \
    vim \
    bash \
    coreutils \
    grep \
    iproute2 \
    iputils-ping \
    traceroute \
    tcpdump \
    bind9-dnsutils \
    dnsmasq-base \
    netcat-openbsd \
    python3 \
    wget \
    iptables \
    procps \
    isc-dhcp-client

USER ${USER}
WORKDIR ${HOME}