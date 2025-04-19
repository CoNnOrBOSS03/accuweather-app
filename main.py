from components.app import App
from config import ACCUWEATHER_API_KEY

if __name__ == '__main__':
    app = App(ACCUWEATHER_API_KEY)
    app.mainloop()
