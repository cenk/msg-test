from endstone import ColorFormat
from endstone.plugin import Plugin
from endstone.event import event_handler, PlayerJoinEvent

class WelcomeMessage(Plugin):
    api_version = "0.9"

    def on_load(self) -> None:
        self.logger.info("on_load is called!")

    def on_enable(self) -> None:
        self.logger.info("on_enable is called!")
        self.save_default_config()
        self.register_events(self)
        message_type = self.config["welcome"]["message_type"]
        toast_title = self.config["welcome"]["toast_title"]
        message_text = self.config["welcome"]["message_text"]
        
    @event_handler
    def on_player_join(self, event: PlayerJoinEvent):
        match message_type:
            case 0:
                self.logger.info("Welcome Message is disabled in the config file!")
            case 1:
                event.player.send_message(message_text)
            case 2:
                event.player.send_tip(message_text)
            case 3:
                event.player.send_toast(message_title, message_text)
            case _:
                pass

    def save_message(self) -> None:
        self.config["notice"]["title"] = self.notice_title
        self.plugin.config["notice"]["body"] = self.notice_body
        self.plugin.config["notice"]["button"] = self.notice_button
        self.plugin.save_config()
