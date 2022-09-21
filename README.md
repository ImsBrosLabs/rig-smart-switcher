# Rig smart switcher
A python script that automatically switches ON/OFF a crypto mining rig depending on the weather and rig temp.

![Project's diagram](diagram.png)

## TODO's
- [x] Find an API wrapper for communicating with the P110 smart plug.
- [ ] ~~Look for and test hiveOS API~~ => use a SSH client like [paramiko](https://docs.paramiko.org/en/stable/api/client.html) to perform this.
- [x] Find a weather API => [Open-Meteo](https://open-meteo.com/en).

## Improvements
- [ ] Refactoring.
- [ ] Write unit tests.
- [x] Config file + validation.
- [ ] Use [Cements](https://docs.builtoncement.com/getting-started/beginner-tutorial/part-1-creating-your-first-project) ?
- [ ] Use pm2 to cronify the script ?
