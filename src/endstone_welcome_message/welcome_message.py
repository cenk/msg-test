from endstone import ColorFormat
from endstone.plugin import Plugin
from endstone.event import event_handler, PlayerJoinEvent
import time

class WelcomeMessage(Plugin):
    api_version = "0.9"

    def on_enable(self) -> None:
        self.save_default_config()
        self.register_events(self)
        self.welcome_message_type = self.config[welcome_message]["type"]
        self.welcome_message_title = self.config[welcome_message]["title"]
        self.welcome_message_text = self.config[welcome_message]["text"]
        self.welcome_message_wait_before = self.config[welcome_message]["wait_before"]
        
    @event_handler
    def on_player_join(self, event: PlayerJoinEvent):
        match self.welcome_message_type:
            case 0:
                self.logger.info("Welcome Message is disabled in the config file!")
            case 1:
                event.player.send_message(self.welcome_message_text)
            case 2:
                event.player.send_tip(self.welcome_message_text)
            case 3:
                event.player.send_toast(self.welcome_message_title, self.welcome_message_text)
            case _:
                pass
