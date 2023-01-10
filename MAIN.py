import sys
import logging
import time

class invalidlogin(Exception):
    pass
class Main:
    stat=False
    def run_db(self):
        import DB_Connection
        DB = DB_Connection.DB_Access()
        DB.main_screen()
        self.stat = DB.return_status()

    def run_Router_Packet_Details(self):
        try:
            if self.stat:
                import Router_Packet_Details
            else:
                raise invalidlogin
        except:
            logging.error("UNAUTHORISED USER")
            sys.exit("Please Login to access Router Packet Details")

    def run_Ping_monitoring(self):
        try:
            if self.stat:
                import Ping_monitoring
            else:
                raise invalidlogin
        except:
            logging.error("UNAUTHORISED USER")
            sys.exit("Please Login to access Ping Monitoring")

    def get_bandwidth(self):
        try:
            if self.stat:
                import BANDWIDTH
            else:
                raise invalidlogin
        except:
            logging.error("UNAUTHORISED USER")
            sys.exit("Please Login to access Get Bandwidth")

    def port_finding(self):
        try:
            if self.stat:
                import FINDING_PORT
            else:
                raise invalidlogin
        except:
            logging.error("UNAUTHORISED USER")
            sys.exit("Please Login to access Port Finding")

    def ModelDP(self):
        try:
            if self.stat:
                import MDP
            else:
                raise invalidlogin
        except:
            logging.error("UNAUTHORISED USER")
            sys.exit("Please Login to access Model Driven Programmability")


def exitprogram():
    logging.info("exited program")
    sys.exit("System Exiting")


def printerror():
    print("Invalid Option Entered")

main = Main()

def run():
    menu = {
        1: main.run_db,
        2: main.run_Router_Packet_Details,
        3: main.run_Ping_monitoring,
        4: main.get_bandwidth,
        5: main.port_finding,
        6: main.ModelDP,
        7: exitprogram
    }
    logging.basicConfig(filename='Log'+time.strftime("%Y%m%d-%H%M%S"),level=logging.INFO)
    logging.info("Main program started")

    while True:
        print(
            "\n1:Establish DataBase connection\n2:Get router packet details\n3:Ping Monitoring\n4:Get Bandwidth\n5:Port Finding\n"
            "6:Model Driven Programmability\n7:Exit Program\nEnter your choice?",end='')
        logging.info("choises are displayed")
        try:
            choice = int(input())
        except ValueError:
            print("Please Enter Valid Input!")
        menu.get(choice, printerror)()

run()