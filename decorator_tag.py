class TextTag:
    def __init__(self, text: str):
        self.text = text
    def render(self) -> str:
        return f"{self.text}"

class Bold(TextTag): # <= decorator
    def __init__(self, tag: TextTag):
        self.tag = tag
    def render(self):
        return f"<b>{self.tag.render()}</b>"

class Italic:... 
    
tag = TextTag("Hello world")
tag = Bold(tag) # <=  decorar ou aplicar o estilo bold
# <b>Hello world</b>
print(tag.render())
# <i><b>Hello world</b></i>
