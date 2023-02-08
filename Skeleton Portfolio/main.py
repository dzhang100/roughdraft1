from templates import create_app

from flask import Blueprint, render_template, request #allows us to flash a message


app = create_app()



if __name__ == '__main__':
    app.run(debug = True)

