

class LayerManager:
    """ """

    def __init__(self, canvas):
        self.canvas = canvas
        self.current_layer = 0
        self.layers = []

    def set_layer(self, cid):
        self.current_layer = self.canvas.find_withtag('caption-'+str(cid))[0]
        print(self.current_layer)

    def raise_layer(self, object_id):
        self.canvas.tag_raise(object_id)

    def lower_layer(self, object_id):
        self.canvas.tag_lower(object_id)

    # -------------------------------------------------------------------------
    # https://stackoverflow.com/a/9576938/503781
    def add_to_layer(self, layer, command, coords, **kwargs):
        """
        :param layer:   int
        :param command: Canvas.element
        :param coords:  (x0, y0, x1, y1)
        :param kwargs:
        :return:        int
        """
        layer_tag = "layer %s" % layer
        if layer_tag not in self.layers:
            self.layers.append(layer_tag)
        tags = kwargs.setdefault("tags", [])
        tags.append(layer_tag)
        item_id = command(coords, **kwargs)
        self._adjust_layers()
        return item_id

    def _adjust_layers(self):
        for layer in sorted(self.layers):
            self.canvas.lift(layer)

    # -------------------------------------------------------------------------
