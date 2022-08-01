from website import create_app #import anything that is definde in website folder, for example create_app function

app = create_app()

if __name__ == '__main__': #only if we run this file (not import it) we will execute the following:
    app.run(port=8080,debug=True) #run Flask application, debut=True re-runs webserver on code change 