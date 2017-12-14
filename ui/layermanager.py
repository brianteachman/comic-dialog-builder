

class LayerManager:
    """ """
    def __init__(self, canvas):
        self.canvas = canvas
        self.current_layer = 0

    def set_layer(self, cid):
        self.current_layer = self.canvas.find_withtag('caption-'+str(cid))[0]
        print(self.current_layer)

    def raise_layer(self, object_id):
        self.canvas.tag_raise(object_id)

    def lower_layer(self, object_id):
        self.canvas.tag_lower(object_id)
