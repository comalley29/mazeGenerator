class InputUserData():
    class Meta:
        fields = ['Style', 'Height', 'Width']


from django import forms

Maze_Styles =(
    ("1", "Aldousbroder"),
    ("2", "Backtracking"),
    ("3", "Binary-Tree"),
    ("4", ""),
    ("5", ""),
)

class MazeInputs(forms.Form):
    styles_field = forms.ChoiceField(choices = Maze_Styles)
    height_field = forms.IntegerField(help_text = "Enter a value for the height of the maze.")
    width_field = forms.IntegerField(help_text = "Enter a value for the width of the maze.")
    


