from app import app  # Adjust this import based on your project structure

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()
