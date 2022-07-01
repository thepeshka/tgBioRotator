from tg.app import get_tg_app


def authorize():
    get_tg_app().start()


if __name__ == '__main__':
    authorize()
    print("Authorization successful!")
