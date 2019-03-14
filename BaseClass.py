import configparser
import openpyxl


class BaseClass():
    config=configparser.ConfigParser()
    config.read("test_config.cfg" )
    BASE_URL=config.get("TestEnvironment", "BASE_URL")
    API_KEY=config.get("TestEnvironment", "API_KEY")
    xl=openpyxl.load_workbook("XL_Driver.xlsx")
    sheet=xl["SmokeTest"]
