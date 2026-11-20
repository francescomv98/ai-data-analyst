from src.ui import create_interface

def main() -> None:
    app = create_interface()
    app.launch(inbrowser=True)

if __name__ == "__main__":
    main()
