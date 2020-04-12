import project

app = project.create_app()

if __name__ == '__main__':
    app.run(debug=True)