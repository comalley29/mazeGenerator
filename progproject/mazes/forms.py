class InputUserData():
    class Meta:
        fields = ['Style', 'Height', 'Width']


from django import forms

Maze_Styles =(
    ("1", "Aldousbroder"),
    ("2", "Backtracking"),
    ("3", "Binary-Tree"),
    ("4", "Cellular-Automation "),
    ("5", "Dungeon-Rooms"),
    ("6", "Ellers"),
    ("7", "Growing-Tree"),
    ("8", "Hunt-and-Kill"),
    ("9", "Kruskals"),
    ("10", "Prims"),
    ("11", "Recursive-Division"),
    ("12", "Sidewinder"),
    ("13", "Wilsons"),

)

class MazeInputs(forms.Form):
    styles_field = forms.ChoiceField(choices = Maze_Styles)
    height_field = forms.IntegerField(help_text = "Enter a value for the height of the maze.")
    width_field = forms.IntegerField(help_text = "Enter a value for the width of the maze.")
    


