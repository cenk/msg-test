from endstone import ColorFormat
from endstone.plugin import Plugin
from endstone.event import event_handler, PlayerJoinEvent
import time

class WelcomeMessage(Plugin):
    api_version = "0.9"

    def on_enable(self) -> None:
        self.save_default_config()
        self.register_events(self)
        self.welcome_message_enabled = bool(self.config["welcome_message"]["enabled"])

        if self.welcome_message_enabled:
            self.welcome_message_type = str(self.config["welcome_message"]["type"])
            self.welcome_message_title = str(self.config["welcome_message"]["title"])
            self.welcome_message_text = str(self.config["welcome_message"]["text"])
            self.welcome_message_wait_before = max(0, min(int(self.config["welcome_message"]["wait_before"]), 10))
        else:
            self.logger.info("Welcome Message is disabled in the config file!")

    @event_handler
    def on_player_join(self, event: PlayerJoinEvent):
        if self.welcome_message_enabled:
            if self.welcome_message_wait_before > 0:
                time.sleep(self.welcome_message_wait_before)
            match self.welcome_message_type:
                case "chat":
                    event.player.send_message(self.welcome_message_text)
                case "tip":
                    event.player.send_tip(self.welcome_message_text)
                case "toast":
                    event.player.send_toast(self.welcome_message_title, self.welcome_message_text)
                case _:
                    pass
