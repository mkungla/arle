# ARLE (Asus ROG Linux extras)

Get maximum out of your Asus ROG when using linux

> Work in progress

- [x] **Adjusting keyboard backlights**
```bash
# to enable / increasing current brightness level
arle kb-backlight +
# to decreasing / disable current keyboard backlight
arle kb-backlight -
```
- [ ] Adjust screen backlight
- [ ] Enable Function keys (fn)

## Contributing

Fork and clone

```bash
# Deps with dnf
sudo dnf install python3-devel
# Deps with apt-get
sudo apt-get install python3-dev

# Setup Virtual environment
virtualenv -p python3 arle-env

# Activate virtual environment
. arle-env/bin/activate

# Install packeage as editable
pip3.5 install --editable .
```
