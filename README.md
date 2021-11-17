# Klima-in-der-Stube
Messung von Feinstaub, Temperatur und Druck mit Rasberry Pi, SDS011, BMP280, Python 3

Dieses Projekt baut auf Projekt https://github.com/zefanja/aqi bzw. https://zefanjas.de/?s=feinstaub auf. Der Unterschied ist, dass es Python 3 und zusätzlich einen Sensor zur Messung von Temperatur und Druck BMP280 verwendet. 
Für die Kommunikation mit Sensoren werden folgende Bibliotheken verwendet:
https://github.com/ikalchev/py-sds011 und https://github.com/pimoroni/bmp280-python.

Technische Daten von Target: 
Raspberry Pi 4B 2GB, SD card: 32GB
OS: Raspberry Pi OS (32-bit, Desktop Version)

Durch die Verwendung eines Webservers ist es möglich, die aktuellen Sensorwerte von jedem beliebigen Gerät im Netzwerk abzurufen.
Über das Display können die Daten am Standort der Sensoren abgerufen werden.

|Übersicht| nur LCD | Laptop |
| ------ | ------- | ------- |
| ![Übersicht](https://user-images.githubusercontent.com/90817262/142719930-4c0c2860-0c04-4b63-84e9-99b7054987e8.jpg) | ![IMG_20211115_200758](https://user-images.githubusercontent.com/90817262/142139236-9b54a4fe-4845-4737-9faf-b4e552cd602b.jpg) | <img alt="Laptop" src="https://user-images.githubusercontent.com/90817262/142720296-037aa62a-3e22-4bc3-8b53-bf78dcd6948e.jpg" width="80%" /> |




Weitere Einstellungen

in /home/pi/.config/lxsession/LXDE-pi/autostart

@chromium-browser --force-device-scale-factor=0.7 --incognito --kiosk http://localhost --windows-size=320,480
