import logging
import os

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

PLACEHOLDERS = ["name", "event_title", "event_date", "event_location"]


def generate_invitations(template, attendees):
    # 1. Check input types
    if not isinstance(template, str):
        logging.error(f"Invalid input: template must be a string, got {type(template).__name__}.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        logging.error(
            f"Invalid input: attendees must be a list of dictionaries, got {type(attendees).__name__}."
        )
        return

    # 2. Check empty inputs
    if template.strip() == "":
        logging.error("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        logging.error("No data provided, no output files generated.")
        return

    # 3. Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        content = template
        for key in PLACEHOLDERS:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            content = content.replace("{" + key + "}", str(value))

        # 4. Write the output file
        filename = f"output_{index}.txt"
        if os.path.exists(filename):
            logging.warning(f"{filename} already exists and will be overwritten.")
        try:
            with open(filename, "w") as file:
                file.write(content)
        except OSError as e:
            logging.error(f"Could not write {filename}: {e}")
