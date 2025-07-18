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

    @event_handler
    def on_player_join(self, event: PlayerJoinEvent):
        message_type = self.config["message"]["type"]
        message_title = self.config["message"]["title"]
        message_text = self.config["message"]["text"]
        
        event.player.send_toast(message_title, message_text)

    def save_message(self) -> None:
        self.config["notice"]["title"] = self.notice_title
        self.plugin.config["notice"]["body"] = self.notice_body
        self.plugin.config["notice"]["button"] = self.notice_button
        self.plugin.save_config()
