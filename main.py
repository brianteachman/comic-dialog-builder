from ui.app import App

app = App()

# Example scene

app.load_scene('imgs/saiyaman.gif')
caption = ("I am the hope of the universe. I am the answer to all living things "
           "that cry out for peace. I am protector of the innocent. I am the "
           "light in the darkness. I am truth. Ally to good! Nightmare to you!"
           )  # speech bubble
# caption = "What's that?"  # thought bubble
app.add_caption(caption)

app.run()
