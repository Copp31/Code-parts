#! /usr/bin/env python
from mon_app import app, ard

if __name__ == "__main__":
   
    app.run(debug=True)
    ard.run()

"""  app.run(host='192.168.0.103', port=5000, debug=True, threaded=False) """