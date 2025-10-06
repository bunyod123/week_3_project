import logging

def logs(self):

    logging.basicConfig(
    filename=r"C:\Users\bunyo\OneDrive\Desktop\3_week_project\log\otherInfo.log",
    filemode='a',
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s-%(message)s"

)

