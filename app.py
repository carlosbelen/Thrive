from health_app import app, routes


# This tells app.py how to behave when called.  In this case, we sumply want it run (so long as it's not being required to do anything else)
if __name__ == '__main__':
    app.run(debug = True)
