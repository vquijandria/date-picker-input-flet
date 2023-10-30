import flet as ft
from flet import *
from datepicker.datepicker import DatePicker
from datepicker.selection_type import SelectionType
from datetime import datetime

class Youdate(UserControl):
    #Docstring for youdate
    def __init__(self):
        super(Youdate, self).__init__()
        self.datepicker = None
        self.holidays = [datetime(2023,4,25),datetime(2023,5,1),datetime(2023,6,2)]
        self.locales = ["en_US"]
        self.selected_locale = None

        #Aqui el resultado que seleccionaste
        self.you_select_date = Text(size=30,weight="bold")

        self.locales_opts = []

        for l in self.locales:
            self.locales_opts.append(
                dropdown.Option(l)
            )
        #Dialog para el input date
        self.dlg_modal = AlertDialog(
            modal=True,
            title=Text("Select date here"),
            actions=[
                TextButton("Cancel",
                           on_click=self.cancel_dlg),
                TextButton("Confirm",
                            on_click=self.confirm_dlg),                               
            ],
            actions_alignment="end",
            actions_padding=5,
            content_padding=0
        )

        self.tf = TextField(
            label="select here",
            dense=True,
            width=260,height=50
        )

        self.cal_icon = TextButton(
            icon=icons.CALENDAR_MONTH,
            on_click=self.open_dlg_modal,
            height=40,
            width=40,
            right=0,
            style=ButtonStyle(
                padding=Padding(4,0,0,0),
                shape={
                    MaterialState.DEFAULT:RoundedRectangleBorder(radius=1)
                }
            )
        )  
        #Ahora se agrega el stack textfield y el icono de calendario
        self.st = Stack([
            self.tf,
            self.cal_icon
        ])
        self.from_to_text = Text(visible=False)


    def build(self):
        return Column([
            Text("Test Date", size=30, weight="bold"),
            
            #Mostrar textfield
            self.st,
            self.from_to_text,
            self.you_select_date
        ])
    
    #Ahora se agrega el metodo para abrir el dialogo
    def confirm_dlg(self,e):
        selected_date = self.datepicker.selected_data[0] if len(self.datepicker.selected_data) > 0 else None
        #Ahora se convierte el formato a DD/MM/YYYY
        selected_data_str = selected_date.strftime("%Y-%m-%dT%H:%M:%S") if selected_date else None
        formated_date = self._format_date(selected_data_str)
        self.tf.value = formated_date
        #Imprime en el terminar el resultado
        print("you date", self.tf.value)
        #Muestra el resultado en pantalla
        self.you_select_date.value = self.tf.value
        #Cierra el dialogo
        self.dlg_modal.open = False
        self.update()
        self.page.update()
    
    #Si haces click en cancelar
    def cancel_dlg(self,e):
        self.dlg_modal.open = False
        self.page.update()

    #Si haces click y muestra el dialogo abierto
    def open_dlg_modal(self,e):
        self.datepicker = DatePicker(
            hour_minute=True,
            selected_date=None,
            selection_type=int(0),
            holidays=self.holidays,
            show_three_months=False,
            locale=self.selected_locale
        )
        self.page.dialog = self.dlg_modal
        self.dlg_modal.content = self.datepicker
        self.dlg_modal.open = True
        self.page.update()

    #Funcion para convertir de formated date a mm/dd/yyyy
    def _format_date(self, date_str):
        if date_str:
            date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
            formated_date = date_obj.strftime("%d %B %Y")
            return formated_date
        else:
            return ""
        
    