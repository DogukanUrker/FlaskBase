"""
This module contains the code for the Log class.

The Log class contains methods to log messages of different types (e.g., danger, success, warning, info, app, sql) with date and time. It also includes a method to print a breaker line.

The code is organized as follows:

Imports: The necessary modules are imported.

Define Log class: A Log class is defined, which contains the methods.

Log.danger: Logs a danger message.
Log.success: Logs a success message.
Log.warning: Logs a warning message.
Log.info: Logs an info message.
Log.app: Logs an app message.
Log.sql: Logs an SQL message.
Log.breaker: Prints a breaker line.

Note: The code is written in Python 3.12.
"""
import os

from config import Config
from utils.time import currentTime, currentTimeZone, currentDate

# Ensure the log folder exists
if not os.path.exists(Config.LOG_FOLDER_ROOT):
    os.makedirs(Config.LOG_FOLDER_ROOT)


class Log:
    @staticmethod
    def logMessage(level: str, message: str, logFile: str, colorCode: str, bgColorCode: str) -> None:
        """
        Logs a message with a timestamp to the console and to a log file.

        Args:
            level (str): The log level (e.g., "DANGER").
            message (str): The message to log.
            logFile (str): The path to the log file.
            colorCode (str): The ANSI color code for text color.
            bgColorCode (str): The ANSI color code for background color.
        """
        if Config.CUSTOM_LOGGER:
            # Print formatted message with timestamp
            print(
                f"\033[38;2;244;63;94m{Config.APP_NAME}@{Config.APP_VERSION}\033[0m"  # App name and version
                "\033[38;2;115;115;115m[\033[0m"  # Open brackets
                f"\033[38;2;217;70;239m{currentDate()}\033[0m"  # Date
                "\033[38;2;115;115;115m |\033[0m"  # Vertical line
                f"\033[38;2;236;72;153m {currentTime()}\033[0m"  # Time
                "\033[38;2;115;115;115m |\033[0m"  # Vertical line
                f"\033[38;2;168;85;247m {currentTimeZone()}\033[0m"  # Time zone
                "\033[38;2;115;115;115m] \033[0m"  # Close brackets
                f"\033[{colorCode}m"  # Text color
                f"\033[{bgColorCode}m"  # Background color
                f"\033[1m {level} \033[0m"  # Log level in bold
                f"\033[0m"  # Reset color
                f"\033[0m"  # Reset color
                f" {message}\033[0m\n"  # Message
            )
            # Write to log files
            with open(Config.LOG_FILE_ROOT, "a", encoding="utf-8") as logFileHandle:
                logFileHandle.write(
                    f"[{currentDate()}|{currentTime()}|{currentTimeZone()}]\t{level} | {message}\n"
                )
            with open(logFile, "a", encoding="utf-8") as specificLogFile:
                specificLogFile.write(
                    f"[{currentDate()}|{currentTime()}|{currentTimeZone()}]\t{message}\n"
                )

    @staticmethod
    def danger(message: str = "NONE") -> None:
        Log.logMessage("DANGER", message, Config.LOG_DANGER_FILE_ROOT, "38;2;220;38;38", "48;2;248;113;113")

    @staticmethod
    def success(message: str = "NONE") -> None:
        Log.logMessage("SUCCESS", message, Config.LOG_SUCCESS_FILE_ROOT, "38;2;22;163;74", "48;2;74;222;128")

    @staticmethod
    def warning(message: str = "NONE") -> None:
        Log.logMessage("WARNING", message, Config.LOG_WARNING_FILE_ROOT, "38;2;234;88;12", "48;2;251;146;60")

    @staticmethod
    def info(message: str = "NONE") -> None:
        Log.logMessage("INFO", message, Config.LOG_INFO_FILE_ROOT, "38;2;37;99;235", "48;2;96;165;250")

    @staticmethod
    def app(message: str = "NONE") -> None:
        Log.logMessage("APP", message, Config.LOG_APP_FILE_ROOT, "38;2;8;145;178", "48;2;32;211;238")

    @staticmethod
    def sql(message: str = "NONE") -> None:
        Log.logMessage("SQL", message, Config.LOG_SQL_FILE_ROOT, "38;2;13;148;136", "48;2;45;212;191")

    @staticmethod
    def breaker() -> None:
        """
        Prints a breaker to the console and appends the line to the log file.
        """
        if Config.CUSTOM_LOGGER:
            # Print breaker line
            print(f"\033[38;2;115;155;155m{Config.BREAKER_TEXT}\033[0m")
            # Append to log file
            with open(Config.LOG_FILE_ROOT, "a", encoding="utf-8") as logFileHandle:
                logFileHandle.write(Config.BREAKER_TEXT + "\n")
