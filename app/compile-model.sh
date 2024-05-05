#!/bin/bash -x
. /root/.bashrc
mkdir model_store
pip install --upgrade pip
if [ "$(uname -i)" = "x86_64" ]; then
  if [ $DEVICE="xla" ]; then
    pip config set global.extra-index-url https://pip.repos.neuron.amazonaws.com
    pip install "optimum[neuronx, diffusers]"
    python compile-sd2.py 
  fi
fi

while true; do sleep 1000; done
