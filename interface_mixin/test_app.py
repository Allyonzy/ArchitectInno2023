from app import InnerDataMixin

def mixin(*mixin_classes, **mixin_kwargs): # decorator factory function
    def decorator(cls): # decorator function
        class wrapper(*mixin_classes, cls):
            def __init__(self, *args, **kwargs):
                wrapped_kwargs = mixin_kwargs.copy() # use the passed kwargs to update the
                wrapped_kwargs.update(kwargs)        # mixin args, so caller can override
                super().__init__(*args, **wrapped_kwargs)
        # maybe modify wrapper's __name__, __qualname__, __doc__, etc. to match cls here?
        return wrapper
    return decorator

class GraphicalEntity:
    def __init__(self, pos_x: float = 0.0, pos_y: float = 0.0, size_x: float = 0, size_y: float = 0):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__size_x = size_x
        self.__size_y = size_y

    @property
    def pos_x(self):
        return self.__pos_x
    
    @property
    def pos_y(self):
        return self.__pos_y
    
    @property
    def size_x(self):
        return self.__size_x
    
    @property
    def size_y(self):
        return self.__size_y

@mixin(InnerDataMixin)
class Button(GraphicalEntity):
    def __init__(self, pos_x=0.0, pos_y=0.0, size_x=0.0, size_y=0.0):
        GraphicalEntity.__init__(pos_x, pos_y, size_x, size_y)
        print(self.dict_data)
        self.__status = 'Enable'

    @property
    def status(self):
        return self.__status

    def toggle(self):
        self.__status = 'Active'

    def __str__(self):
        return "Button (pos_x: {}, pos_y: {}, size_x: {}, size_y: {}, status: {})".format(
            self.pos_x, 
            self.pos_y, 
            self.size_x, 
            self.size_y, 
            self.status
            )



class ResizableMixin:
    def resize(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y

class ResizableGraphicalEntity(GraphicalEntity, ResizableMixin):
    pass


    
# def tkinter_app():
#     root = Tk()
#     root.title("Test_desktop")
#     root.geometry("250x200")
#     button_03 = ttk.Button(text='Test')
#     button_03.pack()
    
#     root.mainloop()

if __name__=='__main__':
    button_01 = Button()
    print(button_01)
    button_02 = Button(100, 200, 300, 100)
    print(button_02)

    # tkinter_app()