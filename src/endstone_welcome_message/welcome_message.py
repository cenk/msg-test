from endstone import ColorFormat
from endstone.plugin import Plugin
from endstone.event import event_handler, PlayerJoinEvent
import time

class WelcomeMessage(Plugin):
    api_version = "0.9"

    def on_enable(self) -> None:
        self.save_default_config()
        self.register_events(self)
        self.welcome_message_type = max(0, min(int(self.config["welcome_message"]["type"]), 5))

        if self.welcome_message_type > 0:
            self.welcome_message_header = str(self.config["welcome_message"]["header"])
            self.welcome_message_body = str(self.config["welcome_message"]["body"])
            self.welcome_message_wait_before = max(0, min(int(self.config["welcome_message"]["wait_before"]), 10))
        else:
            self.logger.info("Welcome Message is disabled in the config file!")

    @event_handler
    def on_player_join(self, event: PlayerJoinEvent):
        if self.welcome_message_type > 0:
            if self.welcome_message_wait_before > 0:
                time.sleep(self.welcome_message_wait_before)
            match self.welcome_message_type:
                case 1:
                    event.player.send_message(self.welcome_message_body)
                case 2:
                    event.player.send_tip(self.welcome_message_body)
                case 3:
                    event.player.send_toast(self.welcome_message_header, self.welcome_message_body)
                case 4:
                    event.player.send_title(self.welcome_message_header, self.welcome_message_body)
                case 5:
                    event.player.send_popup(self.welcome_message_body)
