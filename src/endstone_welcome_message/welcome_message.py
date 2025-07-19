from endstone import ColorFormat
from endstone.plugin import Plugin
from endstone.event import event_handler, PlayerJoinEvent
from endstone.form import ModalForm, Label
import time

class WelcomeMessage(Plugin):
    api_version = "0.6"

    def on_enable(self) -> None:
        self.save_default_config()
        self.register_events(self)
        self.welcome_message_type = max(0, min(int(self.config["welcome_message"]["type"]), 6))

        if self.welcome_message_type > 0:
            self.welcome_message_header = str(self.config["welcome_message"]["header"])
            self.welcome_message_body = str(self.config["welcome_message"]["body"])
            self.welcome_message_wait_before = max(0, min(int(self.config["welcome_message"]["wait_before"]), 10))
        else:
            self.logger.info("Welcome Message is disabled in the config file!")

    @event_handler
    def on_player_join(self, event: PlayerJoinEvent):
        if self.welcome_message_type > 0:
            self.replace_placeholders(event.player)
            if self.welcome_message_wait_before > 0:
                time.sleep(self.welcome_message_wait_before)
            match self.welcome_message_type:
                case 1:
                    event.player.send_message(self.replace_placeholders(self.welcome_message_body))
                case 2:
                    event.player.send_tip(self.replace_placeholders(self.welcome_message_body))
                case 3:
                    event.player.send_popup(self.replace_placeholders(self.welcome_message_body))
                case 4:
                    event.player.send_toast(self.replace_placeholders(self.welcome_message_header), self.replace_placeholders(self.welcome_message_body))
                case 5:
                    event.player.send_title(self.replace_placeholders(self.welcome_message_header), self.replace_placeholders(self.welcome_message_body))
                case 6:
                    welcome_form = ModalForm(
                        title=self.replace_placeholders(self.welcome_message_header),
                        controls=[Label(text=self.replace_placeholders(self.welcome_message_body) + '\n\n')],
                        submit_button=self.welcome_message_form_button_text
                    )
                    event.player.send_form(welcome_form)

    def replace_placeholders(self, player) -> None:
        placeholder = {
            'player_name': player.name,
            'exp_level': player.exp_level,
            'total_exp': player.total_exp,
            'ping': player.ping,
            'server_level': self.server.level,
            'max_players': self.server.max_players,
            'online_players': len(self.server.online_players),
            'start_time': self.server.start_time
        }
        self.welcome_message_header = self.welcome_message_header.format(**placeholder)
        self.welcome_message_body = self.welcome_message_body.format(**placeholder)
        self.welcome_message_form_button_text = self.welcome_message_form_button_text.format(**placeholder)
