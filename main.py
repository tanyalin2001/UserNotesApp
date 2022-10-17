from website import create_app

app = create_app()

if __name__ == '__main__': #only if we run this file not when we import main.py are we going to execute this line
  app.run(debug=True) # every time when we make any change at our python code, it's going to rerun the web server