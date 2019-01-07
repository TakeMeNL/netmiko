from __future__ import unicode_literals

import re
import time

from netmiko.base_connection import BaseConnection


class TpLinkJetstreamBase(BaseConnection):
    def session_preparation(self):
        """Prepare the session after the connection has been established."""
        self._test_channel_read()
        self.set_base_prompt()
        self.enable()
        # Clear the read buffer
        time.sleep(0.3 * self.global_delay_factor)
        self.clear_buffer()

    def enable(self, cmd="enable", pattern="ssword", re_flags=re.IGNORECASE):
        return super(TpLinkJetstreamBase, self).enable(cmd=cmd, pattern=pattern, re_flags=re_flags)

    def check_enable_mode(self, check_string="#"):
        return super(TpLinkJetstreamBase, self).check_enable_mode(check_string=check_string)

    def check_config_mode(self, check_string="(config)#"):
        """Checks if the device is in configuration mode or not."""
        return super(TpLinkJetstreamBase, self).check_config_mode(check_string=check_string)

    def config_mode(self, config_command="configure"):
        """Enter configuration mode."""
        return super(TpLinkJetstreamBase, self).config_mode(config_command=config_command)

    def exit_config_mode(self, exit_config="exit"):
        """Exit configuration mode."""
        return super(TpLinkJetstreamBase, self).exit_config_mode(exit_config=exit_config)

    def exit_enable_mode(self, exit_command="exit"):
        """Exit enable mode."""
        return super(TpLinkJetstreamBase, self).exit_enable_mode(exit_command=exit_command)

    def save_config(self, cmd="copy running-config startup-config", confirm=False):
        """Saves configuration."""
        return super(TpLinkJetstreamBase, self).save_config(cmd=cmd, confirm=confirm)


class TpLinkJetstreamSSH(TpLinkJetstreamBase):
    def __init__(self, *args, **kwargs):
        default_enter = kwargs.get("default_enter")
        kwargs["default_enter"] = "\r\n" if default_enter is None else default_enter
        super(TpLinkJetstreamSSH, self).__init__(*args, **kwargs)


class TpLinkJetstreamTelnet(TpLinkJetstreamBase):
    def telnet_login(
        self,
        pri_prompt_terminator="#",
        alt_prompt_terminator=">",
        username_pattern=r"User:",
        pwd_pattern=r"assword:",
        delay_factor=1,
        max_loops=200,
    ):
        """Telnet login: can be username/password or just password."""
        super(TpLinkJetstreamTelnet, self).telnet_login(
            pri_prompt_terminator=pri_prompt_terminator,
            alt_prompt_terminator=alt_prompt_terminator,
            username_pattern=username_pattern,
            pwd_pattern=pwd_pattern,
            delay_factor=delay_factor,
            max_loops=max_loops,
        )

