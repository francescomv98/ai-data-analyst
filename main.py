from src.ui import create_interface

def main() -> None:
    app = create_interface()
    # open the UI in the default browser as soon as the server is up
    app.launch(inbrowser=True)

if __name__ == "__main__":
    main()
