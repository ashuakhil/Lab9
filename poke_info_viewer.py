""" 
Description: 
  Graphical user interface that displays select information about a user-specified Pokemon fetched from the PokeAPI 
Usage:
  python poke_info_viewer.py
"""

from tkinter import *
from tkinter import ttk, messagebox
from poke_api import get_pokemon_info  
from tkinter import messagebox

root = Tk()
root.title("Pokemon Information")

Frame_input = ttk.Frame(root)
Frame_input.grid(row=1, column=0, columnspan=2, pady=(20, 10))

Frame_info = ttk.Labelframe(root, text="Info")
Frame_info.grid(row=2, column=0, padx=(20, 10), pady=(10, 20), sticky=N)

Frame_stats = ttk.Labelframe(root, text="Stats")
Frame_stats.grid(row=2, column=1, padx=(10, 20), pady=(10, 20), sticky=N)

label_name = ttk.Label(Frame_input, text="Pokemon Name:")
label_name.grid(row=0, column=0, padx=(10, 5), pady=10, sticky=E)

enter_name = ttk.Entry(Frame_input)
enter_name.grid(row=0, column=1, padx=(0, 5), pady=10, sticky=W)

def handle_button_get_info():
    poke_name = enter_name.get().strip()
    if poke_name == '':
        return
    
    poke_info = get_pokemon_info(poke_name)
    if poke_info:
        try:
            types_list = [t['type']['name'].capitalize() for t in poke_info['types']]
            types_str = ", ".join(types_list)
            label_types_value.config(text=types_str)
            
            label_height_value.config(text=str(poke_info['height']) + ' dm')
            label_weight_value.config(text=str(poke_info['weight']) + ' hg')
            
            label_special_attack_bar['value'] = poke_info['stats'][3]['base_stat']
            label_special_defense_bar['value'] = poke_info['stats'][4]['base_stat']
            label_speed_bar['value'] = poke_info['stats'][5]['base_stat']
            label_hp_bar['value'] = poke_info['stats'][0]['base_stat']
            label_attack_bar['value'] = poke_info['stats'][1]['base_stat']
            label_defense_bar['value'] = poke_info['stats'][2]['base_stat']
            
        except KeyError:
            messagebox.showerror("Error", "Invalid Pokemon name")
      

Button_get_info = ttk.Button(Frame_input, text='Get Info', command=handle_button_get_info)
Button_get_info.grid(row=0, column=2, padx=10, pady=10)

label_types = ttk.Label(Frame_info, text="Type(s):")
label_types.grid(row=0, column=0, padx=(10, 5), pady=(10, 5), sticky=E)

label_types_value = ttk.Label(Frame_info, width=20)
label_types_value.grid(row=0, column=1, padx=(0, 10), pady=(10, 5), sticky=W)

label_height = ttk.Label(Frame_info, text="Height:")
label_height.grid(row=1, column=0, padx=(10, 5), pady=(0, 5), sticky=E)

label_height_value = ttk.Label(Frame_info, width=20)
label_height_value.grid(row=1, column=1, padx=(0, 10), pady=(0, 5), sticky=W)

label_weight = ttk.Label(Frame_info, text="Weight:")
label_weight.grid(row=2, column=0, padx=(10, 5), pady=(0, 5), sticky=E)

label_weight_value = ttk.Label(Frame_info, width=20)
label_weight_value.grid(row=2, column=1, padx=(0, 10), pady=(0, 5), sticky=W)

label_special_attack = ttk.Label(Frame_stats, text="Special Attack:")
label_special_attack.grid(row=0, column=0, padx=(10, 5), pady=(10, 5), sticky=E)

label_special_attack_bar = ttk.Progressbar(Frame_stats, orient=HORIZONTAL, length=100, mode='determinate')
label_special_attack_bar.grid(row=0, column=1, padx=(0, 10), pady=(10, 5), sticky=W)

label_special_defense = ttk.Label(Frame_stats, text="Special Defense:")
label_special_defense.grid(row=1, column=0, padx=(10, 5), pady=(0, 5), sticky=E)

label_special_defense_bar = ttk.Progressbar(Frame_stats, orient=HORIZONTAL, length=100, mode='determinate')
label_special_defense_bar.grid(row=1, column=1, padx=(0, 10), pady=(0, 5), sticky=W)

label_speed = ttk.Label(Frame_stats, text="Speed:")
label_speed.grid(row=2, column=0, padx=(10, 5), pady=(0, 5), sticky=E)

label_speed_bar = ttk.Progressbar(Frame_stats, orient=HORIZONTAL, length=100, mode='determinate')
label_speed_bar.grid(row=2, column=1, padx=(0, 10), pady=(0, 5), sticky=W)

label_hp = ttk.Label(Frame_stats, text="HP:")
label_hp.grid(row=3, column=0, padx=(10, 5), pady=(0, 5), sticky=E)

label_hp_bar = ttk.Progressbar(Frame_stats, orient=HORIZONTAL, length=100, mode='determinate')
label_hp_bar.grid(row=3, column=1, padx=(0, 10), pady=(0, 5), sticky=W)

label_attack = ttk.Label(Frame_stats, text="Attack:")
label_attack.grid(row=4, column=0, padx=(10, 5), pady=(0, 5), sticky=E)

label_attack_bar = ttk.Progressbar(Frame_stats, orient=HORIZONTAL, length=100, mode='determinate')
label_attack_bar.grid(row=4, column=1, padx=(0, 10), pady=(0, 5), sticky=W)

label_defense = ttk.Label(Frame_stats, text="Defense:")
label_defense.grid(row=5, column=0, padx=(10, 5), pady=(0, 5), sticky=E)

label_defense_bar = ttk.Progressbar(Frame_stats, orient=HORIZONTAL, length=100, mode='determinate')
label_defense_bar.grid(row=5, column=1, padx=(0, 10), pady=(0, 5), sticky=W)

root.mainloop()
