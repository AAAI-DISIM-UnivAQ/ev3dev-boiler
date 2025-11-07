# EV3DEV Docker Studio: Ambiente Completo per Sviluppo, Emulazione e Flashing LEGO Mindstorms EV3

Ambiente Docker per sviluppo e build di applicazioni LEGO Mindstorms EV3 con EV3DEV, emulazione ARM e flusso automatico per creare immagini microSD flashabili.

## Prerequisiti

- Docker installato su PC (Linux, macOS o Windows)
- Supporto QEMU per emulazione ARM:
`sudo apt-get install qemu-user-static`
- Brickstrap installato nel container (già incluso nel Dockerfile)
- MicroSD almeno 2GB e programma per flash (es. balenaEtcher)
- File d’esempio python (`main.py`), script di build/flash (`build_flash.sh`) già inclusi nel progetto


## Build immagine Docker

Costruisci l’ambiente Docker:

```sh
docker build -t ev3dev-env .
```


## Avvio ambiente di sviluppo

Esegui il container con la cartella corrente montata:

```sh
docker run --rm -it -v $PWD:/src ev3dev-env
```

Verifica di vedere `/src/main.py` e `build_flash.sh` dentro il container.

## Compile \& test esempio base

Compila il file di esempio python in ARM:

```sh
python src/main.py
```


## Creazione immagine microSD EV3DEV

Nel container, crea l’immagine microSD avviando lo script:

```sh
./build_flash.sh
```

Questo comando genera:

- `ev3dev.tar` - rootfs EV3DEV pronto per flashing
- `ev3dev.img` - file immagine microSD pronto


## Flash dell’immagine su microSD

Utilizza balenaEtcher, dd, Raspberry Pi Imager, ecc. per scrivere `ev3dev.img` sulla microSD.

**Esempio dd (Linux/Mac):**

```sh
sudo dd if=ev3dev.img of=/dev/sdX bs=4M conv=fsync status=progress
```

*(Sostituisci `/dev/sdX` con il percorso corretto della microSD)*

## Avvio su brick LEGO EV3

- Inserisci la microSD nel brick
- Accendi l’EV3, dovrebbe partire EV3DEV Linux

## Documentazione su EV3DEV_Body.py e EV3DEV_Controller.py

Questi due file Python rappresentano una struttura modulare per semplificare il controllo del brick LEGO EV3 con EV3DEV usando il pacchetto `ev3dev2`.

- **EV3DEV_Body.py**
Classe che incapsula il controllo dei componenti hardware del brick quindi motori, sensori (come touch, colori, ultrasuoni) e LED.
Include metodi per leggere stati (es. bumper premuto, colore rilevato), azionare motori e impostare il colore dei LED.
La classe funge da "corpo" robotico, astraendo i dettagli hardware.
- **EV3DEV_Controller.py**
Controller che usa EV3DEV_Body per implementare logiche di alto livello, ad esempio cambiare il colore dei LED in base a input da sensori.
Include metodi specifici come `change_led_color(sensor, color)` che ad esempio cambia il LED se il sensore ultrasuoni rileva ostacolo vicino o se il bumper è premuto.
Rappresenta il "cervello" che decide azioni sui componenti hardware astratti nella classe Body.

Questa struttura permette di separare l'accesso diretto all'hardware dalla logica di controllo, rendendo il codice più modulare e manutenibile. Puoi estendere o modificare la logica nel Controller senza toccare direttamente la gestione hardware nel Body.

## Personalizzazione

Puoi modificare il Dockerfile per aggiungere tool, librerie, script e creare firmware personalizzati per la tua robotica EV3.

Per info e tips:

- [Ev3dev Docker Images](https://github.com/ev3dev/docker-library)
- [Guida EV3DEV ufficiale](https://ev3dev.org/docs/getting-started/)
- [Tutorial build e sviluppo](https://ev3dev.org/docs/tutorials/)

***

Questa versione di README ti guida passo passo dall’installazione, sviluppo, compilazione, flashing fino a test e spiega l’architettura Python per gestire robot EV3 in modo modulare e estendibile.
<span style="display:none">[^1][^2][^3]</span>

<div align="center">⁂</div>

[^1]: README.md

[^2]: EV3DEV_Body.py

[^3]: EV3DEV_Controller.py

