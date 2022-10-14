from website import create_app

app = create_app()

"""
if __name__ == '__main__':
    app.run(debug=True)"""


if __name__ == "__main__":
    from waitress import serve
    print("[Starting Server]")
    serve(app, host="0.0.0.0", port=80)