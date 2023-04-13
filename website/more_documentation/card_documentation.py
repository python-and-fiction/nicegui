from nicegui import ui

from ..documentation_tools import text_demo


def main_demo() -> None:
    with ui.card().tight() as card:
        ui.image('https://picsum.photos/id/684/640/360')
        with ui.card_section():
            ui.label('Lorem ipsum dolor sit amet, consectetur adipiscing elit, ...')


def more() -> None:
    @text_demo('The issue with nested borders', '''
        The following example shows a table nested in a card.
        Cards have a default padding in NiceGUI, so the table is not flush with the card's border.
        The table has the `flat` and `bordered` props set, so it should have a border.
        However, due to the way QCard is designed, the border is not visible (first card).
        There are two ways to fix this:

        - To get the original QCard behavior, use the `tight` method (second card).
            It removes the padding and the table border collapses with the card border.
        
        - To preserve the padding _and_ the table border, move the table into another container like a `ui.row` (third card).

        See https://github.com/zauberzeug/nicegui/issues/726 for more information.
    ''')
    def custom_context_menu() -> None:
        columns = [{'name': 'age', 'label': 'Age', 'field': 'age'}]
        rows = [{'age': '16'}, {'age': '18'}, {'age': '21'}]

        with ui.row():
            with ui.card():
                ui.table(columns, rows).props('flat bordered')

            with ui.card().tight():
                ui.table(columns, rows).props('flat bordered')

            with ui.card():
                with ui.row():
                    ui.table(columns, rows).props('flat bordered')
