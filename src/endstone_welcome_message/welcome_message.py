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
        self.load_config()
        self.register_events(self)

    @event_handler
    def on_player_join(self, event: PlayerJoinEvent):
        event.player.send_toast("Welcome", ColorFormat.YELLOW + f"Welcome {event.player.name}!")

    def save_message(self) -> None:
        self.plugin.config["notice"]["title"] = self.notice_title
        self.plugin.config["notice"]["body"] = self.notice_body
        self.plugin.config["notice"]["button"] = self.notice_button
        self.plugin.save_config()
