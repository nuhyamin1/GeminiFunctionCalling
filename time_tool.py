import pytz
import datetime

from google.generativeai.types import FunctionDeclaration, Tool

class TimeTool:
    """Encapsulates timezone-aware time utilities and their Gemini declarations."""

    # Declaration for "now" function
    GET_CURRENT_TIME = FunctionDeclaration(
        name="get_current_time",
        description=(
            "Get the current real-time clock time in Asia/Jakarta timezone."
        ),
        parameters=None
    )

    # Declaration for "future" function: one parameter n_hours
    GET_FUTURE_TIME = FunctionDeclaration(
        name="get_future_time",
        description=(
            "Calculate the clock time N hours from now in Asia/Jakarta timezone."
        ),
        parameters={
            "type": "object",
            "properties": {
                "n_hours": {"type": "number", "description": "Number of hours from now"}
            },
            "required": ["n_hours"]
        }
    )

    @staticmethod
    def get_current_time():
        timezone = pytz.timezone("Asia/Jakarta")
        now = datetime.datetime.now(timezone)
        return now.strftime("%I:%M:%S %p %Z")

    @staticmethod
    def get_future_time(n_hours: float):
        timezone = pytz.timezone("Asia/Jakarta")
        now = datetime.datetime.now(timezone)
        future = now + datetime.timedelta(hours=n_hours)
        return future.strftime("%I:%M:%S %p %Z")