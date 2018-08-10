#### Splash

> https://splash.readthedocs.io/en/stable/install.html

## Linux + Docker

1. Install [Docker](http://docker.io/).

2. Pull the image:

   ```
   $ sudo docker pull scrapinghub/splash
   ```

3. Start the container:

   ```
   $ sudo docker run -p 8050:8050 -p 5023:5023 scrapinghub/splash
   ```

4. Splash is now available at 0.0.0.0 at ports 8050 (http) and 5023 (telnet).