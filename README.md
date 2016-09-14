# ARLE (Asus ROG Linux extras)

Get maximum out of your Asus ROG when using linux

> Work in progress

- [x] Adjust keyboard backlights
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
