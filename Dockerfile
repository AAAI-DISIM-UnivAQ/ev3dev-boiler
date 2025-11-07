# Dockerfile EV3DEV Boilerplate
FROM ev3dev/debian-stretch-cross

# INSTALLA QEMU PER EMULAZIONE ARM
RUN apt-get update && \
    apt-get install -y qemu-user-static brickstrap

# Aggiungi esempio C (Hello World)
COPY src /EV3DEV_boiler/src
COPY build_flash.sh /EV3DEV_boiler
WORKDIR /EV3DEV_boiler

# Script di build e creazione immagine
RUN chmod +x /src/build_flash.sh

CMD ["/bin/bash"]
