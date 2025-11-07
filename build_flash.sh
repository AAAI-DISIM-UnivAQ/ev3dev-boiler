#!/bin/bash
# Compila in ARM
python src/main.py
echo "Compilato hello per ARM."

# Usando brickstrap: crea tar e img
brickstrap create-tar ev3dev/ev3dev-jessie-ev3-generic ev3dev.tar
brickstrap create-image ev3dev.tar ev3dev.img
echo "Immagine pronta: ev3dev.img. Flashala su SD con Etcher."
