import dbus

from arle.helpers import output

class BackLight(object):
    """Adjust keyboard backlights

    Attributes:
        _bus: dbus.SystemBus
        _proxy: org.freedesktop.UPower,  /org/freedesktop/UPower/KbdBacklight
        _kbd_backlight: dbus.Interface
        _max_level: Maximum brightness level
    """

    def __init__(self):
        """Initialize D-Bus interface"""
        self._bus = dbus.SystemBus()
        self._proxy = self._bus.get_object(
            'org.freedesktop.UPower',
            '/org/freedesktop/UPower/KbdBacklight')
        self._kbd_backlight = dbus.Interface(self._proxy, 'org.freedesktop.UPower.KbdBacklight')
        self._max_level = self._kbd_backlight.GetMaxBrightness()

    def get_backlight_level(self):
        """Get current brightness level"""
        return self._kbd_backlight.GetBrightness()

    def set_backlight_level(self, level):
        """Set current brightness level"""
        self._kbd_backlight.SetBrightness(level)

    def up(self):
        """Increasing current brightness level"""
        current_level = self.get_backlight_level()
        new_level = max(0, current_level + 1)

        if new_level >= 0 and new_level <= self._max_level:
            # If value is valid then increase keyboard backlights
            output.Display.ok('Increasing keyboard backlight to %s.' %new_level)
            self.set_backlight_level(new_level)
        else:
            # If value is invalid then do nothing
            output.Display.warning('Keyboard backlights are set to max already!')

    def down(self):
        """Decreasing current brightness level"""
        current_level = self.get_backlight_level()
        new_level = max(-1, current_level - 1)

        if new_level >= 0 and new_level <= self._max_level:
            # If value is valid then increase keyboard backlights
            output.Display.ok('Decreasing keyboard backlights to %s.' %new_level)
            self.set_backlight_level(new_level)
        else:
            # If value is invalid then do nothing
            output.Display.warning('Keyboard backlights are already disabled!')
