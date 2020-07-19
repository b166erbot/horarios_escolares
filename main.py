from src.horarios_escolares import main
from contextlib import suppress


if __name__ == '__main__':
    with suppress((KeyboardInterrupt, EOFError)):
        main()
