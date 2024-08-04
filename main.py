import uvicorn
from positions.api import app
from positions.jsonDump import DumpJson
from positions.tgBot import tgapp


RUN_API = False
DUMP_TO_JSON = True
POST_TO_TG = False


def Runner():
    if RUN_API:
        uvicorn.run(app, host="0.0.0.0")

    elif DUMP_TO_JSON:
        DumpJson()

    elif POST_TO_TG:
        print("Use /photo command to start uploading in your channel")
        tgapp.run_polling()


if __name__ == '__main__':
    Runner()
